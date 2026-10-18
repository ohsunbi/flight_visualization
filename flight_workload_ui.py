"""Shared time-range workload panel for UBIKAIS and Excel charts."""
from __future__ import annotations

import hashlib
from datetime import date, time

import pandas as pd
import streamlit as st

from airport_codes import icao_to_iata
from flight_workload import overlapping_records, query_window


def _result_signature(summary: dict, context: tuple) -> str:
    digest = hashlib.sha256(repr(context).encode("utf-8"))
    for direction in ("dep", "arr"):
        frame = summary[f"{direction}_records"]
        columns = [column for column in ("FLT", "ORG", "DES", "start", "end", "marker") if column in frame]
        digest.update(direction.encode())
        digest.update(pd.util.hash_pandas_object(frame[columns].astype(str), index=False).values.tobytes())
    return digest.hexdigest()


def _details(departures: pd.DataFrame, arrivals: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for label, frame, route in (("출발", departures, "DES"), ("도착", arrivals, "ORG")):
        for _, row in frame.iterrows():
            value = row.get(route, "")
            rows.append({
                "방향": label,
                "항공편명": str(row["FLT"]),
                "출도착지": "" if pd.isna(value) else icao_to_iata(str(value)),
                "조업 시작": pd.Timestamp(row["start"]).strftime("%Y-%m-%d %H:%M"),
                "조업 종료": pd.Timestamp(row["end"]).strftime("%Y-%m-%d %H:%M"),
            })
    return pd.DataFrame(rows, columns=["방향", "항공편명", "출도착지", "조업 시작", "조업 종료"]).sort_values("조업 시작", kind="stable").reset_index(drop=True)


def render_workload_panel(
    *, summary: dict, display_date: date, day_start_hour: int, key_prefix: str,
    chart_context: str, language: str = "ko",
) -> None:
    title = "Handling count by time range" if language == "en" else "시간대별 조업 편수"
    with st.expander(title, expanded=False):
        _render_workload_contents(
            summary=summary, display_date=display_date, day_start_hour=day_start_hour,
            key_prefix=key_prefix, chart_context=chart_context, language=language,
        )


def _render_workload_contents(
    *, summary: dict, display_date: date, day_start_hour: int, key_prefix: str,
    chart_context: str, language: str,
) -> None:
    def text(korean: str, english: str) -> str:
        return english if language == "en" else korean

    st.caption(text(
        "현재 차트의 조업 중 입력 범위와 실제로 겹치는 시간이 있는 편을 셉니다. 시작·종료 경계에 닿기만 하는 조업은 제외합니다.",
        "Count handling operations on the current chart that overlap the selected range. Operations that only touch a boundary are excluded.",
    ))
    if day_start_hour > 0:
        st.caption(text(
            f"하루 시작 시각인 {day_start_hour:02d}:00보다 이른 시작 시각은 다음 날 새벽으로 해석합니다.",
            f"Start times before the service-day cutoff ({day_start_hour:02d}:00) refer to the next calendar day.",
        ))
    st.caption(text(
        "시·분을 선택한 뒤 계산 버튼을 눌러 적용하세요. 분은 10분 단위로 선택합니다.",
        "Select hours and minutes, then click Calculate to apply. Minutes are in 10-minute steps.",
    ))
    # Form controls are sent together on submission, avoiding chart reruns while
    # the user adjusts the four selections. Keep the previous counted range visible.
    with st.form(f"{key_prefix}_workload_form", clear_on_submit=False):
        start_hour_col, start_minute_col, end_hour_col, end_minute_col = st.columns(4, gap="small")
        start_hour = start_hour_col.selectbox(
            text("시작 시", "Start hour"), range(24), index=7,
            format_func=lambda value: f"{value:02d}", key=f"{key_prefix}_workload_start_hour",
        )
        start_minute = start_minute_col.selectbox(
            text("시작 분", "Start minute"), range(0, 60, 10),
            format_func=lambda value: f"{value:02d}", key=f"{key_prefix}_workload_start_minute",
        )
        end_hour = end_hour_col.selectbox(
            text("종료 시", "End hour"), range(24), index=9,
            format_func=lambda value: f"{value:02d}", key=f"{key_prefix}_workload_end_hour",
        )
        end_minute = end_minute_col.selectbox(
            text("종료 분", "End minute"), range(0, 60, 10),
            format_func=lambda value: f"{value:02d}", key=f"{key_prefix}_workload_end_minute",
        )
        submitted = st.form_submit_button(text("조업 편수 계산", "Calculate"), key=f"{key_prefix}_workload_calculate", width="stretch")
    start, end = time(start_hour, start_minute), time(end_hour, end_minute)
    result_key = f"{key_prefix}_workload_result"
    signature_key = f"{key_prefix}_workload_signature"
    signature = _result_signature(summary, (display_date, day_start_hour, chart_context, start, end, language))
    if st.session_state.get(signature_key) != signature:
        st.session_state[result_key] = None
        st.session_state[signature_key] = signature
    if submitted:
        try:
            if start == end:
                raise ValueError("same_time")
            window_start, window_end = query_window(display_date, start, end, day_start_hour)
            departures = overlapping_records(summary["dep_records"], window_start, window_end)
            arrivals = overlapping_records(summary["arr_records"], window_start, window_end)
            st.session_state[result_key] = {
                "start": window_start, "end": window_end,
                "departures": len(departures), "arrivals": len(arrivals),
                "details": _details(departures, arrivals),
            }
        except ValueError as exc:
            st.session_state[result_key] = None
            if str(exc) == "same_time":
                st.warning(text("시작 시각과 종료 시각을 다르게 입력해 주세요.", "Start and end times must be different."))
            else:
                st.warning(text(
                    "집계 시간 범위를 확인해 주세요.",
                    "Please check the selected time range.",
                ))
    result = st.session_state.get(result_key)
    if result is None:
        return
    st.caption(text(
        f"집계 범위: {result['start']:%Y-%m-%d %H:%M} 이상 ~ {result['end']:%Y-%m-%d %H:%M} 미만 · 종료 시각이 시작 시각보다 이르면 다음 날로 계산합니다.",
        f"Counted range: {result['start']:%Y-%m-%d %H:%M} (inclusive) to {result['end']:%Y-%m-%d %H:%M} (exclusive). An end time earlier than the start time means the next day.",
    ))
    departure_label = text("출발 조업", "Departure")
    arrival_label = text("도착 조업", "Arrival")
    unit = text("편", "")
    st.markdown(
        f"""
        <div class="summary-cards">
            <div class="summary-card">
                <div class="summary-card-label">{departure_label}</div>
                <div class="summary-card-value">{result['departures']}{unit}</div>
            </div>
            <div class="summary-card">
                <div class="summary-card-label">{arrival_label}</div>
                <div class="summary-card-value">{result['arrivals']}{unit}</div>
            </div>
        </div>
        """, unsafe_allow_html=True,
    )
    with st.expander(text("집계 항공편 세부사항", "Flight details")):
        if result["details"].empty:
            st.info(text("입력한 시간 범위와 겹치는 조업이 없습니다.", "No handling operations overlap this time range."))
        else:
            details = result["details"].copy()
            if language == "en":
                details = details.rename(columns={
                    "방향": "Direction", "항공편명": "Flight", "출도착지": "ORG/DES",
                    "조업 시작": "Handling start", "조업 종료": "Handling end",
                })
                details["Direction"] = details["Direction"].map({"출발": "Departure", "도착": "Arrival"})
            st.dataframe(details, hide_index=True, width="stretch")
