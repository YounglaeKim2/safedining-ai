from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class VoiceSearchRequest(BaseModel):
    audio_file_path: str
    language: str = "ko-KR"

class VoiceSearchResponse(BaseModel):
    transcribed_text: str
    confidence: float
    search_intent: str  # restaurant_search, question, etc.
    extracted_keywords: list
    search_results: Optional[dict] = None
    processed_at: datetime

class SpeechConfig(BaseModel):
    language: str = "ko-KR"
    voice_name: str = "ko-KR-SunHiNeural"
    speech_rate: str = "1.0"
    speech_pitch: str = "0Hz"
