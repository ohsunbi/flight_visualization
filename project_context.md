# Flight Visualization 프로젝트 컨텍스트

최종 갱신: 2026-07-14  
현재 기준 커밋: `15ab9e0` (`2026_07_13_changed18`)

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

## 앱 데이터 흐름

1. 사용자가 날짜, 항공사, 공항과 필터를 선택한다.
2. `before_app.py`가 `UbikaisQuery`를 구성한다.
3. `ubikais_client.py`가 캐시 또는 UBIKAIS API에서 출발·도착 레코드를 가져온다.
4. 서비스 시작 시각이 0시가 아니면 다음 날짜 자료도 함께 가져와 서비스 데이 범위로 필터링한다.
5. `departures_from_ubikais()`와 `arrivals_from_ubikais()`가 표준 DataFrame을 만든다.
6. 기종 필터와 Memo assignment를 적용한다.
7. `build_timeline_figure()`가 Matplotlib Figure와 summary를 반환한다.
8. Streamlit에서 차트를 표시하고 PNG/PDF 다운로드 데이터를 생성한다.

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

### 2026-07-14

- `project_context.md`를 현재 기준 인수인계 문서로 추가.
- 중요한 구조·운영·의존성 변경 시 이 문서를 갱신하는 규칙 수립.

### 2026-07-13

- PyArrow/NumPy 최신 자동 설치로 발생한 Segmentation fault 조사 및 해결.
- PyArrow 23.0.1, NumPy 2.4.2 고정.
- Python 3.12.13 기준 `pyproject.toml`, `uv.lock`, `.python-version` 추가.
- Memo UI를 기존 `st.data_editor()` 방식으로 복원.
- Matplotlib 객체 Figure, Agg backend, 렌더링 lock과 정리 로직 유지.
