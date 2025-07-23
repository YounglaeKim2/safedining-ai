# SafeDining AI 프로젝트 시작 가이드

## 개발 환경 설정

### 1. 환경변수 설정
`.env.example` 파일을 복사하여 `.env` 파일을 만들고 실제 API 키들을 입력하세요.

```bash
cp .env.example .env
```

### 2. Docker를 이용한 개발 환경 실행

#### 전체 서비스 실행
```bash
docker-compose up -d
```

#### 개별 서비스 실행
```bash
# Redis만 실행
docker-compose up -d redis

# 백엔드 개발 모드
cd backend
pip install -r requirements.txt
uvicorn main:app --reload

# 프론트엔드 개발 모드
cd frontend
npm install
npm start
```

### 3. 로컬 개발 환경 설정

#### 백엔드 설정 (Python 3.11+)
```bash
cd backend
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

pip install -r requirements.txt
uvicorn main:app --reload
```

#### 프론트엔드 설정 (Node.js 18+)
```bash
cd frontend
npm install
npm start
```

### 4. 서비스 접속 주소
- 프론트엔드: http://localhost:3000
- 백엔드 API: http://localhost:8000
- API 문서 (Swagger): http://localhost:8000/docs
- Redis: localhost:6379

## API 엔드포인트

### 식당 관련
- `GET /api/restaurants/search` - 식당 검색
- `GET /api/restaurants/{id}` - 식당 상세 정보
- `GET /api/restaurants/{id}/hygiene` - 위생평가 조회

### AI 예측
- `POST /api/predict/safety-score` - AI 안전도 예측
- `POST /api/predict/risk-analysis` - 위험 요소 분석

### 챗봇
- `POST /api/chat` - AI 챗봇 대화
- `GET /api/chat/history/{session_id}` - 채팅 히스토리

### 음성 서비스
- `POST /api/voice/analyze` - 음성 분석
- `POST /api/voice/text-to-speech` - 텍스트 음성 변환

### 이미지 분석
- `POST /api/image/hygiene-check` - 이미지 위생 체크
- `POST /api/image/food-safety` - 음식 안전성 분석

## 주요 기능

1. **식당 검색 및 지도**: Naver Maps API 연동
2. **AI 안전도 분석**: 위생평가, 리뷰, 이미지 종합 분석
3. **실시간 알림**: 위생 등급 변경, 위험 요소 알림
4. **챗봇**: Azure OpenAI 기반 상담 서비스
5. **음성 검색**: Azure Speech Services 연동
6. **이미지 분석**: AI 기반 위생 상태 체크

## 개발 참고사항

- 백엔드: FastAPI + Azure Cosmos DB + Redis
- 프론트엔드: React + Material-UI + Naver Maps
- AI 서비스: Azure OpenAI + Azure Speech Services
- 배포: Docker + Docker Compose
