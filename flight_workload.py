"""Count plotted handling records that overlap a requested time range."""
from __future__ import annotations

from datetime import date, datetime, time, timedelta

import pandas as pd


def query_window(
    display_date: date, start: time, end: time, day_start_hour: int,
) -> tuple[datetime, datetime]:
    """Map clock times onto the displayed day without changing flight dates.

    A start before the day's cutoff belongs to the next calendar day. An end
    earlier than the start clock time belongs to the following calendar day.
    The UI displays these actual dates, including ranges past the displayed day.
    """
    if start == end:
        raise ValueError("시작 시각과 종료 시각을 다르게 입력해 주세요.")
    window_start = datetime.combine(display_date, start)
    if start < time(day_start_hour):
        window_start += timedelta(days=1)
    window_end = datetime.combine(window_start.date(), end)
    if end < start:
        window_end += timedelta(days=1)
    return window_start, window_end


def overlapping_records(
    records: pd.DataFrame, window_start: datetime, window_end: datetime,
) -> pd.DataFrame:
    """One plotted row is one operation; repeated flight names are not merged."""
    if window_end <= window_start:
        raise ValueError("종료 시각은 시작 시각보다 뒤여야 합니다.")
    if records.empty:
        return records.copy()
    starts = pd.to_datetime(records["start"])
    ends = pd.to_datetime(records["end"])
    # Exclude boundary-only contact and zero-duration handling bars.
    return records.loc[(starts < window_end) & (ends > window_start) & (starts < ends)].copy()
