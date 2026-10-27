# Flight Visualization 프로젝트 컨텍스트

최종 갱신: 2026-10-18
확인한 기준 커밋: `b5a509a`. 아래 시간대별 조업 편수 기능은 이 커밋 이후 작업이며 아직 커밋하지 않았다.

## 문서 목적

이 문서는 `flight_visualization` Streamlit 웹앱의 현재 구조, 운영 환경, 핵심 기능, 중요한 기술 결정과 장애 이력을 다음 작업자에게 전달하기 위한 기준 문서다.

새 대화나 작업을 시작할 때는 먼저 이 문서와 현재 Git 상태를 확인한다. 과거의 `HANDOFF.md`는 2026-06-03 시점의 참고 기록이며, 현재 상태에 대해서는 이 문서를 우선한다.

## 작업 원칙

- 기존 기능과 UI를 가능한 한 유지한다.
- 원인이 확인되지 않은 상태에서 여러 영역을 동시에 수정하지 않는다.
- 사용자가 분석만 요청하면 코드를 변경하지 않는다.
- 코드 변경을 요청받았을 때도 관련 파일과 데이터 흐름을 먼저 확인한다.
- 기존 사용자 변경과 미커밋 파일을 임의로 덮어쓰거나 삭제하지 않는다.
- 운영 장애는 Python 예외와 네이티브 프로세스 종료를 구분해 분석한다.
- 패키지 문제를 조사할 때는 로컬 버전이 아니라 Streamlit Cloud 로그의 실제 버전을 기준으로 판단한다.
- 배포 의존성은 `pyproject.toml`과 `uv.lock`을 기준으로 관리한다.
- 패키지 버전을 변경할 때는 코드 변경과 같은 커밋에 섞지 않는 것을 원칙으로 한다.
- 중요한 구조·운영·의존성 변경이 있으면 이 문서를 같은 작업에서 갱신한다.

## 문서 갱신 기준

다음 변경은 반드시 `project_context.md`에 반영한다.

- 앱 진입점, 주요 모듈 역할 또는 데이터 흐름 변경
- Streamlit Cloud의 Python 버전 변경
- Streamlit, Pandas, PyArrow, NumPy, Matplotlib 버전 변경
- `pyproject.toml` 또는 `uv.lock` 관리 방식 변경
- 외부 API, 캐시 정책, 서비스 데이 계산 방식 변경
- 주요 세션 상태 key 또는 Memo 저장 방식 변경
- 타임라인 생성·다운로드 방식 변경
- 운영 장애의 원인과 해결 방법이 새로 확정된 경우
- 배포 절차나 필수 환경 설정 변경

다음 변경은 보통 이 문서까지 갱신하지 않아도 된다.

- 단순 문구, 색상, 여백 수정
- 기능이나 데이터 계약에 영향이 없는 작은 UI 보정
- 내부 구현에 영향을 주지 않는 주석 또는 포맷 변경

## 프로젝트 위치와 진입점

- 로컬 경로: `C:\alive_coding\flight_visualization`
- Git 브랜치: `main`
- Streamlit 앱 진입점: `before_app.py`
- Streamlit Cloud 실행 경로: `/mount/src/flight_visualization/before_app.py`

## 주요 파일

- `before_app.py`
  - Streamlit UI와 앱 전체 실행 흐름
  - URL query parameter 동기화
  - 항공사·공항·기종·날짜·타임라인 설정 관리
  - Memo 편집, 다운로드, 스케줄 비교, 운항 조회, 원본 데이터 미리보기
- `flight_timeline.py`
  - UBIKAIS 출발·도착 레코드를 타임라인용 DataFrame으로 변환
  - `TimelineConfig` 정의
  - Matplotlib 타임라인 Figure 생성
  - 중첩 수치, 행 배치, turn-around 연결, Memo badge 처리
- `flight_excel.py`
  - 수동 스케줄 `.xlsx` 읽기·검증, 양식 생성, 서비스 날짜 분류와 차트 DataFrame 변환
- `flight_excel_ui.py`
  - UBIKAIS와 분리된 엑셀 입력 화면, 날짜별 차트 및 PNG/PDF 다운로드
- `flight_assignments.py`
  - 기존 UBIKAIS 운항편의 조 배정 엑셀 읽기·내보내기. 수동 스케줄 입력과 별개
- `test_flight_excel.py`
  - 수동 스케줄 검증·서비스 날짜 경계·차트 및 Streamlit 모드 분리 테스트
- `flight_workload.py` / `flight_workload_ui.py`
  - 현재 차트의 조업 구간에 대한 시간 범위 집계 및 두 모드 공통 UI
- `test_flight_workload.py`
  - 경계·자정·설정 변경 초기화·모드 연결과 집계 UI 위치 테스트
- `ubikais_client.py`
  - UBIKAIS 출발·도착 JSON API 호출
  - pagination 처리
  - 다중 항공사 결과 병합
  - 날짜 조건별 JSON 캐시 관리
- `preview_ubikais.py`
  - Streamlit 없이 타임라인 PNG를 생성하는 CLI 도구
- `airport_codes.py`
  - ICAO 공항 코드를 IATA 코드로 변환하는 생성 데이터 파일
- `requirements.txt`
  - `uv.lock`을 사용하지 못하는 환경을 위한 fallback 의존성 목록
- `pyproject.toml`
  - 직접 의존성과 지원 Python 범위의 기준 파일
- `uv.lock`
  - Streamlit Cloud에 설치할 전체 하위 의존성 고정 파일
- `.python-version`
  - 개발·lock 생성 기준 Python 버전
- `cache/`
  - UBIKAIS 응답 JSON 캐시. Git에서 제외됨
- `preview_output/`
  - CLI preview 이미지 출력. Git에서 제외됨
- `HANDOFF.md`
  - 2026-06-03 기준의 과거 인수인계 문서. 현재 기준 문서는 아님

## 현재 배포 환경

Python과 주요 네이티브 패키지는 다음 버전을 기준으로 한다.

```text
Python       3.12.13
Streamlit    1.58.0
Pandas       2.3.3
PyArrow      23.0.1
NumPy        2.4.2
Matplotlib   3.10.8
openpyxl     3.1.5
```

`pyproject.toml`의 Python 범위:

```toml
requires-python = ">=3.12,<3.13"
```

주의사항:

- Streamlit Cloud에서는 `uv.lock`이 `requirements.txt`보다 우선한다.
- 의존성 변경은 `requirements.txt`만 수정해서는 안 된다.
- 직접 의존성은 `pyproject.toml`에서 변경하고 Python 3.12.13 기준으로 `uv.lock`을 다시 생성한다.
- `requirements.txt`는 fallback이므로 핵심 직접 의존성 버전을 `pyproject.toml`과 일치시킨다.

## 의존성 변경 절차

1. 별도 브랜치에서 `pyproject.toml`을 수정한다.
2. Python 3.12.13 기준으로 lock을 갱신한다.

```powershell
uv lock --python 3.12.13
```

3. 설치 상태를 검증한다.

```powershell
uv sync --locked --python 3.12.13
```

4. PyArrow DataFrame 변환, Streamlit 위젯 재실행, PNG/PDF 다운로드를 확인한다.
5. `pyproject.toml`, `uv.lock`, fallback인 `requirements.txt`를 함께 커밋한다.
6. Cloud 테스트 배포 후 운영에 반영한다.

특정 패키지를 의도적으로 업데이트할 때:

```powershell
uv lock --upgrade-package pyarrow
```

운영 브랜치에서 검증 없이 전체 패키지를 최신 버전으로 올리지 않는다.

## 앱 데이터 흐름 (UBIKAIS 모드)

1. 사용자가 날짜, 항공사, 공항과 필터를 선택한다.
2. `before_app.py`가 `UbikaisQuery`를 구성한다.
3. `ubikais_client.py`가 캐시 또는 UBIKAIS API에서 출발·도착 레코드를 가져온다.
4. 서비스 시작 시각이 0시가 아니면 다음 날짜 자료도 함께 가져와 서비스 데이 범위로 필터링한다.
5. `departures_from_ubikais()`와 `arrivals_from_ubikais()`가 표준 DataFrame을 만든다.
6. 기종 필터와 Memo assignment를 적용한다.
7. `build_timeline_figure()`가 Matplotlib Figure와 summary를 반환한다.
8. Streamlit에서 차트를 표시하고 PNG/PDF 다운로드 데이터를 생성한다.

## 엑셀 스케줄 모드 (2026-10-18)

- `before_app.py`의 자료 입력 방식 기본값은 UBIKAIS다. 엑셀 선택 시 URL 적용·API 조회·기종 필터·조 배정 실행 전에 `render_excel_mode()`로 분기한다.
- 출발·도착은 각각 별도 `.xlsx` 파일이며 한쪽만 입력해도 된다. 각 파일의 첫 번째 시트를 읽는다.
- 출발 열: `날짜 / 항공편명 / STD / 출발지 / 도착지`.
- 도착 열: `날짜 / 항공편명 / STA / 출발지 / 도착지`.
- 앞의 세 열은 필수다. 출발지·도착지는 열 자체가 없거나 값이 비어 있어도 허용하며, 입력할 때는 IATA 영문 3자리 코드(예: ICN)를 사용한다. UBIKAIS의 ICAO 입력 계약은 그대로다.
- 날짜는 실제 달력 날짜, 시간은 한 기준 공항의 현지시간이다. 별도 시차 변환은 하지 않는다. 날짜는 Excel 날짜 또는 YYYY-MM-DD, YYYY/MM/DD, YYYYMMDD를 지원한다. 시간은 Excel 시간, HH:MM, HHMM을 지원하며 분 단위로 검증한다.
- 실제 날짜·시간을 `SCHEDULED_AT`으로 결합한다. `service_dates()`는 여기서 서비스 시작 시각을 빼 서비스 날짜를 구하며, `timeline_frame()`은 `[선택 날짜+시작 시각, 다음 날+시작 시각)`의 항공편만 차트로 전달한다.
- 시작 시각 기본값은 0시이며, 2시로 설정하면 12월 3일 01:00 항공편은 12월 2일 서비스 차트에 포함된다. 실제 항공편 날짜는 변경하지 않는다.
- 두 파일에서 계산한 서비스 날짜의 최솟값~최댓값 범위를 달력으로 제공하며 하루씩 표시한다. 화면 용어는 `표시 날짜`, `하루 시작 시각`, `표시 범위`를 사용한다. 범위 안에서 항공편이 없는 날짜는 선택을 유지하고 안내만 표시하며 차트·PNG/PDF는 생성하지 않는다. 다음 날짜 자료가 파일에 없으면 API로 보충하지 않는다. 작업 구간은 선택된 항공편의 전후 작업시간에 따라 서비스 범위를 넘어갈 수 있다.
- `TimelineConfig.use_actual_schedule_dates=True`일 때만 차트가 `SCHEDULED_AT`을 그대로 사용한다. 기본값 False인 기존 UBIKAIS/CLI의 시간 fallback·새벽 이월 방식은 유지한다.
- 엑셀 모드는 STD/STA 기준이며, 양방향 공항 정보는 미리보기에 보존한다. DES/ORG 라벨에는 출발편 도착지·도착편 출발지를 사용한다. 조 배정, 등록기호/SPOT, Turn-around, 기종 필터, API 비교·운항 조회는 제공하지 않는다.
- `excel_` 접두사로 UI 상태를 분리한다. UBIKAIS 날짜·설정 위젯은 숨겨져도 값이 정리되지 않도록 보존하며, 기존 조 배정 딕셔너리와 API payload에는 엑셀 데이터를 넣지 않는다.
- 파일은 디스크에 저장하지 않는다. 내용과 방향 기준의 읽기 결과만 `st.cache_data(max_entries=32)`로 메모리에 캐시한다. 파일 교체·제거 시 현재 업로더 내용으로 다시 판단한다. 다른 모드로 이동하면 업로더가 정리될 수 있어 재업로드가 필요하다. 영구 저장 기능은 없다.
- 오류는 파일·시트·행 번호로 안내하고 해당 업로드의 오류가 해결될 때까지 전체 차트 생성을 중단한다. 빈 행은 무시하며 완전 중복은 경고하고 그대로 유지한다. IATA 코드는 3자리 형식만 검증하며 실제 공항 존재 여부를 외부 조회하지 않는다.
- PNG/PDF는 기존 Figure 생성기와 렌더링 잠금을 재사용한다. 빈 방향에서도 차트 준비 열을 생성하도록 보완했다.
- 추가 패키지·lock 변경 없이 기존 openpyxl 3.1.5를 사용한다.

검증 명령:

```powershell
.venv\Scripts\python.exe -m unittest test_flight_excel -v
.venv\Scripts\python.exe -m py_compile before_app.py flight_timeline.py flight_excel.py flight_excel_ui.py test_flight_excel.py
```

테스트는 UBIKAIS 응답과 파일 업로더를 대체해 실행한다. 실제 API 통신, 브라우저 파일 선택 및 Cloud 배포는 별도 확인이 필요하다.

## 차트 아래 최대 동시 조업 수

- 각 표시 시각을 중심으로 `TimelineConfig.interval_min` 길이의 구간에서 최대 동시 조업 수를 계산한다. 30분 설정의 09:00 표시는 08:45~09:15가 기준이다.
- 검정색은 출발·도착 조업 구간을 합친 실제 최대 동시 조업 수다. 빨간색과 파란색은 각각 출발과 도착의 독립적인 최대값이므로, 두 값을 더한 결과가 검정색과 다를 수 있다.
- `flight_timeline.py`의 `_max_overlaps_in_window()`를 사용하며, 경계에 닿기만 하는 조업과 길이 0인 구간은 제외한다. 화면과 PNG/PDF, UBIKAIS와 엑셀 모드에 공통 적용된다.
- 아래 시간대별 조업 편수 기능은 구간에 겹친 전체 조업 건수를 세므로 최대 동시 조업 수와 구분한다.

## 시간대별 조업 편수

- UBIKAIS에서는 `Flight schedule comparison` 바로 위, 엑셀에서는 PNG/PDF 다운로드 버튼 바로 아래에 공통 집계 UI를 표시한다.
- 집계 기능은 기본적으로 접힌 펼침 영역에 둔다. 시작·종료 각각 시(00~23)와 분(00/10/20/30/40/50)을 따로 선택하며 기본값은 07:00~09:00이다. 선택 위젯과 계산 버튼을 `st.form`으로 묶어 선택 중에는 서버 재실행을 일으키지 않고, 계산 버튼으로 한 번에 적용한다. 제출 전에는 이전 결과와 실제 집계 범위를 유지한다. 시작·종료가 같으면 오류를 안내하고, 계산 결과는 기존 HTML 카드 스타일로 크게 표시한다.
- UBIKAIS 집계 UI는 `Handling count by time range`이며 입력·버튼·안내·오류·결과·상세 표 모두 영어다. 엑셀의 집계 UI는 한국어를 유지한다. 사이드바 입력 방식은 `Airlines`와 같은 subheader 크기의 `Data source` 제목과 가로 라디오(`UBIKAIS` / `Excel`)를 사용한다. 모드의 내부 값과 key는 기존 세션 호환성을 위해 유지한다.
- 대상은 현재 차트 생성 결과의 `summary["dep_records"]` / `summary["arr_records"]`다. 다른 날짜나 필터로 제외된 항공편을 추가 조회하지 않는다. 등록기호 기준 항공기 대수가 아니라 출발·도착 조업 건수를 센다.
- 집계 조건은 `조업 시작 < 조회 종료` AND `조업 종료 > 조회 시작`이며, 양의 조업 길이가 있어야 한다. 경계에 닿기만 하는 조업과 길이 0인 막대는 제외한다. 기존 중첩 숫자(최대 동시 조업 수)를 합산하는 방식이 아니다.
- 한 차트 행은 한 조업으로 한 번 센다. 같은 편명의 별도 행은 합치지 않는다. Turn-around로 연결되어도 출발·도착은 각각 센다. 차트의 handling 설정 및 F편 특수 작업시간을 그대로 따른다.
- 시각은 현재 표시 날짜를 기준으로 해석한다. 시작 시각이 하루 시작 시각보다 이르면 다음 달력 날짜에 대응한다. 종료 시각이 시작 시각보다 이르면 시작 날짜의 다음 날로 계산하며, 같으면 오류를 안내한다. 예: 하루 시작 02:00인 12월 2일 차트에서 00:00~01:00은 12월 3일 새벽이고, 23:00~01:00은 12월 2일 밤~12월 3일 새벽이다.
- 실제 집계 시작·종료 날짜·시간을 결과 위에 명시한다. 조회 구간이 차트 날짜 범위를 넘어도 현재 차트의 조업만 대상으로 하며, 인접 날짜 항공편을 자동 보충하지 않는다.
- 상세 펼침에는 방향·편명·출도착지·실제 조업 시작/종료 날짜·시간을 표시한다. 출도착지는 기존 공항 코드 변환기로 IATA 표시하며, 출발은 목적지, 도착은 출발지를 뜻한다. 빈 결과도 0편으로 표시한다.
- `excel_workload_*` / `ubikais_workload_*` 세션 key로 모드 상태를 분리한다. 시·분 선택은 `_workload_start_hour` / `_workload_start_minute` / `_workload_end_hour` / `_workload_end_minute` key를 사용해 과거 time_input·텍스트 입력 상태와 충돌하지 않는다. 날짜·하루 시작 시각·필터·chart config·대상 레코드·제출된 조회 시각·언어의 signature가 달라지면 결과를 초기화하며 재계산이 필요하다. 추가 API 호출이나 파일 저장은 없다.
- 차트와 PNG/PDF 이미지 자체에는 집계 결과를 삽입하지 않는다. 의존성 및 lock 파일 변경은 없다.

검증 명령:

```powershell
.venv\Scripts\python.exe -m unittest test_flight_workload test_flight_excel -v
.venv\Scripts\python.exe -m py_compile before_app.py flight_excel_ui.py flight_workload.py flight_workload_ui.py test_flight_workload.py
```

## 핵심 기능

- 출발·도착 handling timeline
- 이전 날짜·오늘·다음 날짜 이동
- 복수 항공사와 사용자 지정 3-letter 항공사 코드
- 국내 공항 선택
- 운항 자료에서 추출한 기종 필터
- Ground ops / Flight ops 시간 기준
- 서비스 데이 시작 시각 설정
- 출발·도착 handling window 설정
- 중첩 계산 간격 설정
- FLT, DES/ORG, REG, SPOT, Memo label 설정
- 항공기 turn-around 연결 표시
- 편명별 Memo 편집
- 현재 차트 PNG/PDF 다운로드
- 두 날짜의 운항 스케줄 비교
- 날짜 범위 운항편 조회 및 실제 시각 분포 차트
- 출발·도착 원본 DataFrame 미리보기

## Memo 처리

- Memo는 `st.session_state.team_assignments`에 저장된다.
- 영구 DB 저장이 아니라 현재 Streamlit 세션 범위다.
- `TEAM_KEY`는 날짜, 방향, flight PK 또는 편명·노선·시간·등록기호·spot 정보를 이용해 생성한다.
- 같은 표시 편명의 관련 출발·도착 record는 `TEAM_KEYS` 목록으로 묶을 수 있다.
- 여러 편명은 기존 `st.data_editor()` UI로 편집한다.
- 한 편만 필터링되면 `st.text_input()`을 사용한다.
- Memo 변경 시 출발·도착 DataFrame에 assignment를 다시 연결하고 차트를 다시 생성한다.

## Matplotlib 처리 방식

현재 타임라인은 pyplot 전역 Figure 대신 `matplotlib.figure.Figure` 객체를 직접 생성한다.

유지 중인 안전 처리:

- 서버 렌더링 backend를 `Agg`로 명시
- 모듈 수준 `RLock`으로 Figure 생성과 PNG/PDF 렌더링을 직렬화
- Memo 변경으로 Figure를 다시 만들기 전에 기존 Figure 정리
- 렌더링 완료 또는 예외 발생 시 `fig.clear()` 실행

이 변경은 2026-07-13 PyArrow 장애의 직접 해결책은 아니지만, 조사 과정에서 확인한 pyplot Figure 누적과 동시 렌더링 위험을 줄이기 위해 유지한다.

잠재적인 trade-off:

- 여러 사용자가 동시에 그래프를 생성하면 잠금 때문에 순차 처리된다.
- 400 DPI PNG와 PDF 생성 시간 동안 다른 렌더링이 기다릴 수 있다.
- 현재 앱은 소수 사용자 중심이므로 안정성 이점이 더 크다고 판단했다.

## 2026-07-13 Segmentation fault 장애

### 증상

- 첫 화면 일부가 정상 표시된 후 Streamlit 프로세스가 종료됨
- 위젯 조작 시 발생하는 것처럼 보였음
- 한 번 종료되면 브라우저 새로고침으로 앱이 다시 열리지 않음
- stack trace가 `pyarrow/pandas_compat.py`의 `convert_column`을 가리킴
- 처음에는 `st.data_editor()`, 이후에는 일반 `st.dataframe()`에서 동일하게 재현됨

### 확정 원인

당시 `requirements.txt`에서 PyArrow와 NumPy 버전이 고정되지 않았다. Cloud 재빌드에서 `uv`가 다음 최신 네이티브 패키지를 선택했다.

```text
PyArrow 25.0.0
NumPy   2.5.1
```

서로 다른 DataFrame이 모두 같은 PyArrow 네이티브 변환에서 Segmentation fault를 일으켰기 때문에 특정 DataFrame 구조나 Memo UI 문제가 아닌 배포 바이너리 조합 문제로 판단했다.

Streamlit은 실행 중 UI delta를 순차 전송하므로 스크립트가 끝나기 전에 첫 화면이 보일 수 있다. 이후 하단의 접힌 expander 내부 `st.dataframe()`도 서버에서 실행되며, 이 단계에서 프로세스가 종료될 수 있었다.

Segmentation fault는 일반 Python 예외가 아니라 프로세스 전체를 종료한다. Uvicorn과 WebSocket 서버도 함께 사라지므로 Cloud가 프로세스를 다시 시작하거나 Reboot하기 전까지 앱이 열리지 않았다.

### 최종 해결

- `pyarrow==23.0.1` 고정
- `numpy==2.4.2` 고정
- Python 3.12.13 기준 `uv.lock` 생성
- 직접 의존성과 전체 하위 의존성 재현 가능하게 관리
- 임시로 교체했던 Memo UI는 기존 `st.data_editor()`로 복원
- 진단용 `faulthandler`와 버전 출력 제거

### 수행한 검증

- 실제 캐시 기반 출발·도착 DataFrame Arrow 변환 반복
- FLT/Memo DataFrame Arrow 변환 20,000회
- Python 3.12.13 격리 환경에서 고정 패키지 설치
- 격리 환경 Arrow 변환 1,000회
- Python 파일 `py_compile`

## 캐시와 외부 API

- 데이터 원본은 UBIKAIS 출발·도착 JSON endpoint다.
- cache key에는 날짜, 방향, 항공사, 출발·도착 공항, 편명 조건이 반영된다.
- cache TTL은 조회 날짜가 과거·현재·미래인지와 KST 기준 시각에 따라 달라진다.
- `Refresh` 요청은 일반 cache 사용을 건너뛰고 데이터를 다시 가져온다.
- `ubikais_client.py`는 선택적 `cookie_header` 인자를 지원하지만, 현재 `before_app.py`의 기본 호출은 cookie를 전달하지 않는다.
- 향후 API 인증이 필요해지면 secrets 연동을 별도로 구현해야 하며, 현재 코드에 없는 `UBIKAIS_COOKIE` 연동을 이미 존재하는 것으로 가정하지 않는다.
- `cache/` 파일은 운영 데이터이며 Git에 포함하지 않는다.

## 배포 및 장애 확인

일반 배포:

1. 로컬 문법 검사와 관련 기능 테스트
2. Git commit 및 push
3. Streamlit Cloud dependency 처리 로그 확인
4. 첫 화면 표시만 보지 말고 전체 스크립트가 종료 없이 유지되는지 확인
5. 날짜·필터·Memo를 조작해 rerun 확인
6. PNG/PDF 다운로드 확인

Segmentation fault 조사 시 필요한 로그:

- Python 버전
- Streamlit, Pandas, PyArrow, NumPy, Matplotlib 버전
- `Fatal Python error` 이후 전체 thread stack
- `/app/scripts/run-streamlit.sh` 종료 코드
- 충돌한 `before_app.py` 행 번호

## 기본 테스트 항목

- 앱 최초 로드와 재실행
- 날짜 이전/오늘/다음 이동
- 항공사 및 공항 변경
- 기종 선택 적용
- Ground/Flight 시간 기준 변경
- Memo 입력·수정·삭제
- FLT Memo 필터
- turn-around 표시
- PNG/PDF 다운로드
- 스케줄 비교의 added/missing 결과
- 날짜 범위 운항 조회
- Raw data preview
- 여러 번 연속 위젯 조작 후 프로세스 안정성

## 현재 알려진 제약과 주의사항

- Memo는 세션 상태이므로 앱 재시작이나 세션 종료 후 유지되지 않는다.
- 400 DPI PNG와 PDF를 매 rerun마다 생성하므로 렌더링 비용이 크다.
- 전역 Matplotlib 잠금 때문에 다중 사용자의 동시 렌더링은 순차 처리된다.
- `before_app.py` 파일명이 일반적인 `app.py`는 아니지만 현재 배포 진입점이므로 임의로 변경하지 않는다.
- `airport_codes.py`는 큰 생성 파일이며, 명확한 요청 없이 전체 재생성하지 않는다.
- 콘솔에서 한글이 깨져 보여도 파일 인코딩과 브라우저 표시를 별도로 확인한다.

## 다음 작업 시작 체크리스트

1. `project_context.md`를 읽는다.
2. `git status --short`로 사용자 미커밋 변경을 확인한다.
3. `git log -5 --oneline`으로 최근 작업을 확인한다.
4. 요청과 관련된 파일·함수만 먼저 읽는다.
5. 변경 전 기존 UI와 데이터 흐름에 미칠 영향을 설명한다.
6. 수정 후 최소한 `py_compile`과 관련 경로 테스트를 실행한다.
7. 구조·운영·의존성에 중요한 변화가 있으면 이 문서를 갱신한다.
8. 최종 응답에서 변경 파일, 영향, 테스트 결과와 배포 필요 여부를 설명한다.

## 최근 중요 변경 요약

### 2026-10-18

- 수동 엑셀 스케줄 모드, 날짜별 차트와 PNG/PDF 다운로드 추가.
- 실제 날짜를 보존하면서 서비스 데이 범위로 분류하는 데이터 경로 추가.
- 기본 차트의 빈 출발/도착 방향 처리 보완 및 회귀 테스트 추가.

### 2026-09-06 (현재 코드 확인으로 보충)

- `f99c3bc`에서 조 배정 UI와 `flight_assignments.py` 추가.
- 조 배정 엑셀 가져오기·내보내기를 위해 openpyxl 3.1.5를 직접 의존성과 lock에 추가.
- `.python-version`은 8월 변경으로 현재 `3.12`이며 패치 버전을 고정하지 않는다. Dev Container는 Python 3.11 이미지여서 pyproject의 3.12 요구와 불일치한다. 이번 엑셀 기능에서 환경 파일은 변경하지 않았다.

### 2026-07-14

- `project_context.md`를 현재 기준 인수인계 문서로 추가.
- 중요한 구조·운영·의존성 변경 시 이 문서를 갱신하는 규칙 수립.

### 2026-07-13

- PyArrow/NumPy 최신 자동 설치로 발생한 Segmentation fault 조사 및 해결.
- PyArrow 23.0.1, NumPy 2.4.2 고정.
- Python 3.12.13 기준 `pyproject.toml`, `uv.lock`, `.python-version` 추가.
- Memo UI를 기존 `st.data_editor()` 방식으로 복원.
- Matplotlib 객체 Figure, Agg backend, 렌더링 lock과 정리 로직 유지.
