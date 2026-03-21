from __future__ import annotations

import io
from dataclasses import replace
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

try:
    from ubikais_client import fetch_records_for_airlines
except ImportError:
    def fetch_records_for_airlines(
        direction,
        query,
        airlines,
        *,
        cache_dir="cache",
        refresh=False,
        cookie_header=None,
    ):
        normalized_airlines = []
        for airline in airlines:
            airline_code = str(airline).strip().upper()
            if airline_code and airline_code not in normalized_airlines:
                normalized_airlines.append(airline_code)

        if not normalized_airlines:
            raise ValueError("At least one airline code is required.")

        merged_records = []
        fetched_at_values = []

        for airline_code in normalized_airlines:
            airline_query = replace(query, airline=airline_code)
            payload = fetch_records(
                direction,
                airline_query,
                cache_dir=cache_dir,
                refresh=refresh,
                cookie_header=cookie_header,
            )
            if payload.get("fetched_at"):
                fetched_at_values.append(int(payload["fetched_at"]))
            for record in payload.get("records") or []:
                merged_records.append({**record, "airlineCode": airline_code})

        return {
            "status": "success",
            "direction": direction,
            "query": {
                "flight_date": query.date_text,
                "airlines": normalized_airlines,
                "departure_airport": query.departure_airport,
                "arrival_airport": query.arrival_airport,
                "flight_number": query.flight_number,
                "limit": query.limit,
            },
            "fetched_at": max(fetched_at_values) if fetched_at_values else None,
            "total": len(merged_records),
            "records": merged_records,
        }


st.set_page_config(page_title="Flight Handling Schedule", layout="wide")


if "base_date" not in st.session_state:
    st.session_state.base_date = date.today()
if "selected_airlines" not in st.session_state:
    st.session_state.selected_airlines = ["ESR"]


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


def _normalize_airlines() -> None:
    normalized = []
    for airline in st.session_state.get("selected_airlines", []):
        airline_code = str(airline).strip().upper()
        if airline_code and airline_code not in normalized:
            normalized.append(airline_code)
    st.session_state.selected_airlines = normalized


st.sidebar.header("Ubikais Query")

default_airlines = ["ESR"]
airline_options = sorted({*default_airlines, *st.session_state.selected_airlines})

date_col1, date_col2, date_col3 = st.sidebar.columns([1, 4, 1])
with date_col1:
    st.button("<", key="btn_prev_day", on_click=_prev_day)
with date_col2:
    st.date_input(
        "Flight date",
        key="base_date",
        label_visibility="collapsed",
    )
with date_col3:
    st.button(">", key="btn_next_day", on_click=_next_day)

base_date = st.session_state.base_date
if isinstance(base_date, datetime):
    base_date = base_date.date()

selected_airlines = st.sidebar.multiselect(
    "Airlines",
    options=airline_options,
    accept_new_options=True,
    key="selected_airlines",
    on_change=_normalize_airlines,
    help="Choose one or more airline codes. You can also type a new code and press Enter.",
)
selected_airlines = st.session_state.selected_airlines
departure_airport = st.sidebar.text_input("Departure airport", value="RKSI").strip().upper()
arrival_airport = st.sidebar.text_input("Arrival airport", value="RKSI").strip().upper()
type_filter_slot = st.sidebar.empty()
refresh_button_slot = st.sidebar.empty()
refresh_data = refresh_button_slot.button("Refresh ubikais data")

st.sidebar.markdown("---")
st.sidebar.subheader("Labels on bars")
show_flt = st.sidebar.checkbox("Show FLT", value=True)
show_reg = st.sidebar.checkbox("Show REG", value=False)
show_spot = st.sidebar.checkbox("Show SPOT", value=False)

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

st.title(f"Flight Handling Schedule ({base_date.strftime('%Y-%m-%d')})")
st.caption("Data source: UBIKAIS departure/arrival JSON endpoints")

if not selected_airlines:
    st.warning("Choose at least one airline code.")
    st.stop()

query = UbikaisQuery(
    flight_date=base_date,
    airline=selected_airlines[0],
    departure_airport=departure_airport or "RKSI",
    arrival_airport=arrival_airport or "RKSI",
)

with st.spinner("Loading flight data from ubikais..."):
    try:
        dep_payload = fetch_records_for_airlines("dep", query, selected_airlines, refresh=refresh_data)
        arr_payload = fetch_records_for_airlines("arr", query, selected_airlines, refresh=refresh_data)
    except Exception as exc:
        st.error(f"Ubikais data load failed: {exc}")
        st.stop()

dep_df = departures_from_ubikais(dep_payload["records"])
arr_df = arrivals_from_ubikais(arr_payload["records"])

available_types = sorted(
    {
        str(value).strip()
        for value in pd.concat([dep_df.get("TYP", pd.Series(dtype=str)), arr_df.get("TYP", pd.Series(dtype=str))])
        if pd.notna(value) and str(value).strip()
    }
)
selected_types = type_filter_slot.multiselect(
    "Aircraft type",
    options=available_types,
    default=available_types,
    help="Choose which aircraft types to include in the chart.",
)

if selected_types:
    dep_df = dep_df[dep_df["TYP"].astype(str).isin(selected_types)].reset_index(drop=True)
    arr_df = arr_df[arr_df["TYP"].astype(str).isin(selected_types)].reset_index(drop=True)
else:
    dep_df = dep_df.iloc[0:0].copy()
    arr_df = arr_df.iloc[0:0].copy()

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
    show_spot=show_spot,
)

try:
    fig, summary = build_timeline_figure(dep_df, arr_df, config)
except ValueError as exc:
    st.warning(str(exc))
    st.stop()

content_main, content_spacer = st.columns([7, 2])

with content_main:
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

    airline_tag = selected_airlines[0] if len(selected_airlines) == 1 else f"{selected_airlines[0]}_plus{len(selected_airlines) - 1}"
    chart_name = (
        f"{base_date.strftime('%Y-%m-%d')}_{airline_tag}_D{summary['total_dep']}_A{summary['total_arr']}.png"
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
            f"Query: airlines `{', '.join(selected_airlines)}`, dep `{query.departure_airport}`, "
            f"arr `{query.arrival_airport}`, typ `{', '.join(selected_types) if selected_types else 'None'}`"
        )

    st.pyplot(fig, use_container_width=False)

with st.expander("Raw data preview"):
    preview_col1, preview_col2 = st.columns(2)
    with preview_col1:
        st.subheader("Departures")
        st.dataframe(dep_df)
    with preview_col2:
        st.subheader("Arrivals")
        st.dataframe(arr_df)
