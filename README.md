# Flask 웹 애플리케이션 - 컴퓨터 이름 표시 기능

## 프로젝트 개요
Flask를 사용하여 컴퓨터 이름(호스트네임)을 표시하는 웹 애플리케이션입니다.

## 프로젝트 구조
```
/home/ittae.com/dev/david/
├── app.py                 # Flask 메인 애플리케이션
├── requirements.txt       # Python 의존성 패키지 목록
├── templates/
│   ├── index.html        # 홈 페이지 템플릿
│   └── menu.html         # 메뉴 페이지 템플릿
├── .venv/                # Python 가상환경
├── .vscode/
│   └── settings.json     # VS Code 설정
└── README.md             # 프로젝트 문서
```

## 환경 설정

### 1. Python 가상환경 설정
```bash
# 가상환경 생성 (이미 생성되어 있음)
python3 -m venv .venv

# 가상환경 활성화
source .venv/bin/activate

# 가상환경 비활성화 (필요시)
deactivate
```

### 2. 의존성 패키지 설치
```bash
# requirements.txt로 모든 의존성 설치 (권장)
pip install -r requirements.txt

# 또는 Flask만 개별 설치
pip install flask
```

#### requirements.txt 생성 방법
```bash
# 현재 환경의 패키지 목록을 requirements.txt로 저장
pip freeze > requirements.txt
```

### 3. VS Code Python 인터프리터 설정
`.vscode/settings.json` 파일 생성:
```json
{
    "python.defaultInterpreterPath": "/home/ittae.com/dev/david/.venv/bin/python",
    "python.terminal.activateEnvironment": true,
    "python.analysis.extraPaths": [
        "/home/ittae.com/dev/david/.venv/lib/python3.12/site-packages"
    ]
}
```

## 애플리케이션 실행

### 1. 가상환경에서 Flask 애플리케이션 실행
```bash
# 프로젝트 디렉토리로 이동
cd /home/ittae.com/dev/david

# 가상환경의 Python으로 실행
/home/ittae.com/dev/david/.venv/bin/python app.py

# 또는 가상환경 활성화 후 실행
source .venv/bin/activate
python app.py
```

### 2. 웹브라우저에서 확인
- 홈 페이지: http://127.0.0.1:5000
- 메뉴 페이지: http://127.0.0.1:5000/menu

## 주요 기능

### 1. 컴퓨터 이름 표시
- Debug 모드일 때: "컴퓨터(인스턴스) : [호스트네임]" 표시
- Production 모드일 때: 공백 표시

### 2. 라우팅
- `/` : 홈 페이지 (컴퓨터 이름 표시)
- `/menu` : 메뉴 페이지

## 개발 환경 문제 해결

### Flask Import 경고 해결
VS Code에서 "Import flask could not be resolved" 경고가 나타나는 경우:

1. **Python 인터프리터 수동 선택**
   - `Ctrl+Shift+P` → "Python: Select Interpreter"
   - `.venv/bin/python` 선택

2. **VS Code 재시작**
   - 언어 서버가 새 설정을 인식하도록 함

3. **설정 확인**
   ```bash
   # 가상환경에서 Flask 정상 동작 확인
   /home/ittae.com/dev/david/.venv/bin/python -c "import flask; print('Flask import 성공!')"
   ```

### 환경 정보 확인
```bash
# Python 버전 확인
/home/ittae.com/dev/david/.venv/bin/python --version

# 설치된 패키지 확인
/home/ittae.com/dev/david/.venv/bin/pip list

# Flask 버전 확인
/home/ittae.com/dev/david/.venv/bin/python -c "import flask; print(flask.__version__)"
```

## Git 버전 관리

### 변경사항 커밋
```bash
# 변경된 파일 스테이징
git add .

# 커밋
git commit -m "문제8: 컴퓨터 이름 표시 기능 추가"

# 원격 저장소에 push
git push origin main
```

## 설치된 패키지 목록
- Flask (3.1.2)
- Werkzeug (3.1.3)
- Jinja2 (3.1.6)
- click (8.3.0)
- blinker (1.9.0)
- itsdangerous (2.2.0)
- MarkupSafe (3.0.2)

## 참고사항
- Debug 모드가 활성화되어 있어 코드 변경 시 자동 재시작됩니다
- 개발 서버이므로 프로덕션 환경에서는 사용하지 마세요
- VS Code의 Python 확장이 가상환경을 올바르게 인식하지 못할 수 있지만, 실제 실행에는 문제없습니다
