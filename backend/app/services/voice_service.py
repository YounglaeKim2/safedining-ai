from fastapi import UploadFile
from app.models.voice import VoiceSearchResponse
from app.core.config import settings
from datetime import datetime
import tempfile
import os

# Azure Speech Services 선택적 임포트
try:
    import azure.cognitiveservices.speech as speechsdk
    SPEECH_AVAILABLE = True
except ImportError:
    SPEECH_AVAILABLE = False

class VoiceService:
    def __init__(self):
        if SPEECH_AVAILABLE and settings.azure_speech_api_key:
            self.speech_config = speechsdk.SpeechConfig(
                subscription=settings.azure_speech_api_key,
                region=settings.azure_speech_region
            )
            self.speech_config.speech_recognition_language = "ko-KR"
        else:
            print("알림: Azure Speech Services가 설치되지 않았거나 API 키가 설정되지 않았습니다. 더미 데이터로 동작합니다.")
            self.speech_config = None
    
    async def analyze_voice(self, audio_file: UploadFile) -> VoiceSearchResponse:
        """
        음성 분석 및 텍스트 변환
        """
        try:
            # 임시 파일에 오디오 저장
            with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_file:
                content = await audio_file.read()
                temp_file.write(content)
                temp_file_path = temp_file.name
            
            try:
                # Azure Speech Services를 이용한 음성 인식
                transcribed_text = await self._speech_to_text(temp_file_path)
                
                # 검색 의도 분석
                intent = await self._analyze_intent(transcribed_text)
                
                # 키워드 추출
                keywords = await self._extract_keywords(transcribed_text)
                
                return VoiceSearchResponse(
                    transcribed_text=transcribed_text,
                    confidence=0.95,
                    search_intent=intent,
                    extracted_keywords=keywords,
                    processed_at=datetime.now()
                )
                
            finally:
                # 임시 파일 삭제
                os.unlink(temp_file_path)
                
        except Exception as e:
            raise Exception(f"음성 분석 중 오류: {str(e)}")
    
    async def _speech_to_text(self, audio_file_path: str) -> str:
        """
        음성을 텍스트로 변환
        """
        try:
            # TODO: 실제 Azure Speech API 호출 구현
            # 현재는 더미 응답
            return "강남역 근처 맛있는 한식당 추천해줘"
            
        except Exception as e:
            raise Exception(f"음성 변환 중 오류: {str(e)}")
    
    async def _analyze_intent(self, text: str) -> str:
        """
        텍스트에서 검색 의도 분석
        """
        text_lower = text.lower()
        
        if "추천" in text_lower or "찾아" in text_lower:
            return "restaurant_search"
        elif "위생" in text_lower or "안전" in text_lower:
            return "safety_inquiry"
        elif "리뷰" in text_lower:
            return "review_inquiry"
        else:
            return "general_question"
    
    async def _extract_keywords(self, text: str) -> list:
        """
        텍스트에서 키워드 추출
        """
        # TODO: 실제 NLP 키워드 추출 로직 구현
        keywords = []
        
        # 간단한 키워드 추출
        location_keywords = ["강남", "홍대", "명동", "이태원", "신촌"]
        food_keywords = ["한식", "중식", "일식", "양식", "카페", "치킨", "피자"]
        
        for keyword in location_keywords:
            if keyword in text:
                keywords.append(keyword)
        
        for keyword in food_keywords:
            if keyword in text:
                keywords.append(keyword)
                
        return keywords
    
    async def text_to_speech(self, text: str, language: str = "ko-KR") -> str:
        """
        텍스트를 음성으로 변환
        """
        try:
            # TODO: Azure Speech Services TTS 구현
            return "audio_data_base64_encoded_here"
            
        except Exception as e:
            raise Exception(f"음성 변환 중 오류: {str(e)}")
