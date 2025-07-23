# SafeDining AI 개발 환경 설정 가이드

## 필수 요구사항
- Python 3.11+
- Node.js 18+
- Docker & Docker Compose (선택사항)

## 빠른 시작

### 1. 환경변수 설정
```bash
cp .env.example .env
```

### 2. 백엔드 실행
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### 3. 프론트엔드 실행 (새 터미널)
```bash
cd frontend
npm install
npm start
```

### 4. 브라우저에서 확인
- 프론트엔드: http://localhost:3000
- 백엔드 API 문서: http://localhost:8000/docs

## Docker를 이용한 실행
```bash
docker-compose up -d
```

## 트러블슈팅
1. **포트 충돌**: 8000, 3000 포트가 이미 사용 중인 경우 다른 포트 사용
2. **의존성 오류**: 패키지 재설치 필요할 수 있음
3. **권한 오류**: 관리자 권한으로 실행 필요할 수 있음
