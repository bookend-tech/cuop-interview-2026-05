# c번 과제 실행 안내: Live Server 설치

c번 과제(`c_react_state_update.html`)는 브라우저에서 실행하며 확인하는 문제입니다. GitHub Codespaces에서 HTML 파일을 바로 열면 일부 스크립트가 정상적으로 동작하지 않을 수 있으므로, VS Code 확장 프로그램인 **Live Server**를 설치한 뒤 실행하세요.

## 1. Live Server 설치

1. Codespaces 왼쪽 사이드바에서 **확장: 마켓플레이스** 아이콘을 클릭합니다.
2. 검색창에 `live server`를 입력합니다.
3. 목록에서 **Live Server** 확장을 찾습니다.
   - 확장 이름: `Live Server`
   - 게시자: `Ritwick Dey`
4. **설치** 버튼을 클릭합니다.

이미 설치되어 있다면 설치 버튼 대신 설정 아이콘이 보입니다.

## 2. c번 과제 실행

1. 파일 목록에서 `c_react_state_update.html`을 엽니다.
2. VS Code 하단 상태바의 **Go Live** 버튼을 클릭합니다.
3. 새 브라우저 탭 또는 미리보기 창에서 c번 과제 화면이 열립니다.
4. 화면의 안내에 따라 `TODO` 영역을 수정합니다.
5. 수정 후 브라우저를 새로고침해서 `PASS`가 유지되는지 확인합니다.

## 3. 확인할 동작

c번 과제 화면에서 아래 버튼들을 눌러 확인하세요.

1. `1 증가`: 실제 count와 기대 count가 각각 1씩 증가해야 합니다.
2. `두 번 증가`: 버튼을 한 번 눌렀을 때 실제 count가 2 증가해야 합니다.
3. `비동기 증가 예약`: 예약 후 다른 버튼을 눌러도 최신 count를 기준으로 1 증가해야 합니다.

모든 동작에서 화면 오른쪽 상단의 상태가 `PASS`로 유지되면 됩니다.

## 4. Go Live 버튼이 보이지 않을 때

1. Live Server가 설치되어 있는지 다시 확인합니다.
2. `c_react_state_update.html` 파일이 열린 상태인지 확인합니다.
3. VS Code 창을 새로고침하거나 Codespaces를 다시 연결합니다.
4. 그래도 보이지 않으면 명령 팔레트에서 `Live Server: Open with Live Server`를 실행합니다.
