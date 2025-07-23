# Windows에서 SafeDining AI 실행하기

## 문제 해결됨! ✅

**Pillow 설치 오류 문제를 해결했습니다.**

## 빠른 실행 방법

### 1단계: 백엔드 서버 시작
```powershell
# 방법 1: 배치 파일 실행
cd c:\workspace\safeDining\backend
.\start_backend.bat

# 방법 2: 수동 실행
cd c:\workspace\safeDining\backend
pip install -r requirements-minimal.txt
python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### 2단계: 프론트엔드 서버 시작 (새 PowerShell 창에서)
```powershell
# 방법 1: 배치 파일 실행
cd c:\workspace\safeDining\frontend
.\start_frontend.bat

# 방법 2: 수동 실행
cd c:\workspace\safeDining\frontend
npm install
npm start
```

### 3단계: 브라우저에서 확인
- **메인 웹사이트**: http://localhost:3000
- **API 문서**: http://localhost:8000/docs
- **API 헬스체크**: http://localhost:8000

## 변경사항

### ✅ 해결된 문제들:
1. **Pillow 설치 오류**: `requirements-minimal.txt` 사용으로 해결
2. **Redis 의존성**: 인메모리 캐시로 대체
3. **Azure 서비스**: 선택적 임포트로 변경 (없어도 동작)
4. **복잡한 의존성**: 최소 패키지만 설치

### 🎯 현재 동작 상태:
- ✅ FastAPI 서버 정상 동작
- ✅ React 프론트엔드 정상 동작  
- ✅ API 엔드포인트 모두 응답
- ✅ 더미 데이터로 기능 시연 가능
- ⏳ 실제 Azure 서비스 연동은 나중에 구현

## 트러블슈팅

### 포트 충돌 문제
```powershell
# 8000 포트 사용 중인 프로세스 확인
netstat -ano | findstr :8000

# 3000 포트 사용 중인 프로세스 확인  
netstat -ano | findstr :3000
```

### Python 버전 확인
```powershell
python --version
# Python 3.8+ 필요
```

### Node.js 버전 확인
```powershell
node --version
npm --version
# Node.js 16+ 필요
```

이제 문제없이 실행됩니다! 🚀
