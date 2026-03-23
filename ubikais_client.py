from __future__ import annotations

import json
import time
from dataclasses import asdict, dataclass, replace
from datetime import date
from pathlib import Path
from typing import Any, Literal, Optional, Union
from urllib.parse import urlencode
from urllib.request import Request, urlopen


Direction = Literal["dep", "arr"]

BASE_URL = "https://ubikais.fois.go.kr:8030/sysUbikais/biz/fpl"
ENDPOINTS: dict[Direction, str] = {
    "dep": "selectDep.fois",
    "arr": "selectArr.fois",
}
CACHE_TTL_SECONDS = 15 * 60


@dataclass(frozen=True)
class UbikaisQuery:
    flight_date: date
    airline: str = "ESR"
    departure_airport: str = "RKSI"
    arrival_airport: str = "RKSI"
    flight_number: str = ""
    limit: int = 100

    @property
    def date_text(self) -> str:
        return self.flight_date.strftime("%Y-%m-%d")

    @property
    def date_compact(self) -> str:
        return self.flight_date.strftime("%Y%m%d")


def fetch_records(
    direction: Direction,
    query: UbikaisQuery,
    *,
    cache_dir: Union[str, Path] = "cache",
    refresh: bool = False,
    cookie_header: Optional[str] = None,
) -> dict[str, Any]:
    cache_path = _cache_path(cache_dir, direction, query)
    if cache_path.exists() and not refresh:
        cached_payload = _load_cache_if_fresh(cache_path)
        if cached_payload is not None:
            return cached_payload

    records: list[dict[str, Any]] = []
    total: Optional[int] = None
    offset = 0

    while True:
        payload = _request_page(
            direction=direction,
            query=query,
            offset=offset,
            cookie_header=cookie_header,
        )
        status = payload.get("status")
        if status != "success":
            raise RuntimeError(f"Ubikais returned status={status!r}: {payload.get('msg', '')}")

        page_records = payload.get("records") or []
        total = int(payload.get("total", len(page_records)))
        records.extend(page_records)

        if not page_records or len(records) >= total:
            break

        offset += len(page_records)

    result = {
        "status": "success",
        "direction": direction,
        "query": _serialize_query(query),
        "fetched_at": int(time.time()),
        "total": total if total is not None else len(records),
        "records": records,
    }

    cache_path.parent.mkdir(parents=True, exist_ok=True)
    cache_path.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    return result


def fetch_records_for_airlines(
    direction: Direction,
    query: UbikaisQuery,
    airlines: list[str],
    *,
    cache_dir: Union[str, Path] = "cache",
    refresh: bool = False,
    cookie_header: Optional[str] = None,
) -> dict[str, Any]:
    normalized_airlines = []
    for airline in airlines:
        airline_code = str(airline).strip().upper()
        if airline_code and airline_code not in normalized_airlines:
            normalized_airlines.append(airline_code)

    if not normalized_airlines:
        raise ValueError("At least one airline code is required.")

    merged_records: list[dict[str, Any]] = []
    fetched_at_values: list[int] = []

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
            **_serialize_query(query),
            "airlines": normalized_airlines,
        },
        "fetched_at": max(fetched_at_values) if fetched_at_values else None,
        "total": len(merged_records),
        "records": merged_records,
    }


def _request_page(
    *,
    direction: Direction,
    query: UbikaisQuery,
    offset: int,
    cookie_header: Optional[str],
) -> dict[str, Any]:
    params = {
        "downloadYn": 1,
        "srchDate": query.date_text,
        "srchDatesh": query.date_compact,
        "srchAl": query.airline,
        "srchFln": query.flight_number,
        "srchDep": query.departure_airport if direction == "dep" else "",
        "srchArr": query.arrival_airport if direction == "arr" else "",
        "dummy": int(time.time() * 1000),
        "cmd": "get-records",
        "limit": query.limit,
        "offset": offset,
    }
    url = f"{BASE_URL}/{ENDPOINTS[direction]}?{urlencode(params)}"
    request = Request(
        url,
        headers={
            "Accept": "application/json, text/plain, */*",
            "User-Agent": "Mozilla/5.0",
            **({"Cookie": cookie_header} if cookie_header else {}),
        },
    )

    with urlopen(request, timeout=20) as response:
        body = response.read().decode("utf-8")

    try:
        return json.loads(body)
    except json.JSONDecodeError as exc:
        snippet = body[:200].replace("\n", " ").strip()
        raise RuntimeError(
            "Ubikais response was not JSON. "
            f"Check whether the endpoint changed or requires session data. Snippet: {snippet!r}"
        ) from exc


def _cache_path(cache_dir: Union[str, Path], direction: Direction, query: UbikaisQuery) -> Path:
    safe_airline = query.airline or "ALL"
    safe_flight = query.flight_number or "ALL"
    safe_dep = query.departure_airport or "ANY"
    safe_arr = query.arrival_airport or "ANY"
    filename = (
        f"{query.date_compact}_{direction}_{safe_airline}_{safe_dep}_{safe_arr}_{safe_flight}.json"
    )
    return Path(cache_dir) / filename


def _load_cache_if_fresh(cache_path: Path) -> Optional[dict[str, Any]]:
    try:
        payload = json.loads(cache_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None

    fetched_at = payload.get("fetched_at")
    if fetched_at is None:
        try:
            fetched_at = int(cache_path.stat().st_mtime)
        except OSError:
            return None

    try:
        age_seconds = time.time() - float(fetched_at)
    except (TypeError, ValueError):
        return None

    if age_seconds <= CACHE_TTL_SECONDS:
        return payload
    return None


def _serialize_query(query: UbikaisQuery) -> dict[str, Any]:
    raw = asdict(query)
    raw["flight_date"] = query.date_text
    return raw
