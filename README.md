# sts-todays-lunch

성남테크노과학고등학교 홈페이지의 급식 정보를 웹 크롤링하여 오늘의 급식 정보를 출력하는 프로그램입니다. 2023년 고등학교 2학년이었을 당시 개발하였습니다.

---

## 개요
- **개발 기간:** 2023년 12월 11일
- **개발 언어:** Python
- **개발 환경:** Visual Studio Code

---

## 실행 화면
<img width="351" alt="image" src="https://github.com/user-attachments/assets/236133b7-6442-4923-9b67-e74167b8abe8" />

---

## 구현
- **웹 데이터 파싱:** `requests`와 `BeautifulSoup`를 사용하여 학교 홈페이지의 급식 정보를 추출함
- **정규 표현식을 통한 전처리 파이프라인:** 알레르기 정보 등 불필요한 정보를 제거하고 메뉴명만 순수하게 남김으로써 가독성을 높임
- **PyQt5 기반 커스텀 GUI 위젯 디자인:** 바탕화면 가젯 느낌을 주기 위해 윈도우 타이틀바를 제거(`Qt.FramelessWindowHint`)하고, CSS 스타일시트를 적용해 깔끔한 UI를 구현함
- **마우스 이벤트 오버라이딩:** 타이틀바가 없어 창을 이동할 수 없는 한계를 해결하기 위해, 마우스 클릭 및 이동 이벤트(`mouseMoveEvent`)를 오버라이딩하여 좌표 변위 계산을 통한 커스텀 창 드래그 기능 직접 구현.

---

## 실행 방법
1. 저장소 클론: `git clone https://github.com/hellotomato12/sts-todays-lunch.git`
2. 필수 패키지 설치:
  `pip install PyQt5 requests bs4`
4. 프로그램 실행:
   * 윈도우 환경에서 `main.pyw` 파일을 **더블 클릭**하여 바로 실행하거나,
   * 터미널에서 `python main.pyw` (또는 `pythonw main.pyw`)를 입력하여 실행합니다.
