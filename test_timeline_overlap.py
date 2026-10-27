"""Verify rendered concurrency numbers separately from range operation counts."""
import io
import unittest
from datetime import date, datetime

import pandas as pd

from flight_timeline import TimelineConfig, build_timeline_figure
from flight_workload import overlapping_records


DAY = date(2026, 10, 27)


def frame(direction, clock, count):
    return pd.DataFrame([
        {"FLT": f"TEST{index}", "SCHEDULED_AT": datetime.fromisoformat(f"{DAY}T{clock}"),
         "STD" if direction == "dep" else "STA": clock}
        for index in range(count)
    ], columns=["FLT", "SCHEDULED_AT", "STD" if direction == "dep" else "STA"])


class TimelineOverlapTests(unittest.TestCase):
    def test_rendered_total_uses_combined_concurrency(self):
        for arrival_time, dep_count, arr_count, expected_total in [
            ("09:00", 2, 2, 2),  # Arrivals start exactly when departures end.
            ("08:45", 2, 2, 4),  # Both directional peaks happen together.
            ("09:00", 2, 0, 2),
            ("09:00", 0, 2, 2),
        ]:
            with self.subTest(arrival_time=arrival_time, dep_count=dep_count, arr_count=arr_count):
                config = TimelineConfig(
                    DAY, service_start_hour=0, interval_min=30,
                    dep_before=0, dep_after=15, arr_before=0, arr_after=15,
                    use_actual_schedule_dates=True,
                )
                fig, summary = build_timeline_figure(
                    frame("dep", "08:45", dep_count), frame("arr", arrival_time, arr_count), config,
                )
                try:
                    at_nine = {
                        round(text.get_position()[1], 2): text.get_text()
                        for text in fig.axes[0].texts
                        if text.get_position()[0] == datetime(2026, 10, 27, 9)
                    }
                    self.assertEqual(at_nine[-0.06], str(expected_total))
                    if dep_count:
                        self.assertEqual(at_nine[-0.10], str(dep_count))
                    if arr_count:
                        self.assertEqual(at_nine[-0.14], str(arr_count))
                    start, end = datetime(2026, 10, 27, 8, 45), datetime(2026, 10, 27, 9, 15)
                    for direction, count in (("dep", dep_count), ("arr", arr_count)):
                        self.assertEqual(len(overlapping_records(summary[f"{direction}_records"], start, end)), count)
                    for fmt, signature in (("png", b"\x89PNG"), ("pdf", b"%PDF")):
                        output = io.BytesIO()
                        fig.savefig(output, format=fmt)
                        self.assertTrue(output.getvalue().startswith(signature))
                finally:
                    fig.clear()


if __name__ == "__main__":
    unittest.main()
