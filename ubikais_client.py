from __future__ import annotations

import json
import time
from dataclasses import asdict, dataclass
from datetime import date
from pathlib import Path
from typing import Any, Literal
from urllib.parse import urlencode
from urllib.request import Request, urlopen


Direction = Literal["dep", "arr"]

BASE_URL = "https://ubikais.fois.go.kr:8030/sysUbikais/biz/fpl"
ENDPOINTS: dict[Direction, str] = {
    "dep": "selectDep.fois",
    "arr": "selectArr.fois",
}


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
    cache_dir: str | Path = "cache",
    refresh: bool = False,
    cookie_header: str | None = None,
) -> dict[str, Any]:
    cache_path = _cache_path(cache_dir, direction, query)
    if cache_path.exists() and not refresh:
        return json.loads(cache_path.read_text(encoding="utf-8"))

    records: list[dict[str, Any]] = []
    total: int | None = None
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


def _request_page(
    *,
    direction: Direction,
    query: UbikaisQuery,
    offset: int,
    cookie_header: str | None,
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


def _cache_path(cache_dir: str | Path, direction: Direction, query: UbikaisQuery) -> Path:
    safe_airline = query.airline or "ALL"
    safe_flight = query.flight_number or "ALL"
    safe_dep = query.departure_airport or "ANY"
    safe_arr = query.arrival_airport or "ANY"
    filename = (
        f"{query.date_compact}_{direction}_{safe_airline}_{safe_dep}_{safe_arr}_{safe_flight}.json"
    )
    return Path(cache_dir) / filename


def _serialize_query(query: UbikaisQuery) -> dict[str, Any]:
    raw = asdict(query)
    raw["flight_date"] = query.date_text
    return raw
