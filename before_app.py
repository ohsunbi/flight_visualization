from __future__ import annotations

import io
import math
import statistics
from dataclasses import replace
from datetime import date, datetime, timedelta, timezone
from html import escape
from typing import Optional

import matplotlib.pyplot as plt
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
    "show_team": True,
    "show_turnaround": True,
}
DEFAULT_TIMELINE_VALUES = {
    "time_basis": "ground",
    "service_start_hour": 0,
    "interval_min": 30,
    "dep_before": 50,
    "dep_after": 10,
    "arr_before": 20,
    "arr_after": 30,
    "turnaround_limit_min": 120,
}
LABEL_QUERY_KEYS = (
    ("flt", "show_flt"),
    ("desorg", "show_des_org"),
    ("reg", "show_reg"),
    ("spot", "show_spot"),
    ("memo", "show_team"),
    ("turn", "show_turnaround"),
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
    .flight-lookup-calendar-wrap {
        overflow-x: auto;
        margin-top: 0.75rem;
    }
    .flight-lookup-calendar {
        display: grid;
        grid-template-columns: repeat(7, minmax(132px, 1fr));
        gap: 0.55rem;
        min-width: 980px;
    }
    .flight-lookup-head {
        text-align: center;
        font-size: 0.78rem;
        font-weight: 700;
        letter-spacing: 0.02em;
        text-transform: uppercase;
        color: var(--text-color);
        opacity: 0.82;
        padding: 0.55rem 0.45rem;
        background: var(--secondary-background-color);
        border: 1px solid rgba(128, 128, 128, 0.22);
        border-radius: 10px;
    }
    .flight-lookup-head.is-weekend {
        color: #ff6b5a;
    }
    .flight-lookup-cell {
        background: var(--secondary-background-color);
        border: 1px solid rgba(128, 128, 128, 0.22);
        border-radius: 12px;
        padding: 0.7rem 0.72rem;
        min-height: 108px;
        color: var(--text-color);
    }
    .flight-lookup-cell.is-empty {
        background: transparent;
        border-style: dashed;
        opacity: 0.35;
    }
    .flight-lookup-cell.is-noop {
        opacity: 0.72;
    }
    .flight-lookup-date {
        font-size: 0.82rem;
        font-weight: 700;
        margin-bottom: 0.45rem;
    }
    .flight-lookup-line {
        font-size: 0.84rem;
        line-height: 1.35;
        font-family: Consolas, "SFMono-Regular", Menlo, Monaco, monospace;
    }
    .flight-lookup-time {
        font-weight: 700;
    }
    .flight-lookup-status {
        font-size: 0.82rem;
        opacity: 0.76;
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
if "_main_fetch_signature" not in st.session_state:
    st.session_state["_main_fetch_signature"] = None
if "_main_dep_payload_base" not in st.session_state:
    st.session_state["_main_dep_payload_base"] = None
if "_main_arr_payload_base" not in st.session_state:
    st.session_state["_main_arr_payload_base"] = None
if "_main_dep_payload_next" not in st.session_state:
    st.session_state["_main_dep_payload_next"] = None
if "_main_arr_payload_next" not in st.session_state:
    st.session_state["_main_arr_payload_next"] = None
if "flight_lookup_code" not in st.session_state:
    st.session_state.flight_lookup_code = ""
if "flight_lookup_start_date" not in st.session_state:
    st.session_state.flight_lookup_start_date = st.session_state.base_date
if "flight_lookup_end_date" not in st.session_state:
    st.session_state.flight_lookup_end_date = st.session_state.base_date
if "flight_lookup_direction" not in st.session_state:
    st.session_state.flight_lookup_direction = None
if "flight_lookup_result" not in st.session_state:
    st.session_state.flight_lookup_result = None
if "team_assignments" not in st.session_state:
    st.session_state.team_assignments = {}
if "team_assignment_filter" not in st.session_state:
    st.session_state.team_assignment_filter = ""
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
        "time_basis": str(params.get("time_basis", DEFAULT_TIMELINE_VALUES["time_basis"])).strip().lower()
        if str(params.get("time_basis", DEFAULT_TIMELINE_VALUES["time_basis"])).strip().lower() in {"ground", "flight"}
        else DEFAULT_TIMELINE_VALUES["time_basis"],
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
        "turnaround_limit_min": _coerce_int_param(
            params.get("turn_limit"),
            default=DEFAULT_TIMELINE_VALUES["turnaround_limit_min"],
            minimum=1,
            maximum=1440,
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
    show_team: bool,
    show_turnaround: bool,
    time_basis: str,
    service_start_hour: int,
    interval_min: int,
    dep_before: int,
    dep_after: int,
    arr_before: int,
    arr_after: int,
    turnaround_limit_min: int,
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
        "show_team": bool(show_team),
        "show_turnaround": bool(show_turnaround),
    }
    if current_labels != DEFAULT_LABEL_FLAGS:
        selected_label_keys = [query_key for query_key, state_key in LABEL_QUERY_KEYS if current_labels[state_key]]
        params["labels"] = ",".join(selected_label_keys) if selected_label_keys else "none"

    normalized_time_basis = str(time_basis).strip().lower()
    if normalized_time_basis != DEFAULT_TIMELINE_VALUES["time_basis"]:
        params["time_basis"] = normalized_time_basis
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
    if int(turnaround_limit_min) != DEFAULT_TIMELINE_VALUES["turnaround_limit_min"]:
        params["turn_limit"] = str(int(turnaround_limit_min))

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


def _normalize_team_text(value: object) -> str:
    if value is None or pd.isna(value):
        return ""

    text = " ".join(str(value).replace("\n", " ").split()).strip()
    return text


def _normalize_team_key_part(value: object, *, upper: bool = True) -> str:
    if value is None or pd.isna(value):
        return ""

    text = " ".join(str(value).split()).strip()
    return text.upper() if upper else text


def _build_team_assignment_key(base_date: date, direction: str, row: object) -> str:
    flight_pk = _normalize_team_key_part(
        row.get("FLIGHT_PK", row.get("flightPk", "")),
        upper=False,
    )
    if flight_pk:
        return f"{base_date.isoformat()}|{direction}|pk|{flight_pk}"

    if str(direction).strip().lower() == "dep":
        leg_value = row.get("DES", row.get("apArr", ""))
        scheduled_value = row.get("STD", row.get("schTime", ""))
    else:
        leg_value = row.get("ORG", row.get("apIcao", ""))
        scheduled_value = row.get("STA", row.get("sta", ""))

    flt = _normalize_team_key_part(row.get("FLT", row.get("fpId", "")))
    leg = _normalize_team_key_part(leg_value)
    scheduled = _normalize_team_key_part(_normalize_hhmm(scheduled_value), upper=False)
    reg = _normalize_team_key_part(row.get("REG", row.get("acId", "")))
    spot = _normalize_team_key_part(row.get("SPOT", row.get("standDep", row.get("standArr", ""))))

    return "|".join(
        [
            base_date.isoformat(),
            str(direction).strip().lower(),
            f"flt:{flt}",
            f"leg:{leg}",
            f"sch:{scheduled}",
            f"reg:{reg}",
            f"spot:{spot}",
        ]
    )


def _attach_team_assignments(df: pd.DataFrame, base_date: date, direction: str) -> pd.DataFrame:
    assigned = df.copy()
    if assigned.empty:
        assigned["TEAM_KEY"] = pd.Series(dtype=str)
        assigned["TEAM"] = pd.Series(dtype=str)
        return assigned

    assignment_map = st.session_state.get("team_assignments", {})
    assigned["TEAM_KEY"] = assigned.apply(
        lambda row: _build_team_assignment_key(base_date, direction, row),
        axis=1,
    )
    assigned["TEAM"] = assigned["TEAM_KEY"].map(lambda key: _normalize_team_text(assignment_map.get(key, "")))
    return assigned


def _build_team_assignment_editor_rows(
    *,
    dep_records: pd.DataFrame,
    arr_records: pd.DataFrame,
    base_date: date,
) -> list[dict[str, str]]:
    grouped_rows: dict[str, dict[str, object]] = {}

    for direction, direction_label, records in (
        ("dep", "Departure", dep_records),
        ("arr", "Arrival", arr_records),
    ):
        if records is None or records.empty:
            continue

        for _, row in records.sort_values("marker").iterrows():
            team_key = _build_team_assignment_key(base_date, direction, row)
            raw_flt = str(row.get("FLT", "")).strip().upper()
            display_flt = raw_flt.replace("ESR", "ZE")
            if not display_flt:
                continue

            existing = grouped_rows.get(display_flt)
            current_team = _normalize_team_text(row.get("TEAM", ""))

            if existing is None:
                grouped_rows[display_flt] = {
                    "FLT": display_flt,
                    "Team": current_team,
                    "TEAM_KEYS": [team_key],
                    "_sort_time": row.get("marker"),
                }
                continue

            existing["TEAM_KEYS"].append(team_key)
            if not existing.get("Team") and current_team:
                existing["Team"] = current_team

    rows = list(grouped_rows.values())
    rows.sort(key=lambda item: (item.get("_sort_time"), item.get("FLT")))
    return [
        {
            "FLT": str(item["FLT"]),
            "Team": str(item["Team"]),
            "TEAM_KEYS": list(item.get("TEAM_KEYS", [])),
        }
        for item in rows
    ]


def _pick_service_day_time(record: dict, direction: str, time_basis: str) -> Optional[str]:
    if direction == "dep":
        keys = ("blockOffTime", "atd", "etd", "schTime") if str(time_basis).strip().lower() == "ground" else ("atd", "etd", "schTime")
    else:
        keys = ("blockOnTime", "ata", "eta", "sta") if str(time_basis).strip().lower() == "ground" else ("ata", "eta", "sta")
    for key in keys:
        hhmm = _normalize_hhmm(record.get(key))
        if hhmm is not None:
            return hhmm
    return None


def _compact_hhmm(value: object) -> str:
    if value is None or pd.isna(value):
        return ""

    text = str(value).strip()
    if not text or text.upper() in {"NAN", "NONE", "NULL"}:
        return ""

    digits = "".join(char for char in text if char.isdigit())
    if not digits:
        return ""
    if len(digits) >= 4:
        return digits[-4:]
    return digits.zfill(4)


def _normalize_flight_lookup_code(value: str) -> tuple[Optional[str], Optional[str], str]:
    normalized = "".join(char for char in str(value).upper() if char.isalnum())
    if len(normalized) < 4:
        return None, None, normalized

    airline_code = normalized[:3]
    flight_number = normalized[3:]
    if not airline_code.isalpha() or not flight_number:
        return None, None, normalized
    return airline_code, flight_number, normalized


def _lookup_result_for_date(
    *,
    flight_date: date,
    direction: str,
    airline_code: str,
    flight_number: str,
    full_code: str,
    departure_airport: str,
    arrival_airport: str,
    time_basis: str,
) -> dict:
    query = UbikaisQuery(
        flight_date=flight_date,
        airline=airline_code,
        departure_airport=departure_airport,
        arrival_airport=arrival_airport,
        flight_number=flight_number,
    )
    payload = fetch_records(direction, query, refresh=False)

    matching_records = [
        record
        for record in (payload.get("records") or [])
        if str(record.get("fpId", "")).strip().upper() == full_code
    ]

    if matching_records:
        if direction == "dep":
            matching_records.sort(
                key=lambda record: (
                    _compact_hhmm(record.get("schTime")) or "9999",
                    _compact_hhmm(record.get("etd")) or "9999",
                    _compact_hhmm(record.get("atd")) or "9999",
                )
            )
        else:
            matching_records.sort(
                key=lambda record: (
                    _compact_hhmm(record.get("sta")) or "9999",
                    _compact_hhmm(record.get("eta")) or "9999",
                    _compact_hhmm(record.get("ata")) or "9999",
                )
            )

    record = matching_records[0] if matching_records else None
    if direction == "dep":
        scheduled_label = "STD"
        scheduled_time = _compact_hhmm(record.get("schTime")) if record else ""
        actual_label = "BLOCK" if time_basis == "ground" else "ATD"
        actual_time = _compact_hhmm(record.get("blockOffTime")) if (record and time_basis == "ground") else (
            _compact_hhmm(record.get("atd")) if record else ""
        )
    else:
        scheduled_label = "STA"
        scheduled_time = _compact_hhmm(record.get("sta")) if record else ""
        actual_label = "BLOCK" if time_basis == "ground" else "ATA"
        actual_time = _compact_hhmm(record.get("blockOnTime")) if (record and time_basis == "ground") else (
            _compact_hhmm(record.get("ata")) if record else ""
        )

    return {
        "date": flight_date,
        "operated": bool(record),
        "scheduled_label": scheduled_label,
        "scheduled_time": scheduled_time,
        "actual_label": actual_label,
        "actual_time": actual_time,
        "record": record,
    }


def _render_flight_lookup_calendar(entries: list[dict]) -> str:
    if not entries:
        return ""

    weekday_labels = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    entry_map = {entry["date"]: entry for entry in entries}
    start_date = entries[0]["date"]
    end_date = entries[-1]["date"]

    calendar_start = start_date - timedelta(days=(start_date.weekday() + 1) % 7)
    calendar_end = end_date + timedelta(days=(5 - end_date.weekday()) % 7)

    parts = ['<div class="flight-lookup-calendar-wrap"><div class="flight-lookup-calendar">']
    time_values = sorted(
        {
            entry.get("scheduled_time")
            for entry in entries
            if entry.get("scheduled_time")
        }
    )
    palette = [
        "#3b82f6",
        "#f59e0b",
        "#ec4899",
        "#22c55e",
        "#8b5cf6",
        "#06b6d4",
        "#ef4444",
        "#84cc16",
        "#fb7185",
        "#a78bfa",
    ]
    time_color_map = {
        time_value: palette[index % len(palette)]
        for index, time_value in enumerate(time_values)
    }

    for weekday_label in weekday_labels:
        weekend_class = " is-weekend" if weekday_label in {"Sun", "Sat"} else ""
        parts.append(f'<div class="flight-lookup-head{weekend_class}">{escape(weekday_label)}</div>')

    current = calendar_start
    while current <= calendar_end:
        if current < start_date or current > end_date:
            parts.append('<div class="flight-lookup-cell is-empty"></div>')
        else:
            entry = entry_map[current]
            date_label = current.strftime("%m/%d")
            if entry["operated"]:
                scheduled_time = entry["scheduled_time"] or "----"
                actual_time = entry["actual_time"] or "----"
                scheduled_color = time_color_map.get(entry["scheduled_time"], "var(--text-color)")
                parts.append(
                    f'<div class="flight-lookup-cell">'
                    f'<div class="flight-lookup-date">{escape(date_label)}</div>'
                    f'<div class="flight-lookup-line">{escape(entry["scheduled_label"])} '
                    f'<span class="flight-lookup-time" style="color:{escape(scheduled_color)};">{escape(scheduled_time)}</span>'
                    f'</div>'
                    f'<div class="flight-lookup-line">{escape(entry["actual_label"])} '
                    f'<span class="flight-lookup-time">{escape(actual_time)}</span>'
                    f'</div>'
                    f'</div>'
                )
            else:
                parts.append(
                    f'<div class="flight-lookup-cell is-noop">'
                    f'<div class="flight-lookup-date">{escape(date_label)}</div>'
                    f'<div class="flight-lookup-status">No operation</div>'
                    f'</div>'
                )
        current += timedelta(days=1)

    parts.append("</div></div>")
    return "".join(parts)


def _hhmm_to_minutes(value: object) -> Optional[int]:
    hhmm = _compact_hhmm(value)
    if not hhmm:
        return None
    hours = int(hhmm[:2])
    minutes = int(hhmm[2:])
    if not (0 <= hours <= 23 and 0 <= minutes <= 59):
        return None
    return hours * 60 + minutes


def _minutes_to_hhmm(total_minutes: float | int) -> str:
    normalized_minutes = int(round(float(total_minutes))) % (24 * 60)
    hours, minutes = divmod(normalized_minutes, 60)
    return f"{hours:02d}{minutes:02d}"


def _unwrap_minutes(minutes: list[int]) -> tuple[list[int], int]:
    if not minutes:
        return [], 0

    ordered = sorted(minutes)
    if len(ordered) == 1:
        return ordered, ordered[0]

    gap_candidates = []
    for index, current_minute in enumerate(ordered):
        next_minute = ordered[(index + 1) % len(ordered)]
        if index == len(ordered) - 1:
            next_minute += 24 * 60
        gap_candidates.append((next_minute - current_minute, index))

    _, gap_index = max(gap_candidates)
    start_minute = ordered[(gap_index + 1) % len(ordered)]
    shifted = [minute if minute >= start_minute else minute + 24 * 60 for minute in minutes]
    return shifted, start_minute


def _circular_mean_minutes(minutes: list[int]) -> Optional[float]:
    if not minutes:
        return None

    angles = [(2 * math.pi * minute) / (24 * 60) for minute in minutes]
    sin_total = sum(math.sin(angle) for angle in angles)
    cos_total = sum(math.cos(angle) for angle in angles)
    if math.isclose(sin_total, 0.0, abs_tol=1e-9) and math.isclose(cos_total, 0.0, abs_tol=1e-9):
        return float(sum(minutes) / len(minutes))

    mean_angle = math.atan2(sin_total, cos_total)
    if mean_angle < 0:
        mean_angle += 2 * math.pi
    return (mean_angle * (24 * 60)) / (2 * math.pi)


def _nearest_wrapped_value(value: float, center: float) -> float:
    candidates = [value - 24 * 60, value, value + 24 * 60]
    return min(candidates, key=lambda candidate: abs(candidate - center))


def _tick_step_for_span(span_minutes: float) -> int:
    if span_minutes <= 120:
        return 10
    if span_minutes <= 360:
        return 30
    return 60


def _build_flight_lookup_distribution_chart(
    entries: list[dict],
    *,
    direction: str,
    time_basis: str,
) -> tuple[Optional[plt.Figure], int, int, Optional[str], Optional[str], Optional[str]]:
    operated_entries = [entry for entry in entries if entry["operated"]]
    actual_minutes = []
    for entry in operated_entries:
        minute_value = _hhmm_to_minutes(entry.get("actual_time"))
        if minute_value is not None:
            actual_minutes.append(minute_value)

    available_count = len(actual_minutes)
    operated_count = len(operated_entries)

    if direction == "dep":
        actual_label = "Block off" if time_basis == "ground" else "ATD"
    else:
        actual_label = "Block on" if time_basis == "ground" else "ATA"

    if not actual_minutes:
        return None, available_count, operated_count, actual_label, None, None

    shifted_minutes, start_minute = _unwrap_minutes(actual_minutes)
    min_minute = min(shifted_minutes)
    max_minute = max(shifted_minutes)
    span_minutes = max_minute - min_minute
    tick_step = _tick_step_for_span(span_minutes)
    padding = 30

    if span_minutes < 60:
        center_minute = (min_minute + max_minute) / 2
        min_minute = center_minute - 30
        max_minute = center_minute + 30
    else:
        min_minute -= padding
        max_minute += padding

    min_minute = math.floor(min_minute / tick_step) * tick_step
    max_minute = math.ceil(max_minute / tick_step) * tick_step

    plot_points = []
    bucket_levels: dict[int, int] = {}
    for shifted_minute in sorted(shifted_minutes):
        bucket = int(round(shifted_minute / 5))
        level = bucket_levels.get(bucket, 0)
        bucket_levels[bucket] = level + 1
        plot_points.append((shifted_minute, 0.16 + level * 0.14))

    max_y = max(y_value for _, y_value in plot_points) if plot_points else 0.2
    fig, ax = plt.subplots(figsize=(10, 2.4))
    fig.patch.set_alpha(0)
    ax.set_facecolor("none")

    x_values = [x_value for x_value, _ in plot_points]
    y_values = [y_value for _, y_value in plot_points]
    ax.scatter(
        x_values,
        y_values,
        s=54,
        color="#ff6b5a",
        edgecolors="#ffffff",
        linewidths=0.7,
        alpha=0.95,
        zorder=3,
    )

    mean_minute = _circular_mean_minutes(actual_minutes)
    mean_label = _minutes_to_hhmm(mean_minute) if mean_minute is not None else None
    median_label = _minutes_to_hhmm(statistics.median(shifted_minutes))
    if mean_minute is not None:
        center_reference = (min_minute + max_minute) / 2
        mean_x = _nearest_wrapped_value(mean_minute if mean_minute >= start_minute else mean_minute + 24 * 60, center_reference)
        ax.axvline(mean_x, color="#ffd166", linewidth=1.6, linestyle="--", zorder=2)

    ticks = list(range(int(min_minute), int(max_minute) + tick_step, tick_step))
    ax.set_xlim(min_minute, max_minute)
    ax.set_xticks(ticks)
    ax.set_xticklabels([_minutes_to_hhmm(tick) for tick in ticks], fontsize=9, color="#d1d5db")
    ax.grid(axis="x", color="#475569", alpha=0.35, linewidth=0.8)
    ax.tick_params(axis="x", length=0)
    ax.set_ylim(0, max_y + 0.18)
    ax.set_yticks([])
    for spine in ("left", "right", "top"):
        ax.spines[spine].set_visible(False)
    ax.spines["bottom"].set_color("#475569")
    ax.spines["bottom"].set_alpha(0.55)

    return fig, available_count, operated_count, actual_label, mean_label, median_label


def _filter_service_day_records(
    records: list[dict],
    *,
    direction: str,
    time_basis: str,
    service_start_hour: int,
    include_early_window: bool,
) -> list[dict]:
    service_start_minutes = int(service_start_hour) * 60
    filtered_records = []

    for record in records:
        hhmm = _pick_service_day_time(record, direction, time_basis)
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
    time_basis: str,
    service_start_hour: int,
) -> dict:
    base_records = _filter_service_day_records(
        base_payload.get("records") or [],
        direction=direction,
        time_basis=time_basis,
        service_start_hour=service_start_hour,
        include_early_window=False,
    )

    next_records: list[dict] = []
    if next_payload is not None and service_start_hour > 0:
        next_records = _filter_service_day_records(
            next_payload.get("records") or [],
            direction=direction,
            time_basis=time_basis,
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

if "flight_lookup_time_basis" not in st.session_state or st.session_state.flight_lookup_time_basis not in {"ground", "flight"}:
    st.session_state.flight_lookup_time_basis = st.session_state.time_basis

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
show_flt = st.sidebar.checkbox("FLT", key="show_flt")
show_turnaround = st.sidebar.checkbox("Turn-around", key="show_turnaround")
show_des_org = st.sidebar.checkbox("DES/ORG", key="show_des_org")
show_reg = st.sidebar.checkbox("REG", key="show_reg")
show_spot = st.sidebar.checkbox("SPOT", key="show_spot")
show_team = st.sidebar.checkbox("MEMO", key="show_team")

st.sidebar.markdown("---")
st.sidebar.header("Timeline Settings")
time_basis = st.sidebar.selectbox(
    "Time basis",
    options=["ground", "flight"],
    format_func=lambda value: "Ground ops (Block Time)" if value == "ground" else "Flight ops (ATD/ATA)",
    key="time_basis",
)
service_start_hour = st.sidebar.number_input(
    "Service day starts at (hour)",
    min_value=0,
    max_value=23,
    step=1,
    key="service_start_hour",
)
interval_min = st.sidebar.selectbox("Overlap interval (min)", options=[10, 20, 30], key="interval_min")

st.sidebar.markdown("---")
st.sidebar.subheader("Handling time (min)")
dep_before = st.sidebar.number_input("Departure handling (before ATD)", 0, 240, step=5, key="dep_before")
dep_after = st.sidebar.number_input("Departure handling (after ATD)", 0, 240, step=5, key="dep_after")
arr_before = st.sidebar.number_input("Arrival handling (before ATA)", 0, 240, step=5, key="arr_before")
arr_after = st.sidebar.number_input("Arrival handling (after ATA)", 0, 240, step=5, key="arr_after")
st.sidebar.markdown("---")
turnaround_limit_min = st.sidebar.number_input(
    "Turn-around limit (min)",
    min_value=1,
    max_value=1440,
    step=5,
    key="turnaround_limit_min",
)
st.sidebar.caption("Maximum allowed time for a Turn-around connection from Arrival to the next Departure.")

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
main_fetch_signature = (
    base_date.isoformat(),
    tuple(selected_airlines),
    query.departure_airport,
    query.arrival_airport,
    bool(int(service_start_hour) > 0),
)
needs_main_fetch = should_refresh or st.session_state.get("_main_fetch_signature") != main_fetch_signature

try:
    if needs_main_fetch:
        next_day_query = replace(query, flight_date=base_date + timedelta(days=1))
        spinner_context = st.spinner("Loading flight data from ubikais...")
        with spinner_context:
            dep_payload_base = fetch_records_for_airlines("dep", query, selected_airlines, refresh=should_refresh)
            arr_payload_base = fetch_records_for_airlines("arr", query, selected_airlines, refresh=should_refresh)

            dep_payload_next = None
            arr_payload_next = None
            if int(service_start_hour) > 0:
                dep_payload_next = fetch_records_for_airlines("dep", next_day_query, selected_airlines, refresh=should_refresh)
                arr_payload_next = fetch_records_for_airlines("arr", next_day_query, selected_airlines, refresh=should_refresh)

        st.session_state["_main_fetch_signature"] = main_fetch_signature
        st.session_state["_main_dep_payload_base"] = dep_payload_base
        st.session_state["_main_arr_payload_base"] = arr_payload_base
        st.session_state["_main_dep_payload_next"] = dep_payload_next
        st.session_state["_main_arr_payload_next"] = arr_payload_next
    else:
        dep_payload_base = st.session_state.get("_main_dep_payload_base")
        arr_payload_base = st.session_state.get("_main_arr_payload_base")
        dep_payload_next = st.session_state.get("_main_dep_payload_next")
        arr_payload_next = st.session_state.get("_main_arr_payload_next")

    dep_payload = _merge_service_day_payload(
        direction="dep",
        base_payload=dep_payload_base,
        next_payload=dep_payload_next,
        time_basis=str(time_basis),
        service_start_hour=int(service_start_hour),
    )
    arr_payload = _merge_service_day_payload(
        direction="arr",
        base_payload=arr_payload_base,
        next_payload=arr_payload_next,
        time_basis=str(time_basis),
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

dep_df = _attach_team_assignments(dep_df, base_date, "dep")
arr_df = _attach_team_assignments(arr_df, base_date, "arr")

desired_url_params = _build_url_params(
    selected_airlines=selected_airlines,
    type_preferences=type_preferences,
    show_flt=show_flt,
    show_des_org=show_des_org,
    show_reg=show_reg,
    show_spot=show_spot,
    show_team=show_team,
    show_turnaround=show_turnaround,
    time_basis=str(time_basis),
    service_start_hour=int(service_start_hour),
    interval_min=int(interval_min),
    dep_before=int(dep_before),
    dep_after=int(dep_after),
    arr_before=int(arr_before),
    arr_after=int(arr_after),
    turnaround_limit_min=int(turnaround_limit_min),
)
desired_url_signature = _url_signature(desired_url_params)
if desired_url_signature != current_url_signature:
    st.query_params.from_dict(desired_url_params)
    st.session_state["_applied_url_signature"] = desired_url_signature
    st.session_state["_applied_type_url_signature"] = desired_url_signature
    st.session_state["_url_excluded_types"] = _normalize_csv_values(desired_url_params.get("exclude_types"))

config = TimelineConfig(
    base_date=base_date,
    time_basis=str(time_basis),
    service_start_hour=int(service_start_hour),
    interval_min=int(interval_min),
    dep_before=int(dep_before),
    dep_after=int(dep_after),
    arr_before=int(arr_before),
    arr_after=int(arr_after),
    turnaround_limit_min=int(turnaround_limit_min),
    show_flt=show_flt,
    show_des_org=show_des_org,
    show_reg=show_reg,
    show_spot=show_spot,
    show_team=show_team,
    show_turnaround=show_turnaround,
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
        with st.expander("Flight memo", expanded=False):
            team_editor_rows = _build_team_assignment_editor_rows(
                dep_records=summary["dep_records"],
                arr_records=summary["arr_records"],
                base_date=base_date,
            )
            if not team_editor_rows:
                st.caption("No visible flights to assign.")
            else:
                editor_df = pd.DataFrame(team_editor_rows).set_index("FLT")
                filter_col, editor_col = st.columns([1.1, 2.4], gap="small")

                with filter_col:
                    team_filter = st.text_input(
                        "FLT filter",
                        key="team_assignment_filter",
                        placeholder="ex) ZE605",
                    ).strip()

                filtered_editor_df = editor_df
                if team_filter:
                    flt_mask = filtered_editor_df.index.astype(str).str.contains(team_filter, case=False, na=False)
                    filtered_editor_df = filtered_editor_df[flt_mask].copy()

                if filtered_editor_df.empty:
                    with editor_col:
                        st.caption("No flights match the current filter.")
                    filtered_editor_df = None

                visible_flights = list(filtered_editor_df.index) if filtered_editor_df is not None else []
                editor_signature = (
                    f"{len(visible_flights)}::"
                    f"{visible_flights[0] if visible_flights else ''}::"
                    f"{visible_flights[-1] if visible_flights else ''}"
                )
                team_editor_key = (
                    f"team_assignment_editor::{base_date.isoformat()}::{editor_signature}"
                )

                if filtered_editor_df is not None:
                    flt_to_team_keys = {
                        str(flt): [str(key) for key in (team_keys or []) if str(key)]
                        for flt, team_keys in filtered_editor_df["TEAM_KEYS"].items()
                    }
                    current_assignments = dict(st.session_state.get("team_assignments", {}))
                    updated_assignments = dict(current_assignments)
                    assignment_changed = False

                    if len(filtered_editor_df) == 1:
                        flight_code = str(filtered_editor_df.index[0]).strip()
                        team_keys = flt_to_team_keys.get(flight_code, [])
                        existing_values = {
                            _normalize_team_text(current_assignments.get(team_key, ""))
                            for team_key in team_keys
                        }
                        existing_values.discard("")
                        current_team = next(iter(existing_values), "")
                        single_team_key = f"single_team_input::{base_date.isoformat()}::{flight_code}"
                        if single_team_key not in st.session_state:
                            st.session_state[single_team_key] = current_team

                        with editor_col:
                            single_col1, single_col2 = st.columns([1.1, 1.6], gap="small")
                            with single_col1:
                                st.text_input("FLT", value=flight_code, disabled=True, key=f"{single_team_key}::flt")
                            with single_col2:
                                team_value = st.text_input("Memo", key=single_team_key)

                        normalized_team = _normalize_team_text(team_value)
                        if normalized_team != current_team:
                            for team_key in team_keys:
                                if normalized_team:
                                    updated_assignments[str(team_key)] = normalized_team
                                else:
                                    updated_assignments.pop(str(team_key), None)
                            assignment_changed = True
                    else:
                        editor_view_df = (
                            filtered_editor_df.drop(columns=["TEAM_KEYS"])
                            .reset_index()
                            .rename(columns={"Team": "Memo"})
                        )
                        with editor_col:
                            edited_team_df = st.data_editor(
                                editor_view_df,
                                hide_index=True,
                                width="stretch",
                                height=min(160, 52 + max(1, len(editor_view_df)) * 38),
                                column_order=["FLT", "Memo"],
                                disabled=["FLT"],
                                key=team_editor_key,
                            )

                        for _, row in edited_team_df.iterrows():
                            normalized_team = _normalize_team_text(row.get("Memo", ""))
                            flight_code = str(row.get("FLT", "")).strip()
                            team_keys = flt_to_team_keys.get(flight_code, [])
                            existing_values = {
                                _normalize_team_text(current_assignments.get(team_key, ""))
                                for team_key in team_keys
                            }
                            existing_values.discard("")
                            current_team = next(iter(existing_values), "")

                            if normalized_team == current_team:
                                continue

                            for team_key in team_keys:
                                if normalized_team:
                                    updated_assignments[str(team_key)] = normalized_team
                                else:
                                    updated_assignments.pop(str(team_key), None)
                            assignment_changed = True

                    if assignment_changed:
                        st.session_state.team_assignments = updated_assignments
                        st.rerun()
        with st.expander("Flight schedule lookup"):
            with st.form("flight_lookup_form", border=False, enter_to_submit=False):
                lookup_col1, lookup_col2 = st.columns(2, gap="small")
                with lookup_col1:
                    st.text_input("Flight", key="flight_lookup_code", placeholder="ex) ESR605")
                with lookup_col2:
                    st.selectbox(
                        "Flight type",
                        options=["dep", "arr"],
                        format_func=lambda value: "Departure" if value == "dep" else "Arrival",
                        index=None,
                        placeholder="Select flight type",
                        key="flight_lookup_direction",
                    )

                lookup_date_col1, lookup_date_col2 = st.columns(2, gap="small")
                with lookup_date_col1:
                    st.date_input("Start date", key="flight_lookup_start_date")
                with lookup_date_col2:
                    st.date_input("End date", key="flight_lookup_end_date")

                st.selectbox(
                    "Time basis",
                    options=["ground", "flight"],
                    format_func=lambda value: "Ground ops (Block Time)" if value == "ground" else "Flight ops (ATD/ATA)",
                    key="flight_lookup_time_basis",
                )

                st.markdown("<div style='height:0.35rem;'></div>", unsafe_allow_html=True)
                search_lookup = st.form_submit_button("Search", type="primary", width="stretch")
                st.markdown("<div style='height:0.45rem;'></div>", unsafe_allow_html=True)

            if search_lookup:
                st.session_state.flight_lookup_result = None

                lookup_start = st.session_state.flight_lookup_start_date
                lookup_end = st.session_state.flight_lookup_end_date
                if isinstance(lookup_start, datetime):
                    lookup_start = lookup_start.date()
                if isinstance(lookup_end, datetime):
                    lookup_end = lookup_end.date()

                airline_code, flight_number, normalized_flight = _normalize_flight_lookup_code(
                    st.session_state.flight_lookup_code
                )

                if not airline_code or not flight_number:
                    st.warning("Enter a full flight code like ESR605.")
                elif st.session_state.flight_lookup_direction not in {"dep", "arr"}:
                    st.warning("Select a flight type.")
                elif lookup_end < lookup_start:
                    st.warning("End date must be the same as or later than Start date.")
                elif (lookup_end - lookup_start).days > 30:
                    st.warning("Flight lookup range can be up to 31 days.")
                else:
                    with st.spinner("Searching flight history..."):
                        try:
                            entries = []
                            current_date = lookup_start
                            while current_date <= lookup_end:
                                entries.append(
                                    _lookup_result_for_date(
                                        flight_date=current_date,
                                        direction=st.session_state.flight_lookup_direction,
                                        airline_code=airline_code,
                                        flight_number=flight_number,
                                        full_code=normalized_flight,
                                        departure_airport=query.departure_airport,
                                        arrival_airport=query.arrival_airport,
                                        time_basis=str(st.session_state.flight_lookup_time_basis),
                                    )
                                )
                                current_date += timedelta(days=1)

                            operated_days = sum(1 for entry in entries if entry["operated"])
                            st.session_state.flight_lookup_result = {
                                "flight_code": normalized_flight,
                                "direction": st.session_state.flight_lookup_direction,
                                "start_date": lookup_start,
                                "end_date": lookup_end,
                                "entries": entries,
                                "operated_days": operated_days,
                                "not_operated_days": len(entries) - operated_days,
                                "time_basis": str(st.session_state.flight_lookup_time_basis),
                            }
                        except Exception as exc:
                            st.error(f"Flight lookup failed: {exc}")

            lookup_result = st.session_state.get("flight_lookup_result")
            if lookup_result:
                lookup_direction_label = "Departure" if lookup_result["direction"] == "dep" else "Arrival"
                summary_col1, summary_col2, summary_col3, summary_col4 = st.columns(4, gap="small")
                with summary_col1:
                    st.metric("Flight", lookup_result["flight_code"])
                with summary_col2:
                    st.metric("Flight type", lookup_direction_label)
                with summary_col3:
                    st.metric("Operated days", lookup_result["operated_days"])
                with summary_col4:
                    st.metric("No-op days", lookup_result["not_operated_days"])

                st.caption(
                    f"Period: {lookup_result['start_date'].strftime('%Y-%m-%d')} ~ "
                    f"{lookup_result['end_date'].strftime('%Y-%m-%d')}"
                )
                st.markdown(
                    _render_flight_lookup_calendar(lookup_result["entries"]),
                    unsafe_allow_html=True,
                )

                chart_fig, available_count, operated_count, actual_label, mean_label, median_label = _build_flight_lookup_distribution_chart(
                    lookup_result["entries"],
                    direction=lookup_result["direction"],
                    time_basis=lookup_result["time_basis"],
                )
                st.markdown("<div style='height:0.9rem;'></div>", unsafe_allow_html=True)
                st.markdown("**Actual time distribution**")
                availability_html = (
                    "<div style='display:flex; align-items:center; gap:0.7rem; flex-wrap:wrap; "
                    "margin:0.15rem 0 0.35rem 0;'>"
                    f"<span style='color:#9ca3af; font-size:0.95rem;'>Available: {available_count} / {operated_count} operated</span>"
                )
                if mean_label:
                    availability_html += (
                        f"<span style='color:#ffd166; font-size:0.98rem; font-weight:700;'>AVG {escape(mean_label)}</span>"
                    )
                if median_label:
                    availability_html += (
                        f"<span style='color:#8bd3ff; font-size:0.98rem; font-weight:700;'>MED {escape(median_label)}</span>"
                    )
                availability_html += "</div>"
                st.markdown(availability_html, unsafe_allow_html=True)
                if chart_fig is not None:
                    st.pyplot(chart_fig, width="stretch")
                    plt.close(chart_fig)
                elif operated_count:
                    st.info(f"No {actual_label} values are available in the selected period.")

                operated_entries = [entry for entry in lookup_result["entries"] if entry["operated"]]
                if operated_entries:
                    detail_rows = []
                    for entry in operated_entries:
                        record = entry["record"] or {}
                        if lookup_result["direction"] == "dep":
                            detail_rows.append(
                                {
                                    "Date": entry["date"].strftime("%Y-%m-%d"),
                                    "Day": entry["date"].strftime("%a").upper(),
                                    "Flight": lookup_result["flight_code"],
                                    "STD": _compact_hhmm(record.get("schTime")),
                                    "ETD": _compact_hhmm(record.get("etd")),
                                    "ATD": _compact_hhmm(record.get("atd")),
                                    "Block off": _compact_hhmm(record.get("blockOffTime")),
                                    "REG": str(record.get("acId", "")).strip(),
                                    "SPOT": str(record.get("standDep", "")).strip(),
                                }
                            )
                        else:
                            detail_rows.append(
                                {
                                    "Date": entry["date"].strftime("%Y-%m-%d"),
                                    "Day": entry["date"].strftime("%a").upper(),
                                    "Flight": lookup_result["flight_code"],
                                    "STA": _compact_hhmm(record.get("sta")),
                                    "ETA": _compact_hhmm(record.get("eta")),
                                    "ATA": _compact_hhmm(record.get("ata")),
                                    "Block on": _compact_hhmm(record.get("blockOnTime")),
                                    "REG": str(record.get("acId", "")).strip(),
                                    "SPOT": str(record.get("standArr", "")).strip(),
                                }
                            )

                    st.markdown("<div style='height:0.85rem;'></div>", unsafe_allow_html=True)
                    st.dataframe(pd.DataFrame(detail_rows), width="stretch", hide_index=True)
                else:
                    st.info("No operation found in the selected period.")
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
        with st.expander("Help", expanded=False):
            st.markdown(
                """
**기본 사용 방법**
- Date에서 조회할 날짜를 선택합니다.
- Airlines에서 보고 싶은 항공사를 고릅니다.
- Aircraft type에서 포함하거나 제외할 기종을 고릅니다.
- Filters 안에서 바꾼 값은 Apply를 눌러야 차트에 반영됩니다.
- Refresh를 누르면 ubikais에서 최신 데이터를 다시 가져옵니다.

**Labels on bars**
- FLT: 항공편 번호를 표시합니다.
- DES/ORG: Departure는 destination airport, Arrival는 origin airport를 표시합니다.
- REG: 항공기 등록부호를 표시합니다.
- SPOT: Spot 정보를 표시합니다.
- Turn-around: 도착편과 다음 출발편의 연결 관계를 화살표로 표시합니다.

**Time basis**
- Ground ops (Block Time): blockOn / blockOff time을 우선으로 사용합니다.
- Flight ops (ATD/ATA): ATA / ATD를 우선으로 사용합니다.

**Service day starts at (hour)**
- 이 값은 하루의 기준 시작 시각을 정합니다.
- 예를 들어 0이면 00:00부터 24:00까지를 같은 날짜 차트로 봅니다.
- 2이면 해당 날짜 02:00부터 다음날 01:59까지를 같은 service day로 봅니다.
- 따라서 새벽 항공편을 전날 operation으로 포함해서 보고 싶을 때 사용합니다.

**Handling time (min)**
- Departure handling (before ATD), Departure handling (after ATD)는 Departure 막대 길이를 정합니다.
- Arrival handling (before ATA), Arrival handling (after ATA)는 Arrival 막대 길이를 정합니다.
- 이 값은 차트에서 handling time을 얼마나 길게 볼지 정하는 설정입니다.

**Turn-around**
- Turn-around는 Arrival 이후 일정 시간 안에 이어지는 Departure를 연결편으로 봅니다.
- 기본적으로 REG 또는 SPOT 중 하나가 같고, Turn-around limit 안에 있으면 연결 후보가 됩니다.
- 후보가 여러 개면 가장 가까운 다음 Departure 1개를 연결합니다.

**URL 저장**
- Airlines, Aircraft type, Labels on bars, Timeline Settings, Handling time, Turn-around limit 값은 URL에 반영됩니다.
- 같은 URL을 다시 열면 해당 설정이 초기값으로 복원됩니다.
- Date는 URL에 저장되지 않으며, 앱을 열 때 기준의 오늘 날짜로 시작합니다.
                """
            )
