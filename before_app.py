from __future__ import annotations

import io
from dataclasses import replace
from datetime import date, datetime, timedelta, timezone
from typing import Optional

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

KST = timezone(timedelta(hours=9))
AIRLINE_OPTIONS = [
    ("ESR", "이스타항공"),
    ("TWB", "티웨이항공"),
    ("APJ", "피치항공"),
    ("PTA", "파라타항공"),
    ("MMA", "미얀마국제항공"),
    ("KZR", "에어아스타나"),
    ("CRK", "홍콩항공"),
]
AIRLINE_LABELS = {code: f"{code} {name}" for code, name in AIRLINE_OPTIONS}
DEFAULT_AIRLINE_CODES = [code for code, _ in AIRLINE_OPTIONS]

st.markdown(
    """
    <style>
    div.st-key-custom_airline_input {
        margin-bottom: -0.35rem;
    }
    div[data-testid="stMainBlockContainer"] {
        padding-top: 2rem;
    }
    div.st-key-main_panel {
        max-width: 1240px;
    }
    .summary-cards {
        display: flex;
        flex-wrap: wrap;
        gap: 0.75rem;
        margin-bottom: 1rem;
    }
    .summary-card {
        flex: 1 1 280px;
        background: rgba(255, 255, 255, 0.04);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 14px;
        padding: 0.9rem 1rem 0.85rem;
    }
    .summary-card-label {
        font-size: 0.9rem;
        color: rgba(250, 250, 250, 0.72);
        margin-bottom: 0.35rem;
    }
    .summary-card-value {
        font-size: 2rem;
        line-height: 1;
        font-weight: 700;
        color: #f3f4f8;
    }
    .last-fetched-block {
        margin-top: 0.35rem;
        margin-bottom: 0.55rem;
    }
    .last-fetched-label {
        font-size: 0.8rem;
        font-weight: 600;
        letter-spacing: 0.02em;
        text-transform: uppercase;
        color: rgba(250, 250, 250, 0.62);
        margin-right: 0.4rem;
    }
    .last-fetched-value {
        font-size: 1rem;
        font-weight: 600;
        color: #f3f4f8;
    }
    div.st-key-mobile_date_nav {
        display: none;
    }
    @media (max-width: 768px) {
        div[data-testid="stMainBlockContainer"] {
            padding-top: 1.25rem;
        }
        div.st-key-main_panel {
            max-width: 100%;
        }
        .summary-card {
            flex: 1 1 calc(50% - 0.375rem);
            min-width: 0;
            padding: 0.8rem 0.85rem 0.75rem;
        }
        .summary-card-value {
            font-size: 1.75rem;
        }
        div.st-key-mobile_date_nav {
            display: block;
        }
        div.st-key-button_row div[data-testid="stHorizontalBlock"] {
            row-gap: 0.65rem;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)


if "base_date" not in st.session_state:
    st.session_state.base_date = date.today()
if "airline_preferences" not in st.session_state:
    st.session_state.airline_preferences = {code: code == "ESR" for code, _ in AIRLINE_OPTIONS}
if "custom_airline_codes" not in st.session_state:
    st.session_state.custom_airline_codes = []
if "aircraft_type_preferences" not in st.session_state:
    st.session_state.aircraft_type_preferences = {}
if "_force_refresh" not in st.session_state:
    st.session_state["_force_refresh"] = False


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


def _request_refresh() -> None:
    st.session_state["_force_refresh"] = True


def _airline_widget_key(airline_code: str) -> str:
    return f"airline_enabled::{airline_code}"


def _normalize_airline_code(value: str) -> str:
    return "".join(ch for ch in str(value).strip().upper() if ch.isalnum())


def _get_airline_options() -> list[tuple[str, str]]:
    options = list(AIRLINE_OPTIONS)
    for airline_code in st.session_state.custom_airline_codes:
        if airline_code not in DEFAULT_AIRLINE_CODES:
            options.append((airline_code, ""))
    return options


def _airline_summary(selected_codes: list[str], max_visible: int = 3) -> str:
    if not selected_codes:
        return "none"

    preview = ", ".join(selected_codes[:max_visible])
    if len(selected_codes) > max_visible:
        preview = f"{preview}, +{len(selected_codes) - max_visible} more"
    return preview


def _apply_airline_selection(airline_codes: list[str]) -> None:
    airline_preferences = st.session_state.airline_preferences
    for airline_code in airline_codes:
        state_key = _airline_widget_key(airline_code)
        airline_preferences[airline_code] = bool(st.session_state.get(state_key, False))
    st.session_state.airline_preferences = airline_preferences


def _set_airline_draft(airline_codes: list[str], enabled: bool) -> None:
    for airline_code in airline_codes:
        st.session_state[_airline_widget_key(airline_code)] = enabled


def _add_custom_airline() -> None:
    airline_code = _normalize_airline_code(st.session_state.get("custom_airline_input", ""))
    st.session_state.custom_airline_input = ""
    if not airline_code:
        return

    custom_airline_codes = list(st.session_state.custom_airline_codes)
    if airline_code not in DEFAULT_AIRLINE_CODES and airline_code not in custom_airline_codes:
        custom_airline_codes.append(airline_code)
        st.session_state.custom_airline_codes = custom_airline_codes

    if airline_code not in st.session_state.airline_preferences:
        st.session_state.airline_preferences[airline_code] = False
    st.session_state[_airline_widget_key(airline_code)] = True


def _aircraft_type_widget_key(aircraft_type: str) -> str:
    return f"aircraft_type_enabled::{aircraft_type}"


def _aircraft_type_summary(selected_types: list[str], max_visible: int = 4) -> str:
    if not selected_types:
        return "none"

    preview = ", ".join(selected_types[:max_visible])
    if len(selected_types) > max_visible:
        preview = f"{preview}, +{len(selected_types) - max_visible} more"
    return preview


def _apply_aircraft_type_selection(aircraft_types: list[str]) -> None:
    type_preferences = st.session_state.aircraft_type_preferences
    for aircraft_type in aircraft_types:
        state_key = _aircraft_type_widget_key(aircraft_type)
        type_preferences[aircraft_type] = bool(st.session_state.get(state_key, True))
    st.session_state.aircraft_type_preferences = type_preferences


def _set_aircraft_type_draft(aircraft_types: list[str], enabled: bool) -> None:
    for aircraft_type in aircraft_types:
        st.session_state[_aircraft_type_widget_key(aircraft_type)] = enabled


def _normalize_hhmm(value) -> Optional[str]:
    if pd.isna(value):
        return None

    digits = "".join(ch for ch in str(value).strip() if ch.isdigit())
    if len(digits) == 3:
        digits = f"0{digits}"
    if len(digits) != 4:
        return None

    try:
        hour = int(digits[:2])
        minute = int(digits[2:])
    except ValueError:
        return None

    if not (0 <= hour <= 23 and 0 <= minute <= 59):
        return None
    return digits


def _pick_service_day_time(record: dict, direction: str) -> Optional[str]:
    keys = ("atd", "etd", "schTime") if direction == "dep" else ("ata", "eta", "sta")
    for key in keys:
        hhmm = _normalize_hhmm(record.get(key))
        if hhmm is not None:
            return hhmm
    return None


def _filter_service_day_records(
    records: list[dict],
    *,
    direction: str,
    service_start_hour: int,
    include_early_window: bool,
) -> list[dict]:
    service_start_minutes = int(service_start_hour) * 60
    filtered_records = []

    for record in records:
        hhmm = _pick_service_day_time(record, direction)
        if hhmm is None:
            continue

        minutes = int(hhmm[:2]) * 60 + int(hhmm[2:])
        is_early_window = minutes < service_start_minutes

        if include_early_window == is_early_window:
            filtered_records.append(record)

    return filtered_records


def _merge_service_day_payload(
    *,
    direction: str,
    base_payload: dict,
    next_payload: Optional[dict],
    service_start_hour: int,
) -> dict:
    base_records = _filter_service_day_records(
        base_payload.get("records") or [],
        direction=direction,
        service_start_hour=service_start_hour,
        include_early_window=False,
    )

    next_records: list[dict] = []
    if next_payload is not None and service_start_hour > 0:
        next_records = _filter_service_day_records(
            next_payload.get("records") or [],
            direction=direction,
            service_start_hour=service_start_hour,
            include_early_window=True,
        )

    fetched_at_candidates = [base_payload.get("fetched_at")]
    if next_payload is not None:
        fetched_at_candidates.append(next_payload.get("fetched_at"))
    fetched_at_values = [int(value) for value in fetched_at_candidates if value]

    return {
        "status": "success",
        "direction": direction,
        "query": {
            **(base_payload.get("query") or {}),
            "service_day_start_hour": service_start_hour,
            "service_day_date": (base_payload.get("query") or {}).get("flight_date"),
        },
        "fetched_at": max(fetched_at_values) if fetched_at_values else None,
        "total": len(base_records) + len(next_records),
        "records": [*base_records, *next_records],
    }


st.sidebar.date_input("Date", key="base_date", label_visibility="collapsed")
date_nav_col1, date_nav_col2 = st.sidebar.columns(2, gap="small")
with date_nav_col1:
    st.button("◀ Prev", key="btn_prev_day", on_click=_prev_day, width="stretch")
with date_nav_col2:
    st.button("Next ▶", key="btn_next_day", on_click=_next_day, width="stretch")

base_date = st.session_state.base_date
if isinstance(base_date, datetime):
    base_date = base_date.date()

airline_preferences = st.session_state.airline_preferences
airline_options = _get_airline_options()
airline_codes = [code for code, _ in airline_options]
for airline_code in airline_codes:
    if airline_code not in airline_preferences:
        airline_preferences[airline_code] = False

    draft_key = _airline_widget_key(airline_code)
    if draft_key not in st.session_state:
        st.session_state[draft_key] = airline_preferences[airline_code]

selected_airlines = [airline_code for airline_code in airline_codes if airline_preferences.get(airline_code, False)]
st.sidebar.subheader("Airlines")

with st.sidebar.popover("Filter airlines", width="stretch"):
    st.caption("Add airline code")
    with st.form("airline_add_form", border=False, enter_to_submit=False):
        add_airline_col1, add_airline_col2 = st.columns([3, 1], gap="small")
        with add_airline_col1:
            st.text_input("Add airline code", key="custom_airline_input", label_visibility="collapsed")
        with add_airline_col2:
            st.form_submit_button("Add", on_click=_add_custom_airline, width="stretch")

    st.divider()

    with st.form("airline_filter_form", border=False, enter_to_submit=False):
        st.caption("Changes are applied only when you click Apply.")

        for airline_code, airline_name in airline_options:
            label = f"{airline_code} {airline_name}".strip()
            st.checkbox(label, key=_airline_widget_key(airline_code))

        airline_action_col1, airline_action_col2 = st.columns(2, gap="small")
        with airline_action_col1:
            st.form_submit_button(
                "Select all",
                key="airline_select_all",
                on_click=_set_airline_draft,
                args=(airline_codes, True),
                width="stretch",
            )
        with airline_action_col2:
            st.form_submit_button(
                "Clear",
                key="airline_clear_all",
                on_click=_set_airline_draft,
                args=(airline_codes, False),
                width="stretch",
            )

        st.form_submit_button(
            "Apply",
            key="airline_apply",
            on_click=_apply_airline_selection,
            args=(airline_codes,),
            type="primary",
            width="stretch",
        )

st.sidebar.markdown(
    f"Selected: <span style='color:#ff6b5a; font-weight:600;'>{_airline_summary(selected_airlines)}</span>",
    unsafe_allow_html=True,
)
type_filter_slot = st.sidebar.empty()

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
    value=0,
    step=1,
)
interval_min = st.sidebar.selectbox("Overlap interval (min)", options=[10, 20, 30], index=2)

st.sidebar.subheader("Operation windows (minutes)")
dep_before = st.sidebar.number_input("Departure window start (before ATD)", 0, 240, 50, 5)
dep_after = st.sidebar.number_input("Departure window end (after ATD)", 0, 240, 10, 5)
arr_before = st.sidebar.number_input("Arrival window start (before ATA)", 0, 240, 20, 5)
arr_after = st.sidebar.number_input("Arrival window end (after ATA)", 0, 240, 30, 5)

st.sidebar.markdown("---")
departure_airport = st.sidebar.text_input("Departure airport", value="RKSI").strip().upper()
arrival_airport = st.sidebar.text_input("Arrival airport", value="RKSI").strip().upper()

st.title(f"Flight Schedule ({base_date.strftime('%Y-%m-%d')})")

if not selected_airlines:
    st.warning("Choose at least one airline code.")
    st.stop()

query = UbikaisQuery(
    flight_date=base_date,
    airline=selected_airlines[0],
    departure_airport=departure_airport or "RKSI",
    arrival_airport=arrival_airport or "RKSI",
)
query_signature = (
    query.flight_date.isoformat(),
    tuple(sorted(selected_airlines)),
    query.departure_airport,
    query.arrival_airport,
)
previous_query_signature = st.session_state.get("_last_query_signature")
refresh_data = bool(st.session_state.get("_force_refresh", False))
should_refresh = refresh_data or previous_query_signature != query_signature
st.session_state["_force_refresh"] = False

with st.spinner("Loading flight data from ubikais..."):
    try:
        next_day_query = replace(query, flight_date=base_date + timedelta(days=1))

        dep_payload_base = fetch_records_for_airlines("dep", query, selected_airlines, refresh=should_refresh)
        arr_payload_base = fetch_records_for_airlines("arr", query, selected_airlines, refresh=should_refresh)

        dep_payload_next = None
        arr_payload_next = None
        if int(service_start_hour) > 0:
            dep_payload_next = fetch_records_for_airlines("dep", next_day_query, selected_airlines, refresh=should_refresh)
            arr_payload_next = fetch_records_for_airlines("arr", next_day_query, selected_airlines, refresh=should_refresh)

        dep_payload = _merge_service_day_payload(
            direction="dep",
            base_payload=dep_payload_base,
            next_payload=dep_payload_next,
            service_start_hour=int(service_start_hour),
        )
        arr_payload = _merge_service_day_payload(
            direction="arr",
            base_payload=arr_payload_base,
            next_payload=arr_payload_next,
            service_start_hour=int(service_start_hour),
        )
    except Exception as exc:
        st.error(f"Ubikais data load failed: {exc}")
        st.stop()

st.session_state["_last_query_signature"] = query_signature

dep_df = departures_from_ubikais(dep_payload["records"])
arr_df = arrivals_from_ubikais(arr_payload["records"])

available_types = sorted(
    {
        str(value).strip()
        for value in pd.concat([dep_df.get("TYP", pd.Series(dtype=str)), arr_df.get("TYP", pd.Series(dtype=str))])
        if pd.notna(value) and str(value).strip()
    }
)

with type_filter_slot.container():
    type_preferences = st.session_state.aircraft_type_preferences

    selected_types = []
    if available_types:
        for aircraft_type in available_types:
            if aircraft_type not in type_preferences:
                type_preferences[aircraft_type] = True

            draft_key = _aircraft_type_widget_key(aircraft_type)
            if draft_key not in st.session_state:
                st.session_state[draft_key] = type_preferences[aircraft_type]

        selected_types = [aircraft_type for aircraft_type in available_types if type_preferences.get(aircraft_type, True)]

    st.subheader("Aircraft type")

    if available_types:
        with st.popover("Filter types", width="stretch"):
            with st.form("aircraft_type_form", border=False, enter_to_submit=False):
                st.caption("Changes are applied only when you click Apply.")

                split_index = (len(available_types) + 1) // 2
                left_types = available_types[:split_index]
                right_types = available_types[split_index:]
                type_col1, type_col2 = st.columns(2, gap="medium")

                for col, column_types in ((type_col1, left_types), (type_col2, right_types)):
                    with col:
                        for aircraft_type in column_types:
                            state_key = _aircraft_type_widget_key(aircraft_type)
                            st.checkbox(aircraft_type, key=state_key)

                action_col1, action_col2 = st.columns(2, gap="small")
                with action_col1:
                    st.form_submit_button(
                        "Select all",
                        key="aircraft_type_select_all",
                        on_click=_set_aircraft_type_draft,
                        args=(available_types, True),
                        width="stretch",
                    )
                with action_col2:
                    st.form_submit_button(
                        "Clear",
                        key="aircraft_type_clear_all",
                        on_click=_set_aircraft_type_draft,
                        args=(available_types, False),
                        width="stretch",
                    )

                st.form_submit_button(
                    "Apply",
                    key="aircraft_type_apply",
                    on_click=_apply_aircraft_type_selection,
                    args=(available_types,),
                    type="primary",
                    width="stretch",
                )

        st.markdown(
            f"Selected: <span style='color:#ff6b5a; font-weight:600;'>{_aircraft_type_summary(selected_types)}</span>",
            unsafe_allow_html=True,
        )
    else:
        st.caption("No aircraft types found for this query.")

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
    with st.container(key="main_panel"):
        st.markdown(
            f"""
            <div class="summary-cards">
                <div class="summary-card">
                    <div class="summary-card-label">Departure</div>
                    <div class="summary-card-value">{summary["total_dep"]}</div>
                </div>
                <div class="summary-card">
                    <div class="summary-card-label">Arrival</div>
                    <div class="summary-card-value">{summary["total_arr"]}</div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        fetched_at_values = [dep_payload.get("fetched_at"), arr_payload.get("fetched_at")]
        fetched_at_values = [value for value in fetched_at_values if value]
        if fetched_at_values:
            fetched_at = datetime.fromtimestamp(max(fetched_at_values), tz=timezone.utc).astimezone(KST)
            fetched_at_text = fetched_at.strftime("%Y-%m-%d %H:%M:%S KST")
        else:
            fetched_at_text = "-"

        airline_tag = selected_airlines[0] if len(selected_airlines) == 1 else f"{selected_airlines[0]}_plus{len(selected_airlines) - 1}"
        chart_name = (
            f"{base_date.strftime('%Y-%m-%d')}_{airline_tag}_D{summary['total_dep']}_A{summary['total_arr']}.png"
        )
        buffer = io.BytesIO()
        fig.savefig(buffer, format="png", dpi=200, bbox_inches="tight")
        buffer.seek(0)

        st.pyplot(fig, width="content")
        st.markdown(
            f"""
            <div class="last-fetched-block">
                <span class="last-fetched-label">Last fetched</span>
                <span class="last-fetched-value">{fetched_at_text}</span>
            </div>
            """,
            unsafe_allow_html=True,
        )
        with st.container(key="mobile_date_nav"):
            mobile_prev_col, mobile_next_col = st.columns(2, gap="small")
            with mobile_prev_col:
                st.button("◀ Prev", key="btn_prev_day_mobile", on_click=_prev_day, width="stretch")
            with mobile_next_col:
                st.button("Next ▶", key="btn_next_day_mobile", on_click=_next_day, width="stretch")
        with st.container(key="button_row"):
            refresh_col, download_col = st.columns(2, gap="small")
            with refresh_col:
                st.button("Refresh", key="refresh_main_button", width="stretch", on_click=_request_refresh)
            with download_col:
                st.download_button(
                    label="Download PNG",
                    data=buffer,
                    file_name=chart_name,
                    mime="image/png",
                    width="stretch",
                )
        service_day_end = base_date + timedelta(days=1) if int(service_start_hour) > 0 else base_date
        service_day_end_time = f"{int(service_start_hour):02d}:00" if int(service_start_hour) > 0 else "24:00"
        with st.expander("More details"):
            st.caption(
                f"Service day: {base_date.strftime('%Y-%m-%d')} {int(service_start_hour):02d}:00 "
                f"to {service_day_end.strftime('%Y-%m-%d')} {service_day_end_time}"
            )
            st.caption("Data source: UBIKAIS departure/arrival JSON endpoints")
            st.caption(
                f"Query: airlines {', '.join(selected_airlines)}, dep {query.departure_airport}, "
                f"arr {query.arrival_airport}, typ {', '.join(selected_types) if selected_types else 'None'}"
            )
        with st.expander("Raw data preview"):
            preview_col1, preview_col2 = st.columns(2)
            with preview_col1:
                st.subheader("Departures")
                st.dataframe(dep_df)
            with preview_col2:
                st.subheader("Arrivals")
                st.dataframe(arr_df)
