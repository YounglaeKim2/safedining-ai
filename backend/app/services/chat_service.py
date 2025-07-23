from app.models.chat import ChatRequest, ChatResponse, ChatHistory, ChatMessage
from app.core.config import settings
import uuid
from datetime import datetime
from typing import List

# OpenAI 선택적 임포트
try:
    import openai
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False

class ChatService:
    def __init__(self):
        if OPENAI_AVAILABLE and settings.azure_openai_api_key:
            openai.api_key = settings.azure_openai_api_key
            openai.api_base = settings.azure_openai_endpoint
            openai.api_type = "azure"
            openai.api_version = "2023-12-01-preview"
        else:
            print("알림: OpenAI가 설치되지 않았거나 API 키가 설정되지 않았습니다. 더미 데이터로 동작합니다.")
    
    async def process_chat(self, request: ChatRequest) -> ChatResponse:
        """
        챗봇 대화 처리
        """
        try:
            # 세션 ID 생성 또는 기존 사용
            session_id = request.session_id or str(uuid.uuid4())
            
            # TODO: Azure OpenAI API 호출
            # 현재는 더미 응답 생성
            response_message = await self._generate_response(request.message, request.context)
            
            # 응답 생성
            response = ChatResponse(
                message=response_message,
                session_id=session_id,
                suggestions=[
                    "이 식당의 위생 등급은 어떻게 되나요?",
                    "근처 안전한 식당을 추천해주세요",
                    "음식점 위생 관리 팁을 알려주세요",
                    "식중독 예방법을 알려주세요"
                ],
                restaurant_info=request.context,
                created_at=datetime.now()
            )
            
            # TODO: 채팅 히스토리 저장
            await self._save_chat_history(session_id, request.message, response_message)
            
            return response
            
        except Exception as e:
            raise Exception(f"챗봇 처리 중 오류: {str(e)}")
    
    async def _generate_response(self, message: str, context: dict = None) -> str:
        """
        AI 응답 생성
        """
        # TODO: 실제 Azure OpenAI API 호출 구현
        # 현재는 규칙 기반 더미 응답
        
        message_lower = message.lower()
        
        if "위생" in message or "청결" in message:
            return "식당의 위생 상태는 매우 중요합니다. 저희 AI가 분석한 결과를 확인해보세요. 위생 등급과 상세한 분석 결과를 제공해드립니다."
        elif "추천" in message:
            return "근처 안전하고 위생적인 식당들을 추천해드릴게요. 현재 위치를 기반으로 높은 안전도 점수를 받은 식당들을 찾아보겠습니다."
        elif "안전" in message:
            return "음식 안전은 가장 우선되어야 할 요소입니다. 저희가 제공하는 AI 안전도 분석을 통해 신뢰할 수 있는 식당을 선택하세요."
        else:
            return "안녕하세요! SafeDining AI입니다. 🍽️ 식당의 위생과 안전에 대해 궁금한 점이 있으시면 언제든 물어보세요!"
    
    async def _save_chat_history(self, session_id: str, user_message: str, ai_message: str):
        """
        채팅 히스토리 저장
        """
        # TODO: 실제 데이터베이스 저장 로직 구현
        pass
    
    async def get_chat_history(self, session_id: str) -> List[ChatMessage]:
        """
        채팅 히스토리 조회
        """
        # TODO: 실제 데이터베이스 조회 로직 구현
        return [
            ChatMessage(
                role="user",
                content="안녕하세요",
                timestamp=datetime.now()
            ),
            ChatMessage(
                role="assistant",
                content="안녕하세요! SafeDining AI입니다.",
                timestamp=datetime.now()
            )
        ]
