"""Display-only airline conversion without changing operational identifiers."""
import io
import re
import unittest
from datetime import date

import pandas as pd

from airline_codes import ICAO_TO_IATA, flight_label
from flight_timeline import (
    TimelineConfig, arrivals_from_ubikais, build_timeline_figure,
    departures_from_ubikais, label_for,
)


class AirlineLabelTests(unittest.TestCase):
    def test_supported_flights_preserve_number_and_suffix(self):
        for original, expected in {
            "JJA1035": "7C1035", "ESR001F": "ZE001F", "TTW103": "IT103",
            "AXM103": "AK103", "CDC103": "GJ103", "RLH103": "DR103",
            "CSC103": "3U103", "HKE103": "UO103", "CQH103": "9C103",
            "TWB103": "TW103", "APJ103": "MM103", "KAL103": "KE103",
            "AAR103": "OZ103", "ABL103": "BX103", "ASV103": "RS103",
            "PTA103": "WE103", "EOK103": "RF103", "jja001a": "7C001a",
            "FDX001F": "FX001F", "JST1035": "JQ1035", "TZP001": "ZG001",
            "AJX103": "NQ103", "CKS103": "K4103", "DHK103": "D0103",
            "GGC103": "GG103", "HLF103": "I9103", "ICV103": "C8103",
            "LAO103": "QV103", "LHA103": "GI103", "MAA103": "M7103",
            "MFX103": "C6103", "MGL103": "OM103", "MPH103": "MP103",
            "QNT103": "HH103", "SPQ103": "9G103", "SWM103": "ZA103",
            "TUA103": "T5103",
        }.items():
            with self.subTest(original=original):
                self.assertEqual(flight_label(original), expected)

    def test_unknown_already_iata_and_nonstandard_values_stay_unchanged(self):
        for value in ("7C1035", "ZE103F", "IT103", "ZZZ103", "XESR103",
                      "JJA", "JJA-103", " JJA103 ", "note ESR103", "", None, pd.NA):
            with self.subTest(value=str(value)):
                self.assertEqual(flight_label(value), str(value))

    def test_reference_has_valid_code_shapes(self):
        for icao, iata in ICAO_TO_IATA.items():
            self.assertIsNotNone(re.fullmatch(r"[A-Z]{3}", icao))
            self.assertIsNotNone(re.fullmatch(r"[A-Z0-9]{2}", iata))

    def test_other_label_fields_and_hidden_flight(self):
        flags = dict(show_des_org=True, show_reg=True, show_spot=True)
        self.assertEqual(label_for("JJA1035", "RKSI", "HL1234", "101",
                                   show_flt=True, **flags), "7C1035 / ICN / HL1234 / #101")
        self.assertEqual(label_for("JJA1035", "RKSI", "HL1234", "101",
                                   show_flt=False, **flags), "ICN / HL1234 / #101")

    def test_chart_and_exports_keep_original_records(self):
        day = date(2026, 10, 29)
        for actual_dates in (False, True):
            with self.subTest(actual_dates=actual_dates):
                dep = departures_from_ubikais([{
                    "fpId": "JJA1035F", "schTime": "0900", "flightPk": "dep-key",
                }])
                arr = arrivals_from_ubikais([{
                    "fpId": "ESR001", "sta": "1000", "flightPk": "arr-key",
                }])
                for frame, key, clock in ((dep, "dep-team", "09:00"), (arr, "arr-team", "10:00")):
                    frame["TEAM_KEY"] = key
                    frame["TEAM"] = "Memo"
                    frame["SCHEDULED_AT"] = pd.Timestamp(f"{day} {clock}")
                original_dep, original_arr = dep.copy(deep=True), arr.copy(deep=True)
                fig, summary = build_timeline_figure(dep, arr, TimelineConfig(
                    day, service_start_hour=0, use_actual_schedule_dates=actual_dates,
                ))
                try:
                    labels = [text.get_text() for axis in fig.axes for text in axis.texts]
                    self.assertIn("7C1035F", labels)
                    self.assertIn("ZE001", labels)
                    for direction, original, expected in (
                        ("dep", original_dep, "7C1035F"), ("arr", original_arr, "ZE001"),
                    ):
                        plotted = summary[f"{direction}_records"]
                        self.assertEqual(plotted.iloc[0]["Label"], expected)
                        for column in ("FLT", "FLIGHT_PK", "TEAM_KEY", "TEAM"):
                            self.assertEqual(plotted.iloc[0][column], original.iloc[0][column])
                        self.assertEqual(summary[f"total_{direction}"], 1)
                    self.assertEqual(summary["dep_records"].iloc[0]["end"] - summary["dep_records"].iloc[0]["start"], pd.Timedelta(minutes=30))
                    for fmt, signature in (("png", b"\x89PNG"), ("pdf", b"%PDF")):
                        buffer = io.BytesIO()
                        fig.savefig(buffer, format=fmt)
                        self.assertTrue(buffer.getvalue().startswith(signature))
                    pd.testing.assert_frame_equal(dep, original_dep)
                    pd.testing.assert_frame_equal(arr, original_arr)
                finally:
                    fig.clear()


if __name__ == "__main__":
    unittest.main()
