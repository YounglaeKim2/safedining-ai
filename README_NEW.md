# SafeDining AI 🍽️🤖
**"AI가 지켜주는 안전한 식탁"**

AI 기반 식당 위생 안전도 평가 및 예측 서비스

[![GitHub](https://img.shields.io/badge/GitHub-safedining--ai-blue?logo=github)](https://github.com/YounglaeKim2/safedining-ai)
[![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)](https://python.org)
[![React](https://img.shields.io/badge/React-18-blue?logo=react)](https://reactjs.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-Latest-green?logo=fastapi)](https://fastapi.tiangolo.com)

## 🌟 주요 기능
- 🔍 **식당 검색 및 지도 표시** - Naver Maps API 연동
- 📊 **AI 기반 위생 안전도 예측** - 머신러닝 기반 분석
- 💬 **Azure OpenAI 챗봇** - 식당 안전 관련 질의응답
- 🎤 **음성 검색** - Azure Speech Services 연동
- 📸 **이미지 위생 체크** - AI 기반 이미지 분석
- 🔔 **실시간 알림 시스템** - 위험 요소 모니터링

## 🏗️ 기술 스택

### 백엔드
- **FastAPI** - 고성능 웹 프레임워크
- **Azure Cosmos DB** - NoSQL 데이터베이스
- **Redis** - 캐시 및 세션 관리
- **Azure OpenAI** - AI 챗봇 및 분석
- **Azure Speech Services** - 음성 인식/합성

### 프론트엔드
- **React 18** - 모던 웹 프레임워크
- **Material-UI** - UI 컴포넌트 라이브러리
- **Naver Maps API** - 지도 서비스
- **Axios** - HTTP 클라이언트

## 🚀 빠른 시작

### 필수 요구사항
- Python 3.11+
- Node.js 18+
- Git

### 설치 및 실행
```bash
# 1. 저장소 클론
git clone https://github.com/YounglaeKim2/safedining-ai.git
cd safedining-ai

# 2. 백엔드 실행
cd backend
.\start_backend.bat

# 3. 프론트엔드 실행 (새 터미널)
cd frontend
.\start_frontend.bat
```

### 브라우저에서 확인
- **웹사이트**: http://localhost:3000
- **API 문서**: http://localhost:8000/docs
- **API 테스트**: http://localhost:8000

## 📁 프로젝트 구조
```
safeDining/
├── backend/                 # FastAPI 백엔드
│   ├── app/
│   │   ├── api/routers/    # API 엔드포인트
│   │   ├── core/           # 설정 및 보안
│   │   ├── models/         # 데이터 모델
│   │   ├── services/       # 비즈니스 로직
│   │   └── utils/          # 유틸리티
│   └── main.py             # FastAPI 앱
├── frontend/               # React 프론트엔드
│   ├── src/
│   │   ├── components/     # React 컴포넌트
│   │   ├── pages/          # 페이지 컴포넌트
│   │   └── services/       # API 서비스
│   └── public/
└── docker-compose.yml      # Docker 설정
```

## 🔗 API 엔드포인트
- `GET /api/restaurants/search` - 식당 검색
- `GET /api/restaurants/{id}/hygiene` - 위생평가 조회
- `POST /api/predict/safety-score` - AI 안전도 예측
- `POST /api/chat` - AI 챗봇 대화
- `POST /api/voice/analyze` - 음성 분석
- `POST /api/image/hygiene-check` - 이미지 위생 체크

## 🐳 Docker 실행
```bash
docker-compose up -d
```

## 🤝 기여하기
1. Fork 프로젝트
2. Feature 브랜치 생성 (`git checkout -b feature/amazing-feature`)
3. 변경사항 커밋 (`git commit -m 'Add amazing feature'`)
4. 브랜치에 Push (`git push origin feature/amazing-feature`)
5. Pull Request 생성

## 📄 라이선스
이 프로젝트는 MIT 라이선스를 따릅니다.

## 📞 연락처
- GitHub: [@YounglaeKim2](https://github.com/YounglaeKim2)
- 프로젝트 링크: [SafeDining AI](https://github.com/YounglaeKim2/safedining-ai)

---
**SafeDining AI** - AI가 지켜주는 안전한 식탁 🍽️🤖
