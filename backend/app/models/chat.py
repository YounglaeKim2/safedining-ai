from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class ChatMessage(BaseModel):
    role: str  # user, assistant, system
    content: str
    timestamp: datetime

class ChatRequest(BaseModel):
    message: str
    session_id: Optional[str] = None
    context: Optional[dict] = None  # 식당 정보 등 컨텍스트

class ChatResponse(BaseModel):
    message: str
    session_id: str
    suggestions: List[str]  # 추천 질문들
    restaurant_info: Optional[dict] = None  # 관련 식당 정보
    created_at: datetime

class ChatHistory(BaseModel):
    session_id: str
    messages: List[ChatMessage]
    created_at: datetime
    updated_at: datetime
