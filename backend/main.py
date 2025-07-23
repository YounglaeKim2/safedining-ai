from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routers import restaurants, prediction, chat, voice, image
from app.core.config import settings

app = FastAPI(
    title="SafeDining AI API",
    description="AI가 지켜주는 안전한 식탁 - API 서버",
    version="1.0.0"
)

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_hosts,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# API 라우터 등록
app.include_router(restaurants.router, prefix="/api/restaurants", tags=["restaurants"])
app.include_router(prediction.router, prefix="/api/predict", tags=["prediction"])
app.include_router(chat.router, prefix="/api/chat", tags=["chat"])
app.include_router(voice.router, prefix="/api/voice", tags=["voice"])
app.include_router(image.router, prefix="/api/image", tags=["image"])

@app.get("/")
async def root():
    return {"message": "SafeDining AI API 서버가 정상 작동 중입니다! 🍽️🤖"}

@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "SafeDining AI"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
