from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    # 기본 설정
    app_name: str = "SafeDining AI"
    debug: bool = False
    environment: str = "production"
    
    # CORS 설정
    allowed_hosts: List[str] = ["http://localhost:3000", "http://127.0.0.1:3000"]
    
    # 데이터베이스 설정
    cosmos_db_uri: str = ""
    cosmos_db_key: str = ""
    cosmos_db_name: str = "safedining"
    
    # Redis 설정
    redis_url: str = "redis://localhost:6379"
    
    # Azure 서비스 설정
    azure_openai_api_key: str = ""
    azure_openai_endpoint: str = ""
    azure_speech_api_key: str = ""
    azure_speech_region: str = ""
    
    # Naver Maps API
    naver_maps_client_id: str = ""
    naver_maps_client_secret: str = ""
    
    # JWT 설정
    secret_key: str = "your-secret-key-change-this"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    
    class Config:
        env_file = ".env"
        case_sensitive = False

settings = Settings()
