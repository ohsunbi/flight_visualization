"""Isolated Streamlit screen for manual schedules; no API/assignment dependencies."""
from __future__ import annotations

import io
from datetime import timedelta

import streamlit as st
import pandas as pd

from flight_excel import read_schedule, schedule_columns, service_dates, template_bytes, timeline_frame
from flight_timeline import MATPLOTLIB_RENDER_LOCK, TimelineConfig, build_timeline_figure


@st.cache_data(show_spinner=False, max_entries=32)
def _read_upload(data: bytes, direction: str):
    return read_schedule(data, direction)


def render_excel_mode() -> None:
    st.title("엑셀 항공편 스케줄")
    st.caption("한 기준 공항의 출발·도착 파일을 입력하세요. 한쪽 파일만 있어도 됩니다. UBIKAIS 조회 및 조 배정은 사용하지 않습니다.")
    st.caption("첫 번째 시트를 읽습니다. 날짜 / 항공편명 / STD(출발) 또는 STA(도착)는 필수이며 출발지·도착지는 선택입니다. 공항은 IATA 3자리, 시간은 해당 공항 현지시간으로 입력하세요.")
    st.caption("날짜: Excel 날짜 또는 YYYY-MM-DD · 시간: Excel 시간, HH:MM 또는 HHMM. 양식의 예시 행은 실제 자료로 교체해 주세요.")

    st.sidebar.header("엑셀 차트 설정")
    start_hour = st.sidebar.number_input("서비스 데이 시작 시각", 0, 23, value=0, step=1, key="excel_service_start_hour")
    interval = st.sidebar.selectbox("중첩 계산 간격(분)", [10, 20, 30], index=2, key="excel_interval")
    show_flt = st.sidebar.checkbox("FLT", value=True, key="excel_show_flt")
    show_route = st.sidebar.checkbox("DES/ORG", value=False, key="excel_show_route")
    st.sidebar.caption("출발은 STD, 도착은 STA를 사용합니다. 날짜는 실제 운항 날짜로 유지하며 서비스 데이 범위로 묶습니다.")
    st.sidebar.subheader("작업시간(분)")
    dep_before = st.sidebar.number_input("출발 STD 이전", 0, 240, value=50, step=5, key="excel_dep_before")
    dep_after = st.sidebar.number_input("출발 STD 이후", 0, 240, value=10, step=5, key="excel_dep_after")
    arr_before = st.sidebar.number_input("도착 STA 이전", 0, 240, value=20, step=5, key="excel_arr_before")
    arr_after = st.sidebar.number_input("도착 STA 이후", 0, 240, value=30, step=5, key="excel_arr_after")

    frames = {}
    has_errors = False
    for direction, column in zip(("dep", "arr"), st.columns(2)):
        label = "출발" if direction == "dep" else "도착"
        with column:
            st.subheader(f"{label} 스케줄")
            st.download_button(f"{label} 양식 다운로드", template_bytes(direction), file_name=f"{direction}_schedule_template.xlsx", mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", key=f"excel_template_{direction}")
            upload = st.file_uploader(f"{label} 엑셀 파일", type=["xlsx"], key=f"excel_upload_{direction}")
            if upload is None:
                continue
            try:
                frame, errors, warnings = _read_upload(upload.getvalue(), direction)
                for message in errors:
                    st.error(f"{upload.name}: {message}")
                for message in warnings:
                    st.warning(f"{upload.name}: {message}")
                has_errors = has_errors or bool(errors)
                frames[direction] = frame
                st.caption(f"{upload.name} · {len(frame)}편")
            except Exception as exc:
                st.error(f"{upload.name}: 엑셀을 읽을 수 없습니다. {exc}")
                has_errors = True
    if has_errors:
        st.info("입력 오류를 수정한 파일을 다시 업로드해 주세요. 오류가 있는 동안 차트는 생성하지 않습니다.")
        return
    dates = sorted({day for frame in frames.values() for day in service_dates(frame, start_hour)})
    if not dates:
        st.info("유효한 항공편이 있는 엑셀 파일을 업로드해 주세요.")
        return
    # Widget options change when files/start hour change. Never retain an invalid day.
    if st.session_state.get("excel_display_date") not in dates:
        st.session_state["excel_display_date"] = dates[0]
    selected_date = st.selectbox("표시할 서비스 날짜", dates, format_func=lambda day: day.isoformat(), key="excel_display_date")
    start = f"{selected_date:%Y-%m-%d} {start_hour:02d}:00"
    end = f"{selected_date + timedelta(days=1):%Y-%m-%d} {start_hour:02d}:00"
    st.caption(f"서비스 데이: {start} 이상 ~ {end} 미만 · 업로드된 자료만 표시합니다. 인접 날짜 자료가 파일에 없으면 해당 구간의 항공편은 표시되지 않습니다.")

    plot_frames = {}
    for direction in ("dep", "arr"):
        frame = frames.get(direction)
        if frame is None:
            # An empty input still needs the same schema as a parsed upload.
            frame = pd.DataFrame(columns=schedule_columns(direction) + ["SCHEDULED_AT"])
        plot_frames[direction] = timeline_frame(frame, direction, selected_date, start_hour)
    config = TimelineConfig(
        base_date=selected_date, service_start_hour=int(start_hour), interval_min=interval,
        dep_before=dep_before, dep_after=dep_after, arr_before=arr_before, arr_after=arr_after,
        show_flt=show_flt, show_des_org=show_route, use_actual_schedule_dates=True,
    )
    try:
        fig, summary = build_timeline_figure(plot_frames["dep"], plot_frames["arr"], config)
    except ValueError as exc:
        st.warning(f"차트를 생성할 수 없습니다: {exc}")
        return
    first, second = st.columns(2)
    first.metric("Departure", summary["total_dep"])
    second.metric("Arrival", summary["total_arr"])
    with MATPLOTLIB_RENDER_LOCK:
        try:
            png, pdf = io.BytesIO(), io.BytesIO()
            fig.savefig(png, format="png", dpi=400, bbox_inches="tight")
            fig.savefig(pdf, format="pdf", bbox_inches="tight")
            st.pyplot(fig, width="content")
        finally:
            fig.clear()
    stem = f"excel_{selected_date:%Y-%m-%d}_D{summary['total_dep']}_A{summary['total_arr']}"
    png_col, pdf_col = st.columns(2)
    png_col.download_button("PNG 다운로드", png.getvalue(), file_name=f"{stem}.png", mime="image/png", key="excel_download_png")
    pdf_col.download_button("PDF 다운로드", pdf.getvalue(), file_name=f"{stem}.pdf", mime="application/pdf", key="excel_download_pdf")
    with st.expander("선택한 서비스 데이 입력 자료"):
        for direction, label in (("dep", "출발"), ("arr", "도착")):
            frame = plot_frames[direction]
            st.subheader(label)
            preview = frame[["SCHEDULED_AT", "FLT", "STD" if direction == "dep" else "STA", "ORG", "DES"]].copy()
            preview["SCHEDULED_AT"] = pd.to_datetime(preview["SCHEDULED_AT"]).dt.strftime("%Y-%m-%d")
            preview.columns = schedule_columns(direction)
            st.dataframe(preview, hide_index=True, width="stretch")
