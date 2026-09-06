"""Excel-backed flight team assignment helpers.

The workbook is intentionally treated as the user's source of truth.  The
currently selected service date is rendered from the data currently shown in
the app; other date sheets are copied from the uploaded workbook.
"""

from __future__ import annotations

import io
import re
from collections import defaultdict
from datetime import date, datetime
from typing import Any

import pandas as pd


EXPORT_COLUMNS = [
    "Direction",
    "연결편",
    "FLT",
    "Time",
    "ORG/DES",
    "Aircraft",
    "REG",
    "SPOT",
    "배정조",
    "작업유형",
    "_MATCH_KEY",
]
ASSIGNMENT_COLUMNS = {"Assignment", "TaskType"}


def normalize_text(value: Any) -> str:
    if value is None or pd.isna(value):
        return ""
    return " ".join(str(value).replace("\n", " ").split()).strip()


def normalize_direction(value: Any) -> str:
    text = normalize_text(value).upper()
    return "ARR" if text in {"ARR", "ARRIVAL", "A"} else "DEP"


def normalize_date(value: Any, fallback: date | None = None) -> date | None:
    if isinstance(value, datetime):
        return value.date()
    if isinstance(value, date):
        return value
    text = normalize_text(value)
    if text:
        for fmt in ("%Y-%m-%d", "%Y/%m/%d", "%Y%m%d", "%m/%d/%Y"):
            try:
                return datetime.strptime(text, fmt).date()
            except ValueError:
                pass
    return fallback


def parse_sheet_date(sheet_name: str) -> date | None:
    match = re.search(r"\d{4}[-_]\d{2}[-_]\d{2}|\d{8}", str(sheet_name))
    return normalize_date(match.group(0).replace("_", "-") if match else "")


def _first_column(frame: pd.DataFrame, names: tuple[str, ...]) -> str | None:
    normalized = {normalize_text(column).lower(): column for column in frame.columns}
    for name in names:
        if name.lower() in normalized:
            return normalized[name.lower()]
    return None


def _column(frame: pd.DataFrame, names: tuple[str, ...], default: str = "") -> pd.Series:
    column = _first_column(frame, names)
    if column is None:
        return pd.Series([default] * len(frame), index=frame.index, dtype=object)
    return frame[column].map(normalize_text)


def _sheet_to_assignments(frame: pd.DataFrame, sheet_date: date) -> list[dict[str, str]]:
    if frame is None or frame.empty:
        return []

    direction = _column(frame, ("Direction", "Type", "방향"))
    flt = _column(frame, ("FLT", "Flight", "Flight Number", "항공편"))
    assignment = _column(frame, ("Assignment", "Team", "Memo", "배정조", "담당 조"))
    task_type = _column(frame, ("TaskType", "Task Type", "작업유형", "작업 유형"))
    match_key = _column(frame, ("_MATCH_KEY", "MatchKey", "FlightKey"))
    row_numbers: defaultdict[tuple[str, str], int] = defaultdict(int)
    result: list[dict[str, str]] = []

    for index in frame.index:
        flight = flt.loc[index].strip().upper()
        if not flight:
            continue
        dir_value = normalize_direction(direction.loc[index])
        occurrence_key = (dir_value, flight)
        occurrence = row_numbers[occurrence_key]
        row_numbers[occurrence_key] += 1
        result.append(
            {
                "date": sheet_date.isoformat(),
                "direction": dir_value,
                "flt": flight,
                "assignment": assignment.loc[index],
                "task_type": task_type.loc[index],
                "match_key": match_key.loc[index],
                "occurrence": str(occurrence),
            }
        )
    return result


def read_assignment_workbook(uploaded_file: Any) -> dict[str, list[dict[str, str]]]:
    """Read all date-named sheets, retaining only assignment fields."""
    if uploaded_file is None:
        return {}
    sheets = pd.read_excel(uploaded_file, sheet_name=None, dtype=object)
    assignments: dict[str, list[dict[str, str]]] = {}
    for sheet_name, frame in sheets.items():
        sheet_date = parse_sheet_date(str(sheet_name))
        if sheet_date is None:
            continue
        assignments[sheet_date.isoformat()] = _sheet_to_assignments(frame, sheet_date)
    return assignments


def read_workbook_frames(uploaded_file: Any) -> dict[str, pd.DataFrame]:
    """Read date-named sheets while preserving their displayed columns."""
    if uploaded_file is None:
        return {}
    sheets = pd.read_excel(uploaded_file, sheet_name=None, dtype=object)
    frames: dict[str, pd.DataFrame] = {}
    for sheet_name, frame in sheets.items():
        sheet_date = parse_sheet_date(str(sheet_name))
        if sheet_date is not None:
            frames[sheet_date.isoformat()] = frame.copy()
    return frames


def _row_match_key(row: dict[str, Any], direction: str, occurrence: int) -> str:
    explicit = normalize_text(row.get("TEAM_KEY", ""))
    if explicit:
        return explicit
    flight_pk = normalize_text(row.get("FLIGHT_PK", ""))
    if flight_pk:
        return f"pk|{flight_pk}"
    flt = normalize_text(row.get("FLT", "")).upper()
    return f"{direction}|flt:{flt}|occ:{occurrence}"


def records_to_export_rows(
    *,
    dep_records: pd.DataFrame,
    arr_records: pd.DataFrame,
    flight_date: date,
    existing_assignments: list[dict[str, str]] | None = None,
    assignment_overrides: dict[str, str] | None = None,
) -> pd.DataFrame:
    """Create one row per visible flight and merge prior assignment fields."""
    assignment_rows = existing_assignments or []
    assignment_overrides = assignment_overrides or {}
    by_key: dict[str, list[dict[str, str]]] = defaultdict(list)
    by_flt: dict[tuple[str, str], list[dict[str, str]]] = defaultdict(list)
    for item in assignment_rows:
        if item.get("match_key"):
            by_key[item["match_key"]].append(item)
        by_flt[(item.get("direction", ""), item.get("flt", ""))].append(item)

    rows: list[dict[str, str]] = []
    occurrence_by_flight: defaultdict[tuple[str, str], int] = defaultdict(int)
    for direction, records in (("DEP", dep_records), ("ARR", arr_records)):
        if records is None or records.empty:
            continue
        for _, source in records.sort_values("marker", kind="stable").iterrows():
            flt = normalize_text(source.get("FLT", "")).upper()
            if not flt:
                continue
            occurrence_key = (direction, flt)
            occurrence = occurrence_by_flight[occurrence_key]
            occurrence_by_flight[occurrence_key] += 1
            match_key = _row_match_key(source.to_dict(), direction, occurrence)
            candidates = by_key.get(match_key) or by_flt.get(occurrence_key, [])
            prior = candidates[occurrence] if len(candidates) > occurrence else (candidates[0] if candidates else {})
            org_des = source.get("DES", "") if direction == "DEP" else source.get("ORG", "")
            prior_rows = candidates if candidates and any(
                normalize_text(item.get("task_type", "")) for item in candidates
            ) else [prior]
            for prior_row in prior_rows:
                override_team = normalize_text(assignment_overrides.get(match_key, ""))
                rows.append(
                    {
                        "Direction": direction,
                        "연결편": "",
                        "FLT": flt,
                        "Time": normalize_text(source.get("time_str", "")),
                        "ORG/DES": normalize_text(org_des),
                        "Aircraft": normalize_text(source.get("TYP", "")),
                        "REG": normalize_text(source.get("REG", "")),
                        "SPOT": normalize_text(source.get("SPOT", "")),
                        "배정조": override_team or normalize_text(prior_row.get("assignment", source.get("TEAM", ""))),
                        "작업유형": normalize_text(prior_row.get("task_type", "")),
                        "_MATCH_KEY": match_key,
                    }
                )

    return pd.DataFrame(rows, columns=EXPORT_COLUMNS)


def apply_connection_order(
    frame: pd.DataFrame,
    *,
    dep_records: pd.DataFrame,
    arr_records: pd.DataFrame,
    turnaround_pairs: list[tuple[int, int]],
) -> pd.DataFrame:
    """Interleave departures/arrivals by time and keep turn-arounds adjacent."""
    if frame.empty:
        return frame

    source_info: dict[str, tuple[pd.Timestamp, str]] = {}
    for direction, records in (("DEP", dep_records), ("ARR", arr_records)):
        if records is None or records.empty:
            continue
        for _, row in records.iterrows():
            key = normalize_text(row.get("TEAM_KEY", ""))
            marker = pd.to_datetime(row.get("marker"), errors="coerce")
            if key and pd.notna(marker):
                source_info[key] = (marker, direction)

    connection_by_key: dict[str, str] = {}
    connection_anchor: dict[str, pd.Timestamp] = {}
    connection_number = 0
    for arr_index, dep_index in turnaround_pairs:
        try:
            arr_key = normalize_text(arr_records.iloc[int(arr_index)].get("TEAM_KEY", ""))
            dep_key = normalize_text(dep_records.iloc[int(dep_index)].get("TEAM_KEY", ""))
        except (IndexError, TypeError):
            continue
        if not arr_key or not dep_key:
            continue
        connection_number += 1
        label = f"T/A-{connection_number:02d}"
        connection_by_key[arr_key] = label
        connection_by_key[dep_key] = label
        markers = [source_info[key][0] for key in (arr_key, dep_key) if key in source_info]
        if markers:
            connection_anchor[label] = min(markers)

    result = frame.copy()
    result["연결편"] = result["_MATCH_KEY"].map(connection_by_key).fillna("")
    result["_sort_time"] = result["_MATCH_KEY"].map(
        lambda key: source_info.get(normalize_text(key), (pd.Timestamp.max, ""))[0]
    )
    result["_group_anchor"] = result["연결편"].map(connection_anchor)
    result["_group_anchor"] = result["_group_anchor"].fillna(result["_sort_time"])
    result["_direction_order"] = result["Direction"].map({"ARR": 0, "DEP": 1}).fillna(2)
    result = result.sort_values(
        ["_group_anchor", "연결편", "_sort_time", "_direction_order", "FLT"],
        kind="stable",
    )
    return result.drop(columns=["_sort_time", "_group_anchor", "_direction_order"]).reset_index(drop=True)


def merge_assignment_rows(
    existing: list[dict[str, str]],
    uploaded: list[dict[str, str]],
) -> list[dict[str, str]]:
    """Replace a date's assignment fields with uploaded rows."""
    del existing
    return [
        {
            "date": item.get("date", ""),
            "direction": normalize_direction(item.get("direction", "")),
            "flt": normalize_text(item.get("flt", "")).upper(),
            "assignment": normalize_text(item.get("assignment", "")),
            "task_type": normalize_text(item.get("task_type", "")),
            "match_key": normalize_text(item.get("match_key", "")),
            "occurrence": normalize_text(item.get("occurrence", "0")),
        }
        for item in uploaded
        if normalize_text(item.get("flt", ""))
    ]


def workbook_bytes(
    *,
    date_frames: dict[str, pd.DataFrame],
) -> bytes:
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine="openpyxl") as writer:
        for sheet_date, frame in sorted(date_frames.items()):
            safe_frame = frame.copy()
            safe_frame.to_excel(writer, sheet_name=sheet_date[:31], index=False)
            worksheet = writer.sheets[sheet_date[:31]]
            if "_MATCH_KEY" in safe_frame.columns:
                match_column = list(safe_frame.columns).index("_MATCH_KEY") + 1
                worksheet.column_dimensions[chr(64 + match_column) if match_column <= 26 else "J"].hidden = True
            for column_cells in worksheet.columns:
                width = min(max(max(len(str(cell.value or "")) for cell in column_cells) + 2, 10), 28)
                worksheet.column_dimensions[column_cells[0].column_letter].width = width
    output.seek(0)
    return output.getvalue()
