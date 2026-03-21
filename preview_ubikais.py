from __future__ import annotations

import argparse
import os
from datetime import date, datetime
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Preview ubikais flight handling timeline without Streamlit.")
    parser.add_argument("--date", dest="flight_date", type=parse_date, default=date.today())
    parser.add_argument("--airline", default="ESR")
    parser.add_argument("--dep-airport", default="RKSI")
    parser.add_argument("--arr-airport", default="RKSI")
    parser.add_argument("--flight-number", default="")
    parser.add_argument("--service-start-hour", type=int, default=2)
    parser.add_argument("--interval", type=int, default=30, choices=[10, 20, 30])
    parser.add_argument("--dep-before", type=int, default=50)
    parser.add_argument("--dep-after", type=int, default=10)
    parser.add_argument("--arr-before", type=int, default=20)
    parser.add_argument("--arr-after", type=int, default=30)
    parser.add_argument("--hide-flt", action="store_true")
    parser.add_argument("--show-reg", action="store_true")
    parser.add_argument("--show-spot", action="store_true")
    parser.add_argument("--show", action="store_true", help="Open a matplotlib window after saving the image.")
    parser.add_argument("--refresh", action="store_true", help="Ignore cached JSON and fetch again.")
    parser.add_argument("--cache-dir", default="cache")
    parser.add_argument("--output-dir", default="preview_output")
    return parser.parse_args()


def parse_date(value: str) -> date:
    return datetime.strptime(value, "%Y-%m-%d").date()


def main() -> None:
    args = parse_args()

    if not args.show:
        import matplotlib

        matplotlib.use("Agg")

    from flight_timeline import (
        TimelineConfig,
        arrivals_from_ubikais,
        build_timeline_figure,
        departures_from_ubikais,
    )
    from ubikais_client import UbikaisQuery, fetch_records

    cookie_header = os.getenv("UBIKAIS_COOKIE")
    query = UbikaisQuery(
        flight_date=args.flight_date,
        airline=args.airline,
        departure_airport=args.dep_airport,
        arrival_airport=args.arr_airport,
        flight_number=args.flight_number,
    )

    dep_payload = fetch_records(
        "dep",
        query,
        cache_dir=args.cache_dir,
        refresh=args.refresh,
        cookie_header=cookie_header,
    )
    arr_payload = fetch_records(
        "arr",
        query,
        cache_dir=args.cache_dir,
        refresh=args.refresh,
        cookie_header=cookie_header,
    )

    dep_df = departures_from_ubikais(dep_payload["records"])
    arr_df = arrivals_from_ubikais(arr_payload["records"])

    config = TimelineConfig(
        base_date=args.flight_date,
        service_start_hour=args.service_start_hour,
        interval_min=args.interval,
        dep_before=args.dep_before,
        dep_after=args.dep_after,
        arr_before=args.arr_before,
        arr_after=args.arr_after,
        show_flt=not args.hide_flt,
        show_reg=args.show_reg,
        show_spot=args.show_spot,
    )

    fig, summary = build_timeline_figure(dep_df, arr_df, config)

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / (
        f"{args.flight_date:%Y-%m-%d}_{args.airline}_D{summary['total_dep']}_A{summary['total_arr']}.png"
    )
    fig.savefig(output_path, dpi=200, bbox_inches="tight")

    print(f"Saved preview to: {output_path.resolve()}")
    print(f"Departure records: {summary['total_dep']}")
    print(f"Arrival records:   {summary['total_arr']}")

    if args.show:
        import matplotlib.pyplot as plt

        plt.show()


if __name__ == "__main__":
    main()
