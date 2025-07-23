#!/bin/bash
echo "SafeDining AI 백엔드 서버 시작..."
cd "$(dirname "$0")"
echo "현재 디렉토리: $(pwd)"
echo ""
echo "Python 의존성 설치 중..."
pip install -r requirements.txt
echo ""
echo "FastAPI 서버 시작 중..."
echo "브라우저에서 http://localhost:8000 으로 접속하세요"
echo "API 문서는 http://localhost:8000/docs 에서 확인 가능합니다"
echo ""
python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000
