from fastapi import APIRouter, HTTPException, UploadFile, File
from app.models.voice import VoiceSearchRequest, VoiceSearchResponse
from app.services.voice_service import VoiceService

router = APIRouter()

@router.post("/analyze", response_model=VoiceSearchResponse)
async def analyze_voice(audio_file: UploadFile = File(...)):
    """
    음성 분석 API
    - Azure Speech Services를 이용한 음성인식
    - 음성으로 식당 검색 및 질문
    """
    try:
        if not audio_file.content_type.startswith('audio/'):
            raise HTTPException(status_code=400, detail="오디오 파일만 업로드 가능합니다")
        
        voice_service = VoiceService()
        result = await voice_service.analyze_voice(audio_file)
        return result
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"음성 분석 중 오류가 발생했습니다: {str(e)}")

@router.post("/text-to-speech")
async def text_to_speech(text: str, language: str = "ko-KR"):
    """
    텍스트 음성 변환 API
    - 챗봇 응답을 음성으로 변환
    """
    try:
        voice_service = VoiceService()
        audio_data = await voice_service.text_to_speech(text, language)
        return {"audio_data": audio_data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"음성 변환 중 오류가 발생했습니다: {str(e)}")
