# SafeDining AI 🍽️🤖
**"AI가 지켜주는 안전한 식탁"**

AI 기반 식당 위생 안전도 평가 및 예측 서비스

## 프로젝트 구조
```
safeDining/
├── backend/                 # FastAPI 백엔드
│   ├── app/
│   │   ├── api/            # API 라우터
│   │   ├── core/           # 설정, 보안
│   │   ├── models/         # 데이터 모델
│   │   ├── services/       # 비즈니스 로직
│   │   └── utils/          # 유틸리티
│   ├── requirements.txt
│   └── main.py
├── frontend/               # React 프론트엔드
│   ├── src/
│   │   ├── components/     # React 컴포넌트
│   │   ├── services/       # API 서비스
│   │   ├── utils/          # 유틸리티
│   │   └── pages/          # 페이지 컴포넌트
│   ├── package.json
│   └── public/
├── docker-compose.yml      # 개발 환경 설정
└── .env.example           # 환경변수 예시
```

## 주요 기능
- 🔍 식당 검색 및 지도 표시
- 📊 AI 기반 위생 안전도 예측
- 💬 Azure OpenAI 챗봇
- 🎤 음성 검색 (Azure Speech)
- 📸 이미지 위생 체크
- 🔔 실시간 알림 시스템

## 기술 스택
### 백엔드
- FastAPI
- Azure Cosmos DB
- Redis
- Azure OpenAI
- Azure Speech Services

### 프론트엔드
- React
- Naver Maps API
- Material-UI

## 시작하기

### 빠른 실행 (Windows)
1. **백엔드 서버 시작**
   - `backend/start_backend.bat` 파일을 더블클릭
   - 또는 PowerShell에서: `cd backend && .\start_backend.bat`

2. **프론트엔드 서버 시작** (새 창에서)
   - `frontend/start_frontend.bat` 파일을 더블클릭
   - 또는 PowerShell에서: `cd frontend && .\start_frontend.bat`

3. **브라우저에서 확인**
   - 프론트엔드: http://localhost:3000
   - 백엔드 API 문서: http://localhost:8000/docs

### 수동 설정
1. 백엔드 설정
```bash
cd backend
pip install -r requirements.txt
python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

2. 프론트엔드 설정 (새 터미널에서)
```bash
cd frontend
npm install
npm start
```

### Docker 실행
```bash
docker-compose up -d
```
