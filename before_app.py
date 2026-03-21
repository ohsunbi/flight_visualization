from __future__ import annotations

import io
from datetime import date, datetime, timedelta

import pandas as pd
import streamlit as st

from flight_timeline import (
    TimelineConfig,
    arrivals_from_ubikais,
    build_timeline_figure,
    departures_from_ubikais,
)
from ubikais_client import UbikaisQuery, fetch_records


st.set_page_config(page_title="Flight Handling Schedule", layout="wide")


if "base_date" not in st.session_state:
    st.session_state.base_date = date.today()


def _normalize_base_date() -> None:
    current = st.session_state.get("base_date")
    if isinstance(current, datetime):
        st.session_state.base_date = current.date()


def _prev_day() -> None:
    _normalize_base_date()
    st.session_state.base_date = st.session_state.base_date - timedelta(days=1)


def _next_day() -> None:
    _normalize_base_date()
    st.session_state.base_date = st.session_state.base_date + timedelta(days=1)


st.sidebar.header("Ubikais Query")

date_col1, date_col2, date_col3 = st.sidebar.columns([1, 4, 1])
with date_col1:
    st.button("<", key="btn_prev_day", on_click=_prev_day)
with date_col2:
    st.date_input(
        "Flight date",
        value=st.session_state.base_date,
        key="base_date",
        label_visibility="collapsed",
    )
with date_col3:
    st.button(">", key="btn_next_day", on_click=_next_day)

base_date = st.session_state.base_date
if isinstance(base_date, datetime):
    base_date = base_date.date()

airline = st.sidebar.text_input("Airline", value="ESR").strip().upper()
departure_airport = st.sidebar.text_input("Departure airport", value="RKSI").strip().upper()
arrival_airport = st.sidebar.text_input("Arrival airport", value="RKSI").strip().upper()
refresh_data = st.sidebar.button("Refresh ubikais data")

st.sidebar.markdown("---")
st.sidebar.header("Timeline Settings")
service_start_hour = st.sidebar.number_input(
    "Service day starts at (hour)",
    min_value=0,
    max_value=23,
    value=2,
    step=1,
)
interval_min = st.sidebar.selectbox("Overlap interval (min)", options=[10, 20, 30], index=2)

st.sidebar.subheader("Operation windows (minutes)")
dep_before = st.sidebar.number_input("Departure window start (before ATD)", 0, 240, 50, 5)
dep_after = st.sidebar.number_input("Departure window end (after ATD)", 0, 240, 10, 5)
arr_before = st.sidebar.number_input("Arrival window start (before ATA)", 0, 240, 20, 5)
arr_after = st.sidebar.number_input("Arrival window end (after ATA)", 0, 240, 30, 5)

st.sidebar.subheader("Labels on bars")
show_flt = st.sidebar.checkbox("Show FLT", value=True)
show_reg = st.sidebar.checkbox("Show REG", value=False)
show_memo = st.sidebar.checkbox("Show MEMO", value=False)

st.title(f"Flight Handling Schedule ({base_date.strftime('%Y-%m-%d')})")
st.caption("Data source: UBIKAIS departure/arrival JSON endpoints")

query = UbikaisQuery(
    flight_date=base_date,
    airline=airline or "ESR",
    departure_airport=departure_airport or "RKSI",
    arrival_airport=arrival_airport or "RKSI",
)

with st.spinner("Loading flight data from ubikais..."):
    try:
        dep_payload = fetch_records("dep", query, refresh=refresh_data)
        arr_payload = fetch_records("arr", query, refresh=refresh_data)
    except Exception as exc:
        st.error(f"Ubikais data load failed: {exc}")
        st.stop()

dep_df = departures_from_ubikais(dep_payload["records"])
arr_df = arrivals_from_ubikais(arr_payload["records"])

config = TimelineConfig(
    base_date=base_date,
    service_start_hour=int(service_start_hour),
    interval_min=int(interval_min),
    dep_before=int(dep_before),
    dep_after=int(dep_after),
    arr_before=int(arr_before),
    arr_after=int(arr_after),
    show_flt=show_flt,
    show_reg=show_reg,
    show_memo=show_memo,
)

try:
    fig, summary = build_timeline_figure(dep_df, arr_df, config)
except ValueError as exc:
    st.warning(str(exc))
    st.stop()

status_col1, status_col2, status_col3 = st.columns(3)
status_col1.metric("Departure records", summary["total_dep"])
status_col2.metric("Arrival records", summary["total_arr"])

fetched_at_values = [dep_payload.get("fetched_at"), arr_payload.get("fetched_at")]
fetched_at_values = [value for value in fetched_at_values if value]
if fetched_at_values:
    fetched_at = datetime.fromtimestamp(max(fetched_at_values))
    status_col3.metric("Last fetched", fetched_at.strftime("%Y-%m-%d %H:%M:%S"))
else:
    status_col3.metric("Last fetched", "-")

chart_name = (
    f"{base_date.strftime('%Y-%m-%d')}_{airline or 'ALL'}_D{summary['total_dep']}_A{summary['total_arr']}.png"
)
buffer = io.BytesIO()
fig.savefig(buffer, format="png", dpi=200, bbox_inches="tight")
buffer.seek(0)

download_col, info_col = st.columns([1, 2])
with download_col:
    st.download_button(
        label="Download chart as PNG",
        data=buffer,
        file_name=chart_name,
        mime="image/png",
    )
with info_col:
    st.write(
        f"Query: airline `{query.airline}`, dep `{query.departure_airport}`, "
        f"arr `{query.arrival_airport}`"
    )

st.pyplot(fig, use_container_width=True)

with st.expander("Raw data preview"):
    preview_col1, preview_col2 = st.columns(2)
    with preview_col1:
        st.subheader("Departures")
        st.dataframe(pd.DataFrame(dep_payload["records"]))
    with preview_col2:
        st.subheader("Arrivals")
        st.dataframe(pd.DataFrame(arr_payload["records"]))
