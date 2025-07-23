@echo off
echo SafeDining AI 백엔드 서버 시작...
cd /d "%~dp0"
echo 현재 디렉토리: %CD%
echo.
echo 최소 의존성 설치 중...
pip install -r requirements-minimal.txt
echo.
echo FastAPI 서버 시작 중...
echo 브라우저에서 http://localhost:8000 으로 접속하세요
echo API 문서는 http://localhost:8000/docs 에서 확인 가능합니다
echo 프론트엔드는 http://localhost:3000 에서 확인하세요
echo.
echo 주의: 현재 개발용 더미 데이터로 동작합니다.
echo.
python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000
pause
