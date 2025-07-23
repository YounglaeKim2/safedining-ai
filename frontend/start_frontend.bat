@echo off
echo SafeDining AI 프론트엔드 서버 시작...
cd /d "%~dp0"
echo 현재 디렉토리: %CD%
echo.
echo Node.js 의존성 설치 중...
npm install
echo.
echo React 개발 서버 시작 중...
echo 브라우저에서 http://localhost:3000 으로 접속하세요
echo.
npm start
pause
