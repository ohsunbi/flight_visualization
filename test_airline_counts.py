"""Airline counts and filter behavior without UBIKAIS network calls."""
import unittest
from datetime import date
from unittest.mock import patch

from streamlit.testing.v1 import AppTest


DAY = date(2026, 10, 27)


def payload(direction, query, airlines, **kwargs):
    rows = []
    for code in airlines:
        times = {"ESR": ["0100", "0800"], "TWB": ["0900"]}.get(code, [])
        if query.departure_airport == "RKPC":
            times = times[:1]
        if query.flight_date > DAY:
            times = [clock for clock in times if clock < "0200"]
        for index, clock in enumerate(times):
            rows.append({
                "airlineCode": code, "fpId": f"{code}{index + 100}",
                "schTime": clock, "sta": clock,
                "acType": "B738" if index == 0 else "A320",
            })
    return {"records": rows, "fetched_at": 0}


class AirlineCountTests(unittest.TestCase):
    def app(self):
        app = AppTest.from_file("before_app.py", default_timeout=90)
        app.session_state["base_date"] = DAY
        app.query_params["airlines"] = "ESR,TWB,APJ"
        return app

    def check_counts(self, app, counts):
        self.assertFalse(app.exception)
        for variant in ("desktop", "mobile"):
            for code, count in counts.items():
                widget = app.checkbox(key=f"airline_enabled::{variant}::{code}")
                self.assertTrue(widget.label.endswith(f" ({count})"), widget.label)
            self.assertNotIn("(", app.checkbox(key=f"airline_enabled::{variant}::PTA").label)

    def test_counts_filters_and_apply(self):
        app = self.app()
        with patch("ubikais_client.fetch_records_for_airlines", side_effect=payload) as fetch:
            app.run()
            self.check_counts(app, {"ESR": 4, "TWB": 2, "APJ": 0})
            self.assertEqual(fetch.call_count, 2)
            fetch.reset_mock()
            app.checkbox(key="aircraft_type_enabled::A320").uncheck()
            app.button(key="aircraft_type_apply").click().run()
            self.check_counts(app, {"ESR": 4, "TWB": 2, "APJ": 0})
            fetch.assert_not_called()
            app.checkbox(key="airline_enabled::mobile::TWB").uncheck()
            app.button(key="airline_apply_mobile").click().run()
            self.check_counts(app, {"ESR": 4, "APJ": 0})
            self.assertNotIn("(", app.checkbox(key="airline_enabled::desktop::TWB").label)
            self.assertFalse(app.checkbox(key="airline_enabled::desktop::TWB").value)
            app.selectbox(key="airport").set_value("RKPC").run()
            self.check_counts(app, {"ESR": 2, "APJ": 0})
            app.button(key="airline_clear_all_desktop").click().run()
            app.button(key="airline_apply_desktop").click().run()
            self.assertFalse(app.exception)
            self.assertIn("Choose at least one airline", app.warning[0].value)
            self.assertTrue(app.checkbox(key="airline_enabled::desktop::ESR"))

    def test_service_day_and_fetch_error(self):
        app = self.app()
        app.query_params["service_start"] = "2"
        with patch("ubikais_client.fetch_records_for_airlines", side_effect=payload) as fetch:
            app.run()
            self.check_counts(app, {"ESR": 4, "TWB": 2, "APJ": 0})
            self.assertEqual(fetch.call_count, 4)
            app.date_input(key="base_date").set_value(date(2026, 10, 28)).run()
            self.check_counts(app, {"ESR": 2, "TWB": 0, "APJ": 0})
        with patch("ubikais_client.fetch_records_for_airlines", side_effect=RuntimeError("offline")):
            app.selectbox(key="airport").set_value("RKPC").run()
            self.assertFalse(app.exception)
            self.assertIn("offline", app.error[0].value)
            self.assertNotIn("(", app.checkbox(key="airline_enabled::desktop::ESR").label)


if __name__ == "__main__":
    unittest.main()
