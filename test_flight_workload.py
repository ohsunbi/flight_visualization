"""Workload interval rules and shared/connected Streamlit panel tests."""
import io
import unittest
from datetime import date, datetime, time
from unittest.mock import patch

import pandas as pd
from streamlit.testing.v1 import AppTest

from flight_excel import template_bytes
from flight_workload import overlapping_records, query_window


DAY = date(2026, 12, 2)


def dt(clock, day=2):
    return datetime.fromisoformat(f"2026-12-{day:02d}T{clock}")


class IntervalTests(unittest.TestCase):
    def test_partial_full_cover_and_boundary_contact(self):
        rows = [
            ("A", "06:30", "07:20"), ("B", "07:30", "08:10"),
            ("C", "08:40", "09:30"), ("D", "06:00", "07:00"),
            ("E", "09:00", "09:40"), ("F", "06:00", "10:00"),
            ("G", "08:00", "08:00"),
        ]
        records = pd.DataFrame([{"FLT": flight, "start": dt(start), "end": dt(end)} for flight, start, end in rows])
        original = records.copy(deep=True)
        result = overlapping_records(records, dt("07:00"), dt("09:00"))
        self.assertEqual(result["FLT"].tolist(), ["A", "B", "C", "F"])
        pd.testing.assert_frame_equal(records, original)

    def test_empty_and_repeated_flight_names(self):
        self.assertTrue(overlapping_records(pd.DataFrame(), dt("07:00"), dt("09:00")).empty)
        records = pd.DataFrame([{"FLT": "ZE101", "start": dt("07:30"), "end": dt("08:30")}] * 2)
        self.assertEqual(len(overlapping_records(records, dt("07:00"), dt("09:00"))), 2)

    def test_midnight_and_actual_day_mapping(self):
        start, end = query_window(DAY, time(23), time(1), 2)
        self.assertEqual((start, end), (dt("23:00"), dt("01:00", 3)))
        records = pd.DataFrame([{"start": dt("23:30"), "end": dt("00:30", 3)}])
        self.assertEqual(len(overlapping_records(records, start, end)), 1)
        self.assertEqual(query_window(DAY, time(0), time(1), 2), (dt("00:00", 3), dt("01:00", 3)))
        self.assertEqual(query_window(DAY, time(1), time(3), 2), (dt("01:00", 3), dt("03:00", 3)))
        self.assertEqual(query_window(DAY, time(0), time(1), 0), (dt("00:00"), dt("01:00")))

    def test_equal_and_reversed_actual_range_rejected(self):
        with self.assertRaises(ValueError):
            query_window(DAY, time(7), time(7), 0)
        with self.assertRaises(ValueError):
            overlapping_records(pd.DataFrame(), dt("09:00"), dt("07:00"))


HARNESS = '''
from datetime import date
import pandas as pd
import streamlit as st
from flight_workload_ui import render_workload_panel
day = st.date_input("차트 날짜", value=date(2026,12,2), key="test_day")
hour = st.number_input("차트 시작 시각", 0, 23, value=0, key="test_hour")
before = st.number_input("작업시간", value=30, key="test_before")
visible = st.checkbox("출발 필터", value=True, key="test_filter")
dep = pd.DataFrame([{"FLT":"ZE101", "DES":"RKSI", "start":pd.Timestamp(day)+pd.Timedelta(hours=7), "end":pd.Timestamp(day)+pd.Timedelta(hours=8)}])
if not visible:
    dep = dep.iloc[0:0].copy()
arr = pd.DataFrame(columns=dep.columns)
render_workload_panel(summary={"dep_records":dep,"arr_records":arr}, display_date=day,
    day_start_hour=hour,key_prefix="test",chart_context=repr(before))
'''


class ScreenTests(unittest.TestCase):
    def test_result_details_reset_and_zero_results(self):
        app = AppTest.from_string(HARNESS).run()
        self.assertFalse(app.exception)
        app.button(key="test_workload_calculate").click().run()
        self.assertFalse(app.exception)
        result = app.session_state["test_workload_result"]
        self.assertEqual((result["departures"], result["arrivals"]), (1, 0))
        self.assertEqual(app.dataframe[0].value.iloc[0]["출도착지"], "ICN")
        self.assertTrue(any("1편" in card.value for card in app.markdown))
        app.number_input(key="test_before").set_value(50).run()
        self.assertIsNone(app.session_state["test_workload_result"])
        app.button(key="test_workload_calculate").click().run()
        app.checkbox(key="test_filter").uncheck().run()
        self.assertIsNone(app.session_state["test_workload_result"])
        app.button(key="test_workload_calculate").click().run()
        self.assertEqual(app.session_state["test_workload_result"]["departures"], 0)
        self.assertTrue(any("겹치는 조업이 없습니다" in item.value for item in app.info))
        app.date_input(key="test_day").set_value(date(2026, 12, 3)).run()
        self.assertIsNone(app.session_state["test_workload_result"])
        app.button(key="test_workload_calculate").click().run()
        app.number_input(key="test_hour").set_value(2).run()
        self.assertIsNone(app.session_state["test_workload_result"])
        self.assertFalse(app.exception)

    def test_clock_change_equal_time_and_overnight(self):
        app = AppTest.from_string(HARNESS).run()
        app.button(key="test_workload_calculate").click().run()
        app.selectbox(key="test_workload_end_hour").set_value(7)
        # The client selections are pending until the form is submitted.
        self.assertIsNotNone(app.session_state["test_workload_result"])
        app.button(key="test_workload_calculate").click().run()
        self.assertTrue(app.warning)
        app.selectbox(key="test_workload_start_hour").set_value(23)
        app.selectbox(key="test_workload_start_minute").set_value(50)
        app.selectbox(key="test_workload_end_hour").set_value(1)
        app.selectbox(key="test_workload_end_minute").set_value(10)
        app.button(key="test_workload_calculate").click().run()
        self.assertFalse(app.exception)
        self.assertEqual(app.session_state["test_workload_result"]["start"], dt("23:50"))
        self.assertEqual(app.session_state["test_workload_result"]["end"], dt("01:10", 3))

    def test_english_expander_hour_minute_form_and_validation(self):
        app = AppTest.from_string(HARNESS.replace("chart_context=repr(before))", 'chart_context=repr(before),language="en")')).run()
        self.assertFalse(app.exception)
        self.assertFalse(app.time_input)
        self.assertFalse(app.text_input)
        panel = next(item for item in app.expander if item.label == "Handling count by time range")
        self.assertFalse(panel.proto.expanded)
        self.assertEqual(app.selectbox(key="test_workload_start_hour").label, "Start hour")
        self.assertEqual(app.selectbox(key="test_workload_start_hour").options, [f"{hour:02d}" for hour in range(24)])
        for suffix in ("start_minute", "end_minute"):
            widget = app.selectbox(key=f"test_workload_{suffix}")
            self.assertEqual(widget.options, ["00", "10", "20", "30", "40", "50"])
            self.assertEqual(widget.proto.form_id, "test_workload_form")
        self.assertEqual(app.button(key="test_workload_calculate").label, "Calculate")
        app.button(key="test_workload_calculate").click().run()
        self.assertFalse(app.exception)
        self.assertEqual(app.session_state["test_workload_result"]["departures"], 1)
        self.assertEqual(list(app.dataframe[0].value.columns), ["Direction", "Flight", "ORG/DES", "Handling start", "Handling end"])
        self.assertEqual(app.dataframe[0].value.iloc[0]["Direction"], "Departure")
        app.selectbox(key="test_workload_start_hour").set_value(9)
        app.button(key="test_workload_calculate").click().run()
        self.assertFalse(app.exception)
        self.assertIn("must be different", app.warning[0].value)
        self.assertIsNone(app.session_state["test_workload_result"])
        for caption in app.caption:
            self.assertFalse(any("가" <= char <= "힣" for char in caption.value))

    def test_connected_modes_and_panel_locations(self):
        def payload(direction, query, airlines, **kwargs):
            return {"records": [{"fpId": "ESR101", "schTime": "0800", "sta": "0830", "acType": "B738"}], "fetched_at": 0}

        upload = io.BytesIO(template_bytes("dep"))
        upload.name = "departures.xlsx"
        app = AppTest.from_file("before_app.py", default_timeout=90)
        app.session_state["base_date"] = DAY
        with patch("ubikais_client.fetch_records_for_airlines", side_effect=payload) as fetch:
            app.run()
            radio = app.radio(key="schedule_input_mode")
            self.assertEqual(radio.options, ["UBIKAIS", "Excel"])
            self.assertTrue(radio.proto.horizontal)
            self.assertTrue(any(item.value == "Data source" for item in app.subheader))
            panel = next(item for item in app.expander if item.label == "Handling count by time range")
            self.assertFalse(panel.proto.expanded)
            app.button(key="ubikais_workload_calculate").click().run()
            self.assertFalse(app.exception)
            self.assertEqual(app.session_state["ubikais_workload_result"]["departures"], 1)
            self.assertEqual(app.session_state["ubikais_workload_result"]["arrivals"], 1)
            elements = list(app)
            workload_index = next(index for index, item in enumerate(elements) if getattr(item, "key", None) == "ubikais_workload_calculate")
            comparison_index = next(index for index, item in enumerate(elements) if item.type == "expander" and item.label == "Flight schedule comparison")
            self.assertLess(workload_index, comparison_index)
            fetch.reset_mock()
            with patch("streamlit.file_uploader", side_effect=lambda label, **kwargs: upload if kwargs["key"] == "excel_upload_dep" else None):
                app.radio(key="schedule_input_mode").set_value("엑셀").run()
                app.button(key="excel_workload_calculate").click().run()
                self.assertFalse(app.exception)
                fetch.assert_not_called()
                # Template STD is 09:30 but handling begins at 08:40: it counts.
                self.assertEqual(app.session_state["excel_workload_result"]["departures"], 1)
                self.assertEqual(app.session_state["excel_workload_result"]["details"].iloc[0]["조업 시작"], "2026-12-02 08:40")
                elements = list(app)
                download_index = next(index for index, item in enumerate(elements) if item.type == "download_button" and item.proto.label == "PDF 다운로드")
                workload_index = next(index for index, item in enumerate(elements) if getattr(item, "key", None) == "excel_workload_calculate")
                self.assertLess(download_index, workload_index)


if __name__ == "__main__":
    unittest.main()
