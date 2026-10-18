"""Run with: python -m unittest test_flight_excel -v (no UBIKAIS network calls)."""
import io
import unittest
from datetime import date, datetime, time
from unittest.mock import patch

import matplotlib
matplotlib.use("Agg")
import pandas as pd
from streamlit.testing.v1 import AppTest

from flight_excel import read_schedule, schedule_columns, service_dates, template_bytes, timeline_frame
from flight_timeline import TimelineConfig, arrivals_from_ubikais, build_timeline_figure, departures_from_ubikais


DAY = date(2026, 12, 2)


def workbook(rows, direction="dep", columns=None):
    buffer = io.BytesIO()
    pd.DataFrame(rows, columns=columns or schedule_columns(direction)).to_excel(buffer, index=False, engine="openpyxl")
    return buffer.getvalue()


def empty(direction):
    return pd.DataFrame(columns=schedule_columns(direction) + ["SCHEDULED_AT"])


class ScheduleTests(unittest.TestCase):
    def test_template_round_trip(self):
        for direction in ("dep", "arr"):
            frame, errors, warnings = read_schedule(template_bytes(direction), direction)
            self.assertFalse(errors)
            self.assertFalse(warnings)
            self.assertEqual(list(frame.columns[:5]), schedule_columns(direction))
            self.assertEqual(frame.iloc[0]["SCHEDULED_AT"], datetime(2026, 12, 2, 9, 30))

    def test_optional_routes_and_time_formats(self):
        values = ["00:00", "01:00", "23:59", 930, "0930", time(9, 30), 0.5]
        rows = [[DAY, f"ZE{index}", value] for index, value in enumerate(values)]
        frame, errors, _ = read_schedule(workbook(rows, columns=schedule_columns("dep")[:3]), "dep")
        self.assertFalse(errors)
        self.assertTrue((frame["출발지"] == "").all())
        self.assertEqual(frame["STD"].tolist(), ["00:00", "01:00", "23:59", "09:30", "09:30", "09:30", "12:00"])

    def test_errors_and_duplicate_rows(self):
        rows = [
            [DAY, "ZE101", "09:30", "icn", "nrt"],
            [DAY, "ZE101", "09:30", "ICN", "NRT"],
            [DAY, "ZE102", "24:00", "", ""],
            ["bad date", "ZE103", "12:00", "", ""],
            [DAY, "", "12:00", "", ""],
            [DAY, "ZE104", "12:00", "RKSI", ""],
            [None, None, None, None, None],
            [DAY, "ZE105", None, "", ""],
        ]
        frame, errors, warnings = read_schedule(workbook(rows), "dep")
        self.assertEqual(len(frame), 2)
        self.assertEqual(len(errors), 5)
        self.assertEqual(len(warnings), 1)
        self.assertIn("4행", errors[0])
        self.assertIn("3행", warnings[0])

    def test_missing_columns(self):
        _, errors, _ = read_schedule(workbook([[DAY, "ZE101"]], columns=["날짜", "항공편명"]), "dep")
        self.assertIn("STD", errors[0])

    def test_actual_dates_and_service_boundary(self):
        frame, errors, _ = read_schedule(workbook([
            [DAY, "ZE1", "01:59", "", ""],
            [DAY, "ZE2", "02:00", "", ""],
            [date(2026, 12, 3), "ZE3", "00:00", "", ""],
            [date(2026, 12, 3), "ZE4", "01:59", "", ""],
            [date(2026, 12, 3), "ZE5", "02:00", "", ""],
        ]), "dep")
        self.assertFalse(errors)
        self.assertEqual(service_dates(frame, 2), [date(2026, 12, 1), DAY, date(2026, 12, 3)])
        selected = timeline_frame(frame, "dep", DAY, 2)
        self.assertEqual(selected["FLT"].tolist(), ["ZE2", "ZE3", "ZE4"])
        fig, summary = build_timeline_figure(selected, timeline_frame(empty("arr"), "arr", DAY, 2), TimelineConfig(DAY, use_actual_schedule_dates=True))
        try:
            self.assertEqual(summary["dep_records"]["marker"].tolist(), [datetime(2026, 12, 2, 2), datetime(2026, 12, 3, 0), datetime(2026, 12, 3, 1, 59)])
        finally:
            fig.clear()
        self.assertEqual(timeline_frame(frame, "dep", DAY, 0)["FLT"].tolist(), ["ZE1", "ZE2"])

    def test_each_direction_alone_and_downloads(self):
        for direction in ("dep", "arr"):
            frame, _, _ = read_schedule(template_bytes(direction), direction)
            inputs = {key: timeline_frame(frame if key == direction else empty(key), key, DAY, 0) for key in ("dep", "arr")}
            fig, summary = build_timeline_figure(inputs["dep"], inputs["arr"], TimelineConfig(DAY, use_actual_schedule_dates=True))
            try:
                self.assertEqual(summary[f"total_{direction}"], 1)
                for fmt, signature in (("png", b"\x89PNG"), ("pdf", b"%PDF")):
                    buffer = io.BytesIO()
                    fig.savefig(buffer, format=fmt)
                    self.assertTrue(buffer.getvalue().startswith(signature))
            finally:
                fig.clear()

    def test_legacy_time_fallback_and_iata_label(self):
        dep = departures_from_ubikais([{"fpId": "ESR101", "schTime": "0100", "atd": "0130", "apArr": "RJAA"}])
        arr = arrivals_from_ubikais([{"fpId": "ESR102", "sta": "1200", "blockOnTime": "1210", "apIcao": "RKSI"}])
        fig, summary = build_timeline_figure(dep, arr, TimelineConfig(DAY, service_start_hour=2, show_des_org=True))
        try:
            self.assertEqual(summary["dep_records"].iloc[0]["marker"], datetime(2026, 12, 3, 1, 30))
            self.assertEqual(summary["arr_records"].iloc[0]["marker"], datetime(2026, 12, 2, 12, 10))
            self.assertIn("ICN", summary["arr_records"].iloc[0]["Label"])
        finally:
            fig.clear()


class ScreenTests(unittest.TestCase):
    def test_excel_upload_replace_remove_and_invalid(self):
        upload = io.BytesIO(template_bytes("dep"))
        upload.name = "departure.xlsx"
        app = AppTest.from_string("from flight_excel_ui import render_excel_mode\nrender_excel_mode()", default_timeout=60)
        with patch("streamlit.file_uploader", side_effect=lambda label, **kwargs: upload if kwargs["key"] == "excel_upload_dep" else None):
            app.run()
        self.assertFalse(app.exception)
        self.assertEqual([item.value for item in app.metric], ["1", "0"])
        self.assertEqual(len(app.get("download_button")), 4)
        replacement = io.BytesIO(workbook([[date(2027, 3, 5), "ZE900", "01:00", "", ""]]))
        replacement.name = "replacement.xlsx"
        app.number_input(key="excel_service_start_hour").set_value(2)
        with patch("streamlit.file_uploader", side_effect=lambda label, **kwargs: replacement if kwargs["key"] == "excel_upload_dep" else None):
            app.run()
        self.assertFalse(app.exception)
        self.assertEqual(app.selectbox(key="excel_display_date").value, date(2027, 3, 4))
        invalid = io.BytesIO(workbook([[DAY, "ZE900", "25:00", "", ""]]))
        invalid.name = "invalid.xlsx"
        with patch("streamlit.file_uploader", return_value=invalid):
            app.run()
        self.assertFalse(app.exception)
        self.assertTrue(app.error)
        self.assertFalse(app.metric)
        with patch("streamlit.file_uploader", return_value=None):
            app.run()
        self.assertFalse(app.exception)
        self.assertFalse(app.metric)

    def test_mode_switch_preserves_ubikais_state_and_makes_no_excel_api_calls(self):
        def payload(direction, query, airlines, **kwargs):
            record = {"fpId": "ESR101", "schTime": "0900", "sta": "1200", "acType": "B738", "apArr": "RJAA", "apIcao": "RJAA"}
            return {"records": [record], "fetched_at": 0, "query": {}}

        app = AppTest.from_file("before_app.py", default_timeout=90)
        app.session_state["base_date"] = DAY
        with patch("ubikais_client.fetch_records_for_airlines", side_effect=payload) as fetch:
            app.run()
            self.assertFalse(app.exception)
            self.assertTrue(fetch.called)
            app.session_state["team_assignments"] = {"existing": "A"}
            app.radio(key="schedule_input_mode").set_value("엑셀")
            fetch.reset_mock()
            app.run()
            self.assertFalse(app.exception)
            fetch.assert_not_called()
            self.assertEqual(app.session_state["base_date"], DAY)
            self.assertEqual(app.session_state["team_assignments"], {"existing": "A"})
            self.assertEqual(len(app.date_input), 0)
            app.radio(key="schedule_input_mode").set_value("UBIKAIS").run()
            self.assertFalse(app.exception)
            self.assertEqual(app.date_input(key="base_date").value, DAY)
            self.assertEqual(app.session_state["team_assignments"], {"existing": "A"})


if __name__ == "__main__":
    unittest.main()
