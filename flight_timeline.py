from __future__ import annotations

import math
from dataclasses import dataclass
from datetime import date, datetime, time, timedelta
from typing import Any

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import transforms


F_BEFORE = 20
F_AFTER = 10
MAX_ROWS_PER_PANEL = 18
A4_LANDSCAPE_WIDTH = 11.69
A4_LANDSCAPE_HEIGHT = 8.27

COL_ARR = "#1f77b4"
COL_DEP = "#d62728"


@dataclass(frozen=True)
class TimelineConfig:
    base_date: date
    service_start_hour: int = 2
    interval_min: int = 30
    dep_before: int = 50
    dep_after: int = 10
    arr_before: int = 20
    arr_after: int = 30
    show_flt: bool = True
    show_reg: bool = False
    show_spot: bool = False


def departures_from_ubikais(records: list[dict[str, Any]]) -> pd.DataFrame:
    df = pd.DataFrame(records)
    if df.empty:
        return pd.DataFrame(columns=["FLT", "REG", "TYP", "SPOT", "ATD", "ETD", "STD"])

    return pd.DataFrame(
        {
            "FLT": _series_or_blank(df, "fpId"),
            "REG": _series_or_blank(df, "acId"),
            "TYP": _series_or_blank(df, "acType"),
            "SPOT": _series_or_blank(df, "standDep"),
            "ATD": _series_or_blank(df, "atd"),
            "ETD": _series_or_blank(df, "etd"),
            "STD": _series_or_blank(df, "schTime"),
        }
    )


def arrivals_from_ubikais(records: list[dict[str, Any]]) -> pd.DataFrame:
    df = pd.DataFrame(records)
    if df.empty:
        return pd.DataFrame(columns=["FLT", "REG", "TYP", "SPOT", "ATA", "ETA", "STA"])

    return pd.DataFrame(
        {
            "FLT": _series_or_blank(df, "fpId"),
            "REG": _series_or_blank(df, "acId"),
            "TYP": _series_or_blank(df, "acType"),
            "SPOT": _series_or_blank(df, "standArr"),
            "ATA": _series_or_blank(df, "ata"),
            "ETA": _series_or_blank(df, "eta"),
            "STA": _series_or_blank(df, "sta"),
        }
    )


def build_timeline_figure(
    dep_df: pd.DataFrame,
    arr_df: pd.DataFrame,
    config: TimelineConfig,
):
    dep_plot = _prepare_departures(dep_df, config)
    arr_plot = _prepare_arrivals(arr_df, config)

    dep_intervals = dep_plot[["start", "end"]].copy() if len(dep_plot) > 0 else pd.DataFrame(columns=["start", "end"])
    arr_intervals = arr_plot[["start", "end"]].copy() if len(arr_plot) > 0 else pd.DataFrame(columns=["start", "end"])

    if dep_intervals.empty and arr_intervals.empty:
        raise ValueError("No records to plot after applying time fallbacks.")

    start_candidates = []
    end_candidates = []
    if not dep_intervals.empty:
        start_candidates.append(dep_intervals["start"].min())
        end_candidates.append(dep_intervals["end"].max())
    if not arr_intervals.empty:
        start_candidates.append(arr_intervals["start"].min())
        end_candidates.append(arr_intervals["end"].max())

    start_time = min(start_candidates)
    end_time = max(end_candidates)
    time_range = pd.date_range(start=start_time, end=end_time, freq=f"{config.interval_min}min")
    if len(time_range) < 2:
        time_range = pd.date_range(
            start=start_time,
            end=end_time + timedelta(minutes=config.interval_min),
            freq=f"{config.interval_min}min",
        )

    mid_times = [
        time_range[i] + (time_range[i + 1] - time_range[i]) / 2
        for i in range(len(time_range) - 1)
    ]
    dep_counts = [_count_overlaps(dep_intervals, t) for t in mid_times]
    arr_counts = [_count_overlaps(arr_intervals, t) for t in mid_times]

    dep_block = dep_plot[["Label", "start", "end", "marker", "type", "time_str"]].sort_values("start").reset_index(drop=True)
    arr_block = arr_plot[["Label", "start", "end", "marker", "type", "time_str"]].sort_values("start").reset_index(drop=True)

    total_dep = len(dep_block)
    total_arr = len(arr_block)
    visible_rows = max(total_dep, total_arr, 1)
    panel_count = max(1, math.ceil(visible_rows / MAX_ROWS_PER_PANEL))
    rows_per_panel = max(1, math.ceil(visible_rows / panel_count))
    dep_wrapped = _assign_wrap_rows(dep_block, rows_per_panel)
    arr_wrapped = _assign_wrap_rows(arr_block, rows_per_panel)

    fig_height = max(A4_LANDSCAPE_HEIGHT, rows_per_panel * 0.28 + 3.0)
    fig, ax = plt.subplots(figsize=(A4_LANDSCAPE_WIDTH, fig_height))
    fig.subplots_adjust(left=0.04, right=0.98, top=0.90, bottom=0.18)

    ax.set_title("Flight Handling Timeline")
    ax.text(
        0.01,
        1.02,
        f"{config.base_date.strftime('%Y-%m-%d')} ({config.base_date.strftime('%a').upper()})",
        transform=ax.transAxes,
        ha="left",
        va="bottom",
        fontsize=11,
        color="#333333",
    )
    ax.text(
        0.99,
        1.02,
        f"Total Departure: {total_dep}   Total Arrival: {total_arr}",
        transform=ax.transAxes,
        ha="right",
        va="bottom",
        fontsize=11,
        color="#333333",
    )

    _plot_wrapped_timeline(
        ax,
        dep_block=dep_wrapped,
        arr_block=arr_wrapped,
        panel_count=panel_count,
        rows_per_panel=rows_per_panel,
        x_start=start_time,
        x_end=end_time,
    )
    _plot_overlap_numbers(
        ax,
        mid_times=mid_times,
        dep_counts=dep_counts,
        arr_counts=arr_counts,
    )

    summary = {
        "start_time": start_time,
        "end_time": end_time,
        "total_dep": total_dep,
        "total_arr": total_arr,
        "panel_count": panel_count,
        "dep_records": dep_plot,
        "arr_records": arr_plot,
    }
    return fig, summary


def _prepare_departures(dep_df: pd.DataFrame, config: TimelineConfig) -> pd.DataFrame:
    dep_df = dep_df.copy()
    dep_df["TIME_RAW"] = dep_df.apply(_pick_time_dep, axis=1)
    dep_df = dep_df[pd.notna(dep_df["TIME_RAW"])].reset_index(drop=True)

    dep_df["time_dt"] = dep_df["TIME_RAW"].apply(
        lambda value: hhmm_to_datetime(config.base_date, value, config.service_start_hour)
    )
    dep_df["time_dt"] = pd.to_datetime(dep_df["time_dt"], errors="coerce")
    dep_df = dep_df.dropna(subset=["time_dt"]).reset_index(drop=True)

    dep_df["is_F"] = dep_df["FLT"].astype(str).str.strip().str.upper().str.endswith("F")
    dep_df["start"] = dep_df.apply(
        lambda row: row["time_dt"] - timedelta(minutes=(F_BEFORE if row["is_F"] else int(config.dep_before))),
        axis=1,
    )
    dep_df["end"] = dep_df.apply(
        lambda row: row["time_dt"] + timedelta(minutes=(F_AFTER if row["is_F"] else int(config.dep_after))),
        axis=1,
    )
    dep_df["marker"] = dep_df["time_dt"]
    dep_df["type"] = "DEP"
    dep_df["time_str"] = dep_df["time_dt"].dt.strftime("%H:%M")
    dep_df["Label"] = dep_df.apply(
        lambda row: label_for(
            row["FLT"],
            row.get("REG", ""),
            row.get("SPOT", ""),
            show_flt=config.show_flt,
            show_reg=config.show_reg,
            show_spot=config.show_spot,
        ),
        axis=1,
    )
    return dep_df


def _prepare_arrivals(arr_df: pd.DataFrame, config: TimelineConfig) -> pd.DataFrame:
    arr_df = arr_df.copy()
    arr_df["TIME_RAW"] = arr_df.apply(_pick_time_arr, axis=1)
    arr_df = arr_df[pd.notna(arr_df["TIME_RAW"])].reset_index(drop=True)

    arr_df["time_dt"] = arr_df["TIME_RAW"].apply(
        lambda value: hhmm_to_datetime(config.base_date, value, config.service_start_hour)
    )
    arr_df["time_dt"] = pd.to_datetime(arr_df["time_dt"], errors="coerce")
    arr_df = arr_df.dropna(subset=["time_dt"]).reset_index(drop=True)

    arr_df["is_F"] = arr_df["FLT"].astype(str).str.strip().str.upper().str.endswith("F")
    arr_df["start"] = arr_df.apply(
        lambda row: row["time_dt"] - timedelta(minutes=(F_BEFORE if row["is_F"] else int(config.arr_before))),
        axis=1,
    )
    arr_df["end"] = arr_df.apply(
        lambda row: row["time_dt"] + timedelta(minutes=(F_AFTER if row["is_F"] else int(config.arr_after))),
        axis=1,
    )
    arr_df["marker"] = arr_df["time_dt"]
    arr_df["type"] = "ARR"
    arr_df["time_str"] = arr_df["time_dt"].dt.strftime("%H:%M")
    arr_df["Label"] = arr_df.apply(
        lambda row: label_for(
            row["FLT"],
            row.get("REG", ""),
            row.get("SPOT", ""),
            show_flt=config.show_flt,
            show_reg=config.show_reg,
            show_spot=config.show_spot,
        ),
        axis=1,
    )
    return arr_df


def _plot_wrapped_timeline(
    ax,
    dep_block: pd.DataFrame,
    arr_block: pd.DataFrame,
    *,
    panel_count: int,
    rows_per_panel: int,
    x_start,
    x_end,
) -> None:
    ax.set_facecolor("#ffffff")
    ax.set_xlim(x_start, x_end)
    ax.grid(True, axis="x", linestyle="--", alpha=0.25)
    ax.grid(False, axis="y")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.tick_params(axis="y", which="both", left=False, labelleft=False)
    ax.xaxis.set_major_locator(mdates.HourLocator(interval=2))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%H:%M"))
    for label in ax.get_xticklabels():
        label.set_rotation(0)
        label.set_ha("center")

    if dep_block.empty and arr_block.empty:
        ax.text(0.5, 0.5, "No flights", transform=ax.transAxes, ha="center", va="center", color="#777777")
        ax.set_yticks([])
        return

    dep_labeled = False
    for _, row in dep_block.iterrows():
        y_pos = row["wrap_row"]
        legend_label = "Departure" if not dep_labeled else ""
        dep_labeled = True
        ax.plot([row["start"], row["end"]], [y_pos, y_pos], color=COL_DEP, linewidth=4, label=legend_label, zorder=2)
        if row["Label"]:
            ax.text(
                row["end"] + timedelta(minutes=5),
                y_pos,
                row["Label"],
                va="center",
                fontsize=7,
                color=COL_DEP,
                clip_on=False,
            )
        ax.scatter(row["marker"], y_pos, color=COL_DEP, s=28, marker="o", zorder=3)
        ax.text(
            row["marker"] - timedelta(minutes=3),
            y_pos + 0.15,
            row["time_str"],
            ha="right",
            va="bottom",
            fontsize=7,
            color=COL_DEP,
        )

    arr_labeled = False
    for _, row in arr_block.iterrows():
        row_y = row["wrap_row"] + 0.55
        legend_label = "Arrival" if not arr_labeled else ""
        arr_labeled = True
        ax.plot([row["start"], row["end"]], [row_y, row_y], color=COL_ARR, linewidth=4, label=legend_label, zorder=2)
        if row["Label"]:
            ax.text(
                row["end"] + timedelta(minutes=5),
                row_y,
                row["Label"],
                va="center",
                fontsize=7,
                color=COL_ARR,
                clip_on=False,
            )
        ax.scatter(row["marker"], row_y, color=COL_ARR, s=28, marker="s", zorder=3)
        ax.text(
            row["marker"] - timedelta(minutes=3),
            row_y + 0.15,
            row["time_str"],
            ha="right",
            va="bottom",
            fontsize=7,
            color=COL_ARR,
        )

    ax.set_ylim(-0.75, rows_per_panel + 0.2)
    ax.legend(loc="upper left")


def _plot_overlap_numbers(
    ax,
    mid_times,
    dep_counts: list[int],
    arr_counts: list[int],
) -> None:
    totals = [dep + arr for dep, arr in zip(dep_counts, arr_counts)]
    trans = transforms.blended_transform_factory(ax.transData, ax.transAxes)
    max_dep = max(dep_counts) if dep_counts else 1
    max_arr = max(arr_counts) if arr_counts else 1

    for mid, total, dep_count, arr_count in zip(mid_times, totals, dep_counts, arr_counts):
        if total > 0:
            ax.text(mid, -0.06, str(total), transform=trans, ha="center", va="top", fontsize=8, color="black")
        if dep_count > 0:
            alpha = 0.35 + 0.65 * (dep_count / max_dep)
            ax.text(
                mid,
                -0.10,
                str(dep_count),
                transform=trans,
                ha="center",
                va="top",
                fontsize=8,
                color=(0.84, 0.15, 0.16, alpha),
            )
        if arr_count > 0:
            alpha = 0.35 + 0.65 * (arr_count / max_arr)
            ax.text(
                mid,
                -0.14,
                str(arr_count),
                transform=trans,
                ha="center",
                va="top",
                fontsize=8,
                color=(0.12, 0.46, 0.70, alpha),
            )


def _assign_wrap_rows(block: pd.DataFrame, rows_per_panel: int) -> pd.DataFrame:
    if block.empty:
        return block.assign(wrap_panel=pd.Series(dtype=int), wrap_row=pd.Series(dtype=float))

    wrapped = block.copy()
    wrapped["wrap_panel"] = wrapped.index // rows_per_panel
    wrapped["wrap_row"] = wrapped.index % rows_per_panel
    return wrapped




def hhmm_to_datetime(base_date: date, hhmm: Any, service_start_hour: int):
    if pd.isna(hhmm):
        return None

    if isinstance(hhmm, (datetime, pd.Timestamp)):
        current_time = hhmm.time()
    else:
        if isinstance(hhmm, (int, float)) and not (isinstance(hhmm, float) and math.isnan(hhmm)):
            try:
                raw = f"{int(round(hhmm)):04d}"
            except Exception:
                return None
        else:
            digits = "".join(ch for ch in str(hhmm).strip() if ch.isdigit())
            raw = f"0{digits}" if len(digits) == 3 else digits

        if len(raw) != 4:
            return None
        try:
            current_time = datetime.strptime(raw, "%H%M").time()
        except ValueError:
            return None

    dt = datetime.combine(base_date, current_time)
    if time(current_time.hour, current_time.minute) < time(service_start_hour, 0):
        dt += timedelta(days=1)
    return dt


def label_for(
    flt: Any,
    reg: Any,
    spot: Any = None,
    *,
    show_flt: bool,
    show_reg: bool,
    show_spot: bool,
) -> str:
    parts = []
    if show_flt:
        parts.append(str(flt).replace("ESR", "ZE"))
    if show_reg and pd.notna(reg) and str(reg).strip():
        parts.append(str(reg))
    if show_spot and pd.notna(spot) and str(spot).strip():
        parts.append(f"#{str(spot).strip()}")
    return " / ".join(parts)


def _pick_time_dep(row: pd.Series):
    for key in ("ATD", "ETD", "STD"):
        value = row.get(key, pd.NA)
        if pd.notna(value) and str(value).strip():
            return value
    return pd.NA


def _pick_time_arr(row: pd.Series):
    for key in ("ATA", "ETA", "STA"):
        value = row.get(key, pd.NA)
        if pd.notna(value) and str(value).strip():
            return value
    return pd.NA


def _count_overlaps(intervals: pd.DataFrame, moment) -> int:
    if len(intervals) == 0:
        return 0
    return int(((intervals["start"] <= moment) & (intervals["end"] > moment)).sum())


def _series_or_blank(df: pd.DataFrame, column: str) -> pd.Series:
    if column in df.columns:
        return df[column]
    return pd.Series([""] * len(df))
