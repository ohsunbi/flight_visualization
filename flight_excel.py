"""Read manual schedules without changing their actual local calendar dates."""
from __future__ import annotations

import io
import math
import re
from datetime import date, datetime, time, timedelta

import pandas as pd


def schedule_columns(direction: str) -> list[str]:
    if direction not in {"dep", "arr"}:
        raise ValueError("Unknown schedule direction")
    return ["날짜", "항공편명", "STD" if direction == "dep" else "STA", "출발지", "도착지"]


def _text(value: object) -> str:
    return "" if pd.isna(value) else str(value).strip()


def _date(value: object) -> date:
    if pd.isna(value):
        raise ValueError("날짜가 비어 있습니다")
    if isinstance(value, (datetime, date)):
        return value.date() if isinstance(value, datetime) else value
    raw = _text(value)
    for fmt in ("%Y-%m-%d", "%Y/%m/%d", "%Y%m%d"):
        try:
            return datetime.strptime(raw, fmt).date()
        except ValueError:
            pass
    raise ValueError("날짜는 Excel 날짜 또는 YYYY-MM-DD 형식이어야 합니다")


def _time(value: object) -> time:
    if pd.isna(value):
        raise ValueError("시간이 비어 있습니다")
    if isinstance(value, (datetime, time)):
        result = value.time() if isinstance(value, datetime) else value
    elif isinstance(value, (int, float)) and not isinstance(value, bool):
        number = float(value)
        if not math.isfinite(number):
            raise ValueError("올바른 시간이 아닙니다")
        if 0 <= number < 1 and not number.is_integer():
            seconds = round(number * 86400)
            if seconds >= 86400:
                raise ValueError("24:00은 사용할 수 없습니다")
            result = (datetime.min + timedelta(seconds=seconds)).time()
        elif number.is_integer():
            return _time(f"{int(number):04d}")
        else:
            raise ValueError("시간은 HH:MM 또는 HHMM 형식이어야 합니다")
    else:
        raw = _text(value)
        if not re.fullmatch(r"\d{3,4}|\d{1,2}:\d{2}(:\d{2})?", raw):
            raise ValueError("시간은 HH:MM 또는 HHMM 형식이어야 합니다")
        try:
            if ":" not in raw:
                result = datetime.strptime(raw.zfill(4), "%H%M").time()
            else:
                parts = [int(part) for part in raw.split(":")]
                result = time(*parts)
        except ValueError as exc:
            raise ValueError("시간 범위는 00:00~23:59입니다") from exc
    if result.second or result.microsecond:
        raise ValueError("시간은 분 단위로 입력해 주세요")
    return result.replace(tzinfo=None)


def read_schedule(data: bytes, direction: str) -> tuple[pd.DataFrame, list[str], list[str]]:
    """Read the first sheet, returning rows, blocking errors and duplicate warnings.

    Invalid rows are reported; the UI blocks charting the entire upload until fixed.
    No upload is written to disk or merged with UBIKAIS/assignment data.
    """
    columns = schedule_columns(direction)
    time_column = columns[2]
    with pd.ExcelFile(io.BytesIO(data), engine="openpyxl") as workbook:
        sheet = workbook.sheet_names[0]
        frame = pd.read_excel(workbook, sheet_name=sheet, dtype=object)
    frame.columns = [str(column).strip() for column in frame.columns]
    missing = [column for column in columns[:3] if column not in frame.columns]
    if missing:
        return pd.DataFrame(columns=columns + ["SCHEDULED_AT"]), [f"시트 {sheet}: 필수 열 누락 — {', '.join(missing)}"], []
    if frame.columns.duplicated().any():
        return pd.DataFrame(columns=columns + ["SCHEDULED_AT"]), [f"시트 {sheet}: 중복된 열 이름이 있습니다"], []
    rows, errors, warnings = [], [], []
    seen: dict[tuple, int] = {}
    for position, (_, source) in enumerate(frame.iterrows(), start=2):
        if all(not _text(source.get(column, "")) for column in columns):
            continue
        try:
            flight_date = _date(source["날짜"])
            flight = _text(source["항공편명"]).upper()
            if not flight:
                raise ValueError("항공편명이 비어 있습니다")
            flight_time = _time(source[time_column])
            origin, destination = (_text(source.get(column, "")).upper() for column in columns[3:])
            for label, airport in (("출발지", origin), ("도착지", destination)):
                if airport and not re.fullmatch(r"[A-Z]{3}", airport):
                    raise ValueError(f"{label}는 ICN과 같은 IATA 영문 3자리여야 합니다")
            key = (flight_date, flight, flight_time, origin, destination)
            if key in seen:
                warnings.append(f"시트 {sheet}, {position}행: {seen[key]}행과 중복됩니다. 삭제하지 않고 모두 표시합니다.")
            else:
                seen[key] = position
            rows.append(dict(zip(columns, [flight_date, flight, flight_time.strftime("%H:%M"), origin, destination]), SCHEDULED_AT=datetime.combine(flight_date, flight_time)))
        except ValueError as exc:
            errors.append(f"시트 {sheet}, {position}행: {exc}")
    return pd.DataFrame(rows, columns=columns + ["SCHEDULED_AT"]), errors, warnings


def service_dates(frame: pd.DataFrame, start_hour: int) -> list[date]:
    shifted = pd.to_datetime(frame["SCHEDULED_AT"]) - pd.Timedelta(hours=start_hour)
    return sorted(set(shifted.dt.date))


def timeline_frame(frame: pd.DataFrame, direction: str, service_date: date, start_hour: int) -> pd.DataFrame:
    columns = schedule_columns(direction)
    start = pd.Timestamp(service_date) + pd.Timedelta(hours=start_hour)
    times = pd.to_datetime(frame["SCHEDULED_AT"])
    selected = frame.loc[(times >= start) & (times < start + pd.Timedelta(days=1))].reset_index(drop=True)
    result = pd.DataFrame({
        "FLT": selected["항공편명"], "ORG": selected["출발지"], "DES": selected["도착지"],
        columns[2]: selected[columns[2]], "SCHEDULED_AT": selected["SCHEDULED_AT"],
    })
    for column in ("FLIGHT_PK", "REG", "TYP", "SPOT", "BLOCK_OFF", "ATD", "ETD", "BLOCK_ON", "ATA", "ETA"):
        result[column] = ""
    return result


def template_bytes(direction: str) -> bytes:
    buffer = io.BytesIO()
    columns = schedule_columns(direction)
    example = [date(2026, 12, 2), "ZE101" if direction == "dep" else "ZE102", time(9, 30), "ICN" if direction == "dep" else "NRT", "NRT" if direction == "dep" else "ICN"]
    with pd.ExcelWriter(buffer, engine="openpyxl", date_format="YYYY-MM-DD") as writer:
        pd.DataFrame([example], columns=columns).to_excel(writer, index=False, sheet_name="Schedule")
        worksheet = writer.sheets["Schedule"]
        worksheet.freeze_panes = "A2"
        for column in ("A", "B", "C", "D", "E"):
            worksheet.column_dimensions[column].width = 18
        worksheet["A2"].number_format = "yyyy-mm-dd"
        worksheet["C2"].number_format = "hh:mm"
    return buffer.getvalue()
