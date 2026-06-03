# HANDOFF

Generated: 2026-06-03

This handoff is based only on the current project file state. Previous Codex session context was intentionally ignored.

## Work Method Notes

- Did not read the whole project at once.
- First checked top-level structure and file list only.
- Read only selected parts of key files: imports, constants, function definitions, app UI sections, and cache/client logic.
- Large generated/data-like files were not read in full.
- Items that are not certain are marked as "확인 필요".

## Project Structure

Top-level files and directories:

- `.git/` - Git repository metadata.
- `.gitignore` - ignores `__pycache__/`, `*.pyc`, `cache/`, `preview_output/`, `.streamlit/secrets.toml`.
- `requirements.txt` - Python dependencies.
- `before_app.py` - Streamlit app entry candidate. 확인 필요: actual run/deploy entrypoint.
- `flight_timeline.py` - Matplotlib timeline construction and Ubikais record normalization.
- `ubikais_client.py` - Ubikais API client, pagination, and JSON cache handling.
- `preview_ubikais.py` - CLI preview renderer that saves PNG output without Streamlit.
- `airport_codes.py` - generated ICAO-to-IATA lookup table.
- `_date_block.txt` - small Streamlit sidebar date-navigation snippet. 확인 필요: whether this is scratch/reference text.
- `cache/` - ignored Ubikais JSON cache. Currently 697 files.
- `preview_output/` - ignored generated PNG previews. Currently 2 files.
- `__pycache__/` - ignored Python bytecode cache.

## Main File Roles

- `before_app.py`
  - Streamlit UI for flight handling schedule visualization.
  - Uses `flight_timeline.py` to build the chart and `ubikais_client.py` to load Ubikais data.
  - Maintains Streamlit session state for date, airline filters, aircraft type filters, label flags, timeline settings, memo assignments, and flight lookup state.
  - Syncs many options to URL query parameters.
  - Fetches both base-date and next-date data to build a service day window when `service_start_hour > 0`.
  - Shows sidebar controls, main timeline chart, memo editor, refresh/download actions, flight schedule lookup, details, raw data preview, and help.

- `flight_timeline.py`
  - Converts Ubikais departure/arrival records into plotting DataFrames.
  - Defines `TimelineConfig`.
  - Builds a Matplotlib figure with departure/arrival handling bars, overlap counts, optional memo badges, optional turn-around links, row wrapping, and spill rows to reduce visual collisions.
  - Maps ICAO airport codes to IATA labels through `airport_codes.icao_to_iata`.

- `ubikais_client.py`
  - Defines `UbikaisQuery`.
  - Calls Ubikais JSON endpoints for departure and arrival records.
  - Handles pagination using `limit`/`offset`.
  - Stores and reads JSON cache files under `cache/`.
  - Cache TTL depends on whether the queried date is today, tomorrow, future, or past after a KST cutoff.
  - Supports fetching and merging multiple airline codes with `fetch_records_for_airlines`.

- `preview_ubikais.py`
  - CLI utility for producing a PNG preview from Ubikais data.
  - Supports date, airline, airport, flight number, timeline settings, cache refresh, and output directory options.
  - Saves files under `preview_output/` by default.

- `airport_codes.py`
  - Generated mapping from OurAirports `airports.csv`.
  - Provides `icao_to_iata(code)`.
  - 확인 필요: source generation script is not present in the current file list.

## Implemented Features - Current Estimate

Based on selected code reads, the app appears to implement:

- Flight handling timeline for departures and arrivals.
- Date navigation with previous/today/next controls.
- Airline filtering with predefined airlines and custom 3-letter airline codes.
- Airport selection for Korean airport codes such as RKSI/RKSS/RKJB/RKNY/RKPS/RKPU/RKTL/RKTU.
- Aircraft type filtering derived from loaded records.
- Configurable time basis:
  - Ground ops: block on/off priority.
  - Flight ops: ATA/ATD priority.
- Configurable service-day start hour.
- Configurable overlap interval of 10, 20, or 30 minutes.
- Configurable handling-time windows before/after departure and arrival.
- Optional labels on bars: flight number, DES/ORG, registration, spot, memo.
- Optional turn-around link display based on registration or spot and a configurable limit.
- Memo assignment UI for visible flights, stored in Streamlit session state.
- PNG download from the current figure.
- Flight schedule comparison between one base date and one comparison date.
- Flight schedule lookup over a date range up to 31 days, including operation calendar, actual time distribution, and detail table.
- Raw departure/arrival data preview.
- Local CLI preview generation through `preview_ubikais.py`.

확인 필요:

- Whether `before_app.py` is the intended production Streamlit entrypoint or a renamed/backup file.
- Whether Ubikais endpoints currently work without a cookie, or whether `UBIKAIS_COOKIE` / Streamlit secrets are required in real use.
- Whether Korean help text displays correctly in the browser. PowerShell `Get-Content` displayed some Korean text as mojibake, while `rg` and `py_compile` did not indicate a syntax problem.
- Whether `_date_block.txt` is still used by the workflow.

## Recent Change - Schedule Comparison

Added in this session:

- `before_app.py` now includes a collapsed `Flight schedule comparison` expander near `Flight schedule lookup`.
- Users can select:
  - Base date.
  - Comparison date.
- Comparison always includes both departures and arrivals.
- Comparison key is direction + flight number.
- Duplicate records with the same comparison key are treated as the same flight; the first sorted representative row is shown.
- The comparison reuses existing Ubikais fetch/cache and service-day filtering logic.
- Applied filters/settings:
  - Selected airlines.
  - Selected airport.
  - Current time basis.
  - Current service-day start hour.
- Aircraft type filter is intentionally ignored for comparison.
- Result UI shows base count, comparison count, added count, missing count, then added/missing tables.
- Comparison result tables now show only `Type`, `Flight`, `STD/STA`, and `ORG/DES`.
- `ORG/DES` uses the same ICAO-to-IATA 3-letter airport code conversion as the main chart labels.
- Comparison result rows are sorted by `Flight`, then `ARR` before `DEP`, then scheduled time.

Files changed:

- `before_app.py`
- `HANDOFF.md`

## Git Status And Diff

Before creating this handoff:

- `git status --short` produced no output.
- `git diff --stat` produced no output.
- `git diff --name-status` produced no output.
- `git ls-files --others --exclude-standard` produced no output.

Interpretation:

- The tracked working tree was clean before `HANDOFF.md` was added.
- Ignored directories such as `cache/`, `preview_output/`, and `__pycache__/` exist but are excluded by `.gitignore`.

After this handoff:

- `HANDOFF.md` is expected to appear as an untracked file unless it is added to Git.

## Verification Performed

- Ran `python -m py_compile flight_timeline.py ubikais_client.py preview_ubikais.py before_app.py airport_codes.py`.
- Result: no compiler output, so the checked Python files parsed successfully.
- After adding schedule comparison, ran `python -m py_compile before_app.py`.
- Result: no compiler output.

## Suggested Next Steps

- Decide whether `before_app.py` should remain the app entrypoint or be renamed/copied to a conventional Streamlit entrypoint.
- Run the Streamlit app manually and verify UI rendering, especially Korean help text and date-navigation buttons.
- If continuing feature work, make minimal edits around the relevant function/UI section instead of restructuring the app.
- If changing Ubikais fetch behavior, preserve existing cache semantics unless there is a specific bug to fix.
