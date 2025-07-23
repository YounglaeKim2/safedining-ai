# 🚀 SafeDining AI - 완전 설치 및 실행 가이드

> **새로운 컴퓨터에서 처음부터 끝까지 혼자서 실행하기**

이 가이드는 아무것도 설치되지 않은 Windows 컴퓨터에서 SafeDining AI 프로젝트를 완전히 실행할 수 있도록 도와줍니다.

## 📋 목차
1. [시스템 요구사항](#-시스템-요구사항)
2. [필수 소프트웨어 설치](#-필수-소프트웨어-설치)
3. [프로젝트 다운로드](#-프로젝트-다운로드)
4. [백엔드 설정 및 실행](#-백엔드-설정-및-실행)
5. [프론트엔드 설정 및 실행](#-프론트엔드-설정-및-실행)
6. [실행 확인](#-실행-확인)
7. [문제 해결](#-문제-해결)

---

## 🖥️ 시스템 요구사항

### 최소 요구사항
- **운영체제**: Windows 10/11
- **메모리**: 8GB RAM 이상
- **저장공간**: 5GB 이상 여유공간
- **인터넷**: 안정적인 인터넷 연결

### 권장 사양
- **메모리**: 16GB RAM 이상
- **프로세서**: Intel i5 또는 AMD Ryzen 5 이상

---

## 💾 필수 소프트웨어 설치

다음 순서대로 소프트웨어를 설치해주세요:

### 1. Git 설치 (버전 관리)

1. https://git-scm.com/download/win 접속
2. "64-bit Git for Windows Setup" 다운로드
3. 다운로드한 파일 실행
4. 설치 과정에서 모든 옵션을 기본값으로 선택
5. 설치 완료 후 확인:
   ```bash
   # 명령 프롬프트 또는 PowerShell에서 실행
   git --version
   ```
   **예상 출력**: `git version 2.x.x.windows.x`

### 2. Python 3.11 설치 (백엔드)

1. https://www.python.org/downloads/ 접속
2. "Python 3.11.x" 버전 다운로드 (최신 3.11 버전)
3. 다운로드한 파일 실행
4. **중요**: "Add Python to PATH" 체크박스 선택 ✅
5. "Install Now" 클릭
6. 설치 완료 후 확인:
   ```bash
   python --version
   pip --version
   ```
   **예상 출력**: 
   ```
   Python 3.11.x
   pip 23.x.x
   ```

### 3. Node.js 18 설치 (프론트엔드)

1. https://nodejs.org/ 접속
2. "LTS" 버전 다운로드 (18.x.x)
3. 다운로드한 파일 실행
4. 설치 과정에서 모든 옵션을 기본값으로 선택
5. 설치 완료 후 확인:
   ```bash
   node --version
   npm --version
   ```
   **예상 출력**:
   ```
   v18.x.x
   9.x.x
   ```

### 4. VS Code 설치 (선택사항, 권장)

1. https://code.visualstudio.com/ 접속
2. "Download for Windows" 클릭
3. 설치 과정에서 "Add to PATH" 옵션 선택

---

## 📦 프로젝트 다운로드

### 1. 작업 폴더 생성
```bash
# 바탕화면에 작업 폴더 생성
cd Desktop
mkdir SafeDining
cd SafeDining
```

### 2. GitHub에서 프로젝트 클론
```bash
git clone https://github.com/YounglaeKim2/safedining-ai.git
cd safedining-ai
```

### 3. 프로젝트 구조 확인
```bash
# 디렉토리 구조 확인
dir
```
**확인해야 할 폴더**:
- `backend/` (Python FastAPI)
- `frontend/` (React)
- `README.md`

---

## 🐍 백엔드 설정 및 실행

### 1. 백엔드 폴더로 이동
```bash
cd backend
```

### 2. 가상환경 생성 (권장)
```bash
# 가상환경 생성
python -m venv venv

# 가상환경 활성화 (Windows)
venv\Scripts\activate
```
**성공 시**: 명령 프롬프트 앞에 `(venv)` 표시됨

### 3. Python 패키지 설치
```bash
# 필수 패키지 설치
pip install -r requirements-minimal.txt
```

**설치되는 주요 패키지**:
- FastAPI
- Uvicorn
- Pydantic
- 기타 필수 라이브러리

### 4. 백엔드 서버 실행
```bash
# 방법 1: 배치 파일 사용 (Windows)
start_backend.bat

# 방법 2: 직접 명령어 (모든 OS)
python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### 5. 백엔드 실행 확인
브라우저에서 다음 URL들을 확인:
- **API 문서**: http://localhost:8000/docs
- **기본 응답**: http://localhost:8000/

**성공적인 실행 시 터미널 출력**:
```
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     Started reloader process
INFO:     Started server process
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

---

## ⚛️ 프론트엔드 설정 및 실행

### 1. 새 터미널 창 열기
**중요**: 백엔드는 실행 상태로 두고 새 터미널 창을 열어주세요!

### 2. 프론트엔드 폴더로 이동
```bash
# 프로젝트 루트로 이동 후 frontend 폴더로
cd Desktop\SafeDining\safedining-ai\frontend
```

### 3. Node.js 패키지 설치
```bash
npm install
```

**설치되는 주요 패키지**:
- React
- Material-UI
- Axios
- React Router

**설치 완료까지 시간**: 약 2-5분 (인터넷 속도에 따라)

### 4. 프론트엔드 서버 실행
```bash
# 방법 1: 배치 파일 사용 (Windows)
start_frontend.bat

# 방법 2: 직접 명령어
npm start
```

### 5. 프론트엔드 실행 확인
**성공적인 실행 시**:
- 자동으로 브라우저가 열림
- 주소: http://localhost:3000
- SafeDining AI 홈페이지가 표시됨

---

## ✅ 실행 확인

### 1. 두 서버가 모두 실행 중인지 확인

**백엔드 (포트 8000)**:
- http://localhost:8000/docs → FastAPI Swagger 문서가 보여야 함
- http://localhost:8000/ → `{"message":"SafeDining AI Backend is running!"}` 응답

**프론트엔드 (포트 3000)**:
- http://localhost:3000 → SafeDining AI 웹사이트가 보여야 함

### 2. 기능 테스트

1. **홈페이지 검색**: 
   - 식당 이름 입력하고 검색 버튼 클릭
   - 검색 결과가 나타나는지 확인

2. **API 테스트**:
   - http://localhost:8000/docs 접속
   - `GET /api/restaurants/search` 클릭
   - "Try it out" → "Execute" 실행
   - 응답 데이터 확인

### 3. 정상 실행 상태
두 터미널이 다음과 같이 표시되어야 합니다:

**터미널 1 (백엔드)**:
```
INFO:     Uvicorn running on http://0.0.0.0:8000
```

**터미널 2 (프론트엔드)**:
```
webpack compiled with warnings
Local:            http://localhost:3000
On Your Network:  http://192.168.x.x:3000
```

---

## 🔧 문제 해결

### 자주 발생하는 문제들

#### 1. "Python을 찾을 수 없습니다"
**해결법**:
1. Python 재설치 시 "Add Python to PATH" 선택
2. 컴퓨터 재시작 후 다시 시도

#### 2. "Node.js를 찾을 수 없습니다"
**해결법**:
1. Node.js 재설치
2. 터미널 재시작 후 다시 시도

#### 3. "포트가 이미 사용중입니다"
**해결법**:
```bash
# 포트 사용 프로세스 확인
netstat -ano | findstr :8000
netstat -ano | findstr :3000

# 프로세스 종료 (PID 번호는 위 명령어 결과에서 확인)
taskkill /PID [PID번호] /F
```

#### 4. "패키지 설치 실패"
**해결법**:
```bash
# npm 캐시 클리어
npm cache clean --force

# pip 업그레이드
python -m pip install --upgrade pip
```

#### 5. "방화벽 경고"
**해결법**:
- Windows 방화벽 경고 시 "액세스 허용" 선택
- Python과 Node.js 모두 허용

#### 6. "페이지를 찾을 수 없음"
**체크리스트**:
- [ ] 백엔드 서버가 실행 중인가? (포트 8000)
- [ ] 프론트엔드 서버가 실행 중인가? (포트 3000)
- [ ] 브라우저 주소가 정확한가?
- [ ] 방화벽이 차단하고 있지 않은가?

---

## 📞 추가 도움

### 로그 확인 방법
실행 중 오류 발생 시 터미널에 표시되는 로그를 확인하세요:

**백엔드 로그 예시**:
```
INFO:     Started server process [1234]
ERROR:    [오류 메시지]
```

**프론트엔드 로그 예시**:
```
webpack compiled successfully
Failed to compile. [오류 메시지]
```

### 도움이 필요할 때
1. 터미널의 전체 오류 메시지 복사
2. 어떤 단계에서 문제가 발생했는지 명시
3. 운영체제 및 버전 정보 포함

---

## 🎉 성공!

모든 단계를 완료하셨다면:
- ✅ 백엔드: http://localhost:8000
- ✅ 프론트엔드: http://localhost:3000
- ✅ SafeDining AI가 정상 실행됨!

**축하합니다! SafeDining AI 프로젝트를 성공적으로 실행하셨습니다! 🎊**

---
**문서 작성일**: 2025년 7월 24일  
**프로젝트**: SafeDining AI v1.0  
**GitHub**: https://github.com/YounglaeKim2/safedining-ai
