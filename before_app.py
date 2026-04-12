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
DEFAULT_LABEL_FLAGS = {
    "show_flt": True,
    "show_des_org": False,
    "show_reg": False,
    "show_spot": False,
}
DEFAULT_TIMELINE_VALUES = {
    "service_start_hour": 0,
    "interval_min": 30,
    "dep_before": 50,
    "dep_after": 10,
    "arr_before": 20,
    "arr_after": 30,
}
LABEL_QUERY_KEYS = (
    ("flt", "show_flt"),
    ("desorg", "show_des_org"),
    ("reg", "show_reg"),
    ("spot", "show_spot"),
)
AIRLINE_OPTIONS = [
    ("ESR", "이스타항공"),
    ("TWB", "트리니티항공"),
    ("APJ", "피치항공"),
    ("PTA", "파라타항공"),
    ("MMA", "미얀마국제항공"),
    ("KZR", "에어아스타나"),
    ("CRK", "홍콩항공"),
]
AIRLINE_LABELS = {code: f"{code} {name}" for code, name in AIRLINE_OPTIONS}
AIRLINE_SHORT_LABELS = {
    "ESR": "ESR 이스타",
    "TWB": "TWB 티웨이",
    "APJ": "APJ 피치",
    "PTA": "PTA 파라타",
    "MMA": "MMA 미얀마",
    "KZR": "KZR 아스타나",
    "CRK": "CRK 홍콩",
}
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
        background: var(--secondary-background-color);
        border: 1px solid rgba(128, 128, 128, 0.22);
        border-radius: 14px;
        padding: 0.9rem 1rem 0.85rem;
        color: var(--text-color);
    }
    .summary-card-label {
        font-size: 0.9rem;
        color: inherit;
        opacity: 0.72;
        margin-bottom: 0.35rem;
    }
    .summary-card-value {
        font-size: 2rem;
        line-height: 1;
        font-weight: 700;
        color: inherit;
    }
    .last-fetched-block {
        margin-top: 0.35rem;
        margin-bottom: 0.55rem;
        color: var(--text-color);
    }
    .last-fetched-label {
        font-size: 0.8rem;
        font-weight: 600;
        letter-spacing: 0.02em;
        text-transform: uppercase;
        color: inherit;
        opacity: 0.68;
        margin-right: 0.4rem;
    }
    .last-fetched-value {
        font-size: 1rem;
        font-weight: 600;
        color: inherit;
    }
    div.st-key-airline_filter_mobile {
        display: none;
    }
    div.st-key-mobile_date_nav {
        display: none;
    }
    div.st-key-mobile_action_set {
        display: none;
    }
    @media (max-width: 768px) {
        div[data-testid="stMainBlockContainer"] {
            padding-top: 1.25rem;
        }
        div.st-key-main_panel {
            max-width: 100%;
        }
        div.st-key-airline_filter_desktop {
            display: none;
        }
        div.st-key-airline_filter_mobile {
            display: block;
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
        div.st-key-mobile_action_set {
            display: block;
        }
        div.st-key-mobile_action_set button {
            min-height: 2.6rem;
            padding: 0.35rem 0.45rem;
            font-size: 0.95rem;
        }
        div.st-key-mobile_action_set > div + div {
            margin-top: 0.45rem;
        }
        div.st-key-button_row div[data-testid="stHorizontalBlock"] {
            display: none;
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
if "_applied_url_signature" not in st.session_state:
    st.session_state["_applied_url_signature"] = None
if "_applied_type_url_signature" not in st.session_state:
    st.session_state["_applied_type_url_signature"] = None
if "_url_excluded_types" not in st.session_state:
    st.session_state["_url_excluded_types"] = []
for state_key, default_value in DEFAULT_LABEL_FLAGS.items():
    if state_key not in st.session_state:
        st.session_state[state_key] = default_value
for state_key, default_value in DEFAULT_TIMELINE_VALUES.items():
    if state_key not in st.session_state:
        st.session_state[state_key] = default_value


def _normalize_csv_values(value: Optional[str], *, upper: bool = False) -> list[str]:
    if value is None:
        return []

    normalized_values = []
    for part in str(value).split(","):
        item = part.strip()
        if not item:
            continue
        item = item.upper() if upper else item
        if item not in normalized_values:
            normalized_values.append(item)
    return normalized_values


def _coerce_int_param(
    value: Optional[str],
    *,
    default: int,
    minimum: Optional[int] = None,
    maximum: Optional[int] = None,
    allowed: Optional[list[int]] = None,
) -> int:
    if value is None or str(value).strip() == "":
        return default

    try:
        parsed = int(str(value).strip())
    except ValueError:
        return default

    if allowed is not None and parsed not in allowed:
        return default
    if minimum is not None and parsed < minimum:
        return default
    if maximum is not None and parsed > maximum:
        return default
    return parsed


def _url_signature(params: dict[str, str]) -> tuple[tuple[str, str], ...]:
    return tuple(sorted((str(key), str(value)) for key, value in params.items()))


def _read_url_state(params: dict[str, str]) -> dict:
    airlines = _normalize_csv_values(params.get("airlines"), upper=True)
    exclude_types = _normalize_csv_values(params.get("exclude_types"))

    label_flags = dict(DEFAULT_LABEL_FLAGS)
    if "labels" in params:
        label_flags = {state_key: False for _, state_key in LABEL_QUERY_KEYS}
        raw_labels = str(params.get("labels", "")).strip().lower()
        if raw_labels != "none":
            selected_label_keys = {label.lower() for label in _normalize_csv_values(raw_labels)}
            for query_key, state_key in LABEL_QUERY_KEYS:
                label_flags[state_key] = query_key in selected_label_keys

    return {
        "airlines": airlines,
        "exclude_types": exclude_types,
        "labels": label_flags,
        "service_start_hour": _coerce_int_param(
            params.get("service_start"),
            default=DEFAULT_TIMELINE_VALUES["service_start_hour"],
            minimum=0,
            maximum=23,
        ),
        "interval_min": _coerce_int_param(
            params.get("interval"),
            default=DEFAULT_TIMELINE_VALUES["interval_min"],
            allowed=[10, 20, 30],
        ),
        "dep_before": _coerce_int_param(
            params.get("dep_before"),
            default=DEFAULT_TIMELINE_VALUES["dep_before"],
            minimum=0,
            maximum=240,
        ),
        "dep_after": _coerce_int_param(
            params.get("dep_after"),
            default=DEFAULT_TIMELINE_VALUES["dep_after"],
            minimum=0,
            maximum=240,
        ),
        "arr_before": _coerce_int_param(
            params.get("arr_before"),
            default=DEFAULT_TIMELINE_VALUES["arr_before"],
            minimum=0,
            maximum=240,
        ),
        "arr_after": _coerce_int_param(
            params.get("arr_after"),
            default=DEFAULT_TIMELINE_VALUES["arr_after"],
            minimum=0,
            maximum=240,
        ),
    }


def _apply_url_state(params: dict[str, str]) -> None:
    url_state = _read_url_state(params)

    url_airlines = url_state["airlines"] or ["ESR"]
    airline_preferences = st.session_state.airline_preferences
    custom_airline_codes = list(st.session_state.custom_airline_codes)

    for airline_code in url_airlines:
        if airline_code not in DEFAULT_AIRLINE_CODES and airline_code not in custom_airline_codes:
            custom_airline_codes.append(airline_code)
    st.session_state.custom_airline_codes = custom_airline_codes

    all_airline_codes = list(dict.fromkeys([*DEFAULT_AIRLINE_CODES, *custom_airline_codes, *url_airlines]))
    for airline_code in all_airline_codes:
        airline_preferences[airline_code] = airline_code in url_airlines
        for variant in ("desktop", "mobile"):
            st.session_state[_airline_widget_key(airline_code, variant)] = airline_preferences[airline_code]
    st.session_state.airline_preferences = airline_preferences

    for state_key, enabled in url_state["labels"].items():
        st.session_state[state_key] = enabled

    for state_key in DEFAULT_TIMELINE_VALUES:
        st.session_state[state_key] = url_state[state_key]

    st.session_state["_url_excluded_types"] = url_state["exclude_types"]


def _build_url_params(
    *,
    selected_airlines: list[str],
    type_preferences: dict[str, bool],
    show_flt: bool,
    show_des_org: bool,
    show_reg: bool,
    show_spot: bool,
    service_start_hour: int,
    interval_min: int,
    dep_before: int,
    dep_after: int,
    arr_before: int,
    arr_after: int,
) -> dict[str, str]:
    params: dict[str, str] = {}

    if selected_airlines != ["ESR"]:
        params["airlines"] = ",".join(selected_airlines)

    excluded_types = sorted(
        aircraft_type
        for aircraft_type, enabled in type_preferences.items()
        if not bool(enabled)
    )
    if excluded_types:
        params["exclude_types"] = ",".join(excluded_types)

    current_labels = {
        "show_flt": bool(show_flt),
        "show_des_org": bool(show_des_org),
        "show_reg": bool(show_reg),
        "show_spot": bool(show_spot),
    }
    if current_labels != DEFAULT_LABEL_FLAGS:
        selected_label_keys = [query_key for query_key, state_key in LABEL_QUERY_KEYS if current_labels[state_key]]
        params["labels"] = ",".join(selected_label_keys) if selected_label_keys else "none"

    if int(service_start_hour) != DEFAULT_TIMELINE_VALUES["service_start_hour"]:
        params["service_start"] = str(int(service_start_hour))
    if int(interval_min) != DEFAULT_TIMELINE_VALUES["interval_min"]:
        params["interval"] = str(int(interval_min))
    if int(dep_before) != DEFAULT_TIMELINE_VALUES["dep_before"]:
        params["dep_before"] = str(int(dep_before))
    if int(dep_after) != DEFAULT_TIMELINE_VALUES["dep_after"]:
        params["dep_after"] = str(int(dep_after))
    if int(arr_before) != DEFAULT_TIMELINE_VALUES["arr_before"]:
        params["arr_before"] = str(int(arr_before))
    if int(arr_after) != DEFAULT_TIMELINE_VALUES["arr_after"]:
        params["arr_after"] = str(int(arr_after))

    return params


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


def _airline_widget_key(airline_code: str, variant: str = "desktop") -> str:
    return f"airline_enabled::{variant}::{airline_code}"


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


def _airline_checkbox_label(airline_code: str, airline_name: str, *, short: bool) -> str:
    if short:
        return AIRLINE_SHORT_LABELS.get(airline_code, airline_code)
    return f"{airline_code} {airline_name}".strip()


def _apply_airline_selection(airline_codes: list[str], variant: str) -> None:
    airline_preferences = st.session_state.airline_preferences
    for airline_code in airline_codes:
        state_key = _airline_widget_key(airline_code, variant)
        airline_preferences[airline_code] = bool(st.session_state.get(state_key, False))
    st.session_state.airline_preferences = airline_preferences
    for airline_code in airline_codes:
        for other_variant in ("desktop", "mobile"):
            st.session_state[_airline_widget_key(airline_code, other_variant)] = airline_preferences[airline_code]


def _set_airline_draft(airline_codes: list[str], enabled: bool, variant: str) -> None:
    for airline_code in airline_codes:
        st.session_state[_airline_widget_key(airline_code, variant)] = enabled


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
    st.session_state[_airline_widget_key(airline_code, "desktop")] = True
    st.session_state[_airline_widget_key(airline_code, "mobile")] = True


def _render_airline_filter_form(
    airline_options: list[tuple[str, str]],
    airline_codes: list[str],
    *,
    variant: str,
    short_labels: bool,
) -> None:
    with st.form(f"airline_filter_form_{variant}", border=False, enter_to_submit=False):
        st.caption("Click Apply to apply changes.")

        for airline_code, airline_name in airline_options:
            label = _airline_checkbox_label(airline_code, airline_name, short=short_labels)
            st.checkbox(label, key=_airline_widget_key(airline_code, variant))

        airline_action_col1, airline_action_col2 = st.columns(2, gap="small")
        with airline_action_col1:
            st.form_submit_button(
                "Select all",
                key=f"airline_select_all_{variant}",
                on_click=_set_airline_draft,
                args=(airline_codes, True, variant),
                width="stretch",
            )
        with airline_action_col2:
            st.form_submit_button(
                "Clear",
                key=f"airline_clear_all_{variant}",
                on_click=_set_airline_draft,
                args=(airline_codes, False, variant),
                width="stretch",
            )

        st.form_submit_button(
            "Apply",
            key=f"airline_apply_{variant}",
            on_click=_apply_airline_selection,
            args=(airline_codes, variant),
            type="primary",
            width="stretch",
        )


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


current_url_params = st.query_params.to_dict()
current_url_signature = _url_signature(current_url_params)
if st.session_state["_applied_url_signature"] != current_url_signature:
    _apply_url_state(current_url_params)
    st.session_state["_applied_url_signature"] = current_url_signature

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

    for variant in ("desktop", "mobile"):
        draft_key = _airline_widget_key(airline_code, variant)
        if draft_key not in st.session_state:
            st.session_state[draft_key] = airline_preferences[airline_code]

selected_airlines = [airline_code for airline_code in airline_codes if airline_preferences.get(airline_code, False)]
st.sidebar.subheader("Airlines")

with st.sidebar.expander("Filter airlines", expanded=False):
    st.caption("Airline 3 Code")
    with st.form("airline_add_form", border=False, enter_to_submit=False):
        add_airline_col1, add_airline_col2 = st.columns([2, 1], gap="small")
        with add_airline_col1:
            st.text_input("Airline 3 Code", key="custom_airline_input", label_visibility="collapsed")
        with add_airline_col2:
            st.form_submit_button("Add", on_click=_add_custom_airline, width="stretch")

    with st.container(key="airline_filter_desktop"):
        _render_airline_filter_form(
            airline_options,
            airline_codes,
            variant="desktop",
            short_labels=False,
        )

    with st.container(key="airline_filter_mobile"):
        _render_airline_filter_form(
            airline_options,
            airline_codes,
            variant="mobile",
            short_labels=True,
        )

st.sidebar.markdown(
    f"Selected: <span style='color:#ff6b5a; font-weight:600;'>{_airline_summary(selected_airlines)}</span>",
    unsafe_allow_html=True,
)
type_filter_slot = st.sidebar.empty()

st.sidebar.markdown("---")
st.sidebar.subheader("Labels on bars")
show_flt = st.sidebar.checkbox("Show FLT", key="show_flt")
show_des_org = st.sidebar.checkbox("Show DES/ORG", key="show_des_org")
show_reg = st.sidebar.checkbox("Show REG", key="show_reg")
show_spot = st.sidebar.checkbox("Show SPOT", key="show_spot")

st.sidebar.header("Timeline Settings")
service_start_hour = st.sidebar.number_input(
    "Service day starts at (hour)",
    min_value=0,
    max_value=23,
    step=1,
    key="service_start_hour",
)
interval_min = st.sidebar.selectbox("Overlap interval (min)", options=[10, 20, 30], key="interval_min")

st.sidebar.subheader("Operation windows (minutes)")
dep_before = st.sidebar.number_input("Departure window start (before ATD)", 0, 240, step=5, key="dep_before")
dep_after = st.sidebar.number_input("Departure window end (after ATD)", 0, 240, step=5, key="dep_after")
arr_before = st.sidebar.number_input("Arrival window start (before ATA)", 0, 240, step=5, key="arr_before")
arr_after = st.sidebar.number_input("Arrival window end (after ATA)", 0, 240, step=5, key="arr_after")

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
refresh_data = bool(st.session_state.get("_force_refresh", False))
should_refresh = refresh_data
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
        excluded_types = set(st.session_state.get("_url_excluded_types", []))
        if st.session_state.get("_applied_type_url_signature") != current_url_signature:
            for aircraft_type in available_types:
                type_preferences[aircraft_type] = aircraft_type not in excluded_types
                st.session_state[_aircraft_type_widget_key(aircraft_type)] = type_preferences[aircraft_type]
            st.session_state["_applied_type_url_signature"] = current_url_signature

        for aircraft_type in available_types:
            if aircraft_type not in type_preferences:
                type_preferences[aircraft_type] = aircraft_type not in excluded_types

            draft_key = _aircraft_type_widget_key(aircraft_type)
            if draft_key not in st.session_state:
                st.session_state[draft_key] = type_preferences[aircraft_type]

        selected_types = [aircraft_type for aircraft_type in available_types if type_preferences.get(aircraft_type, True)]

    st.subheader("Aircraft type")

    if available_types:
        apply_aircraft_type = False
        with st.expander("Filter types", expanded=False):
            with st.form("aircraft_type_form", border=False, enter_to_submit=False):
                st.caption("Click Apply to apply changes.")

                with st.container(key="aircraft_type_list"):
                    for aircraft_type in available_types:
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

                apply_aircraft_type = st.form_submit_button(
                    "Apply",
                    key="aircraft_type_apply",
                    type="primary",
                    width="stretch",
                )

        if apply_aircraft_type:
            _apply_aircraft_type_selection(available_types)
            type_preferences = st.session_state.aircraft_type_preferences
            selected_types = [aircraft_type for aircraft_type in available_types if type_preferences.get(aircraft_type, True)]

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

desired_url_params = _build_url_params(
    selected_airlines=selected_airlines,
    type_preferences=type_preferences,
    show_flt=show_flt,
    show_des_org=show_des_org,
    show_reg=show_reg,
    show_spot=show_spot,
    service_start_hour=int(service_start_hour),
    interval_min=int(interval_min),
    dep_before=int(dep_before),
    dep_after=int(dep_after),
    arr_before=int(arr_before),
    arr_after=int(arr_after),
)
desired_url_signature = _url_signature(desired_url_params)
if desired_url_signature != current_url_signature:
    st.query_params.from_dict(desired_url_params)
    st.session_state["_applied_url_signature"] = desired_url_signature

config = TimelineConfig(
    base_date=base_date,
    service_start_hour=int(service_start_hour),
    interval_min=int(interval_min),
    dep_before=int(dep_before),
    dep_after=int(dep_after),
    arr_before=int(arr_before),
    arr_after=int(arr_after),
    show_flt=show_flt,
    show_des_org=show_des_org,
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
        with st.container(key="mobile_action_set"):
            st.button("Next day", key="btn_next_day_mobile", on_click=_next_day, width="stretch")
            st.button("Previous day", key="btn_prev_day_mobile", on_click=_prev_day, width="stretch")
            st.button("Refresh", key="refresh_main_button_mobile", width="stretch", on_click=_request_refresh)
            st.download_button(
                label="Download PNG",
                data=buffer,
                file_name=chart_name,
                mime="image/png",
                key="download_png_mobile",
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
