from fastapi import APIRouter, HTTPException
from app.models.chat import ChatRequest, ChatResponse
from app.services.chat_service import ChatService

router = APIRouter()

@router.post("/", response_model=ChatResponse)
async def chat_with_ai(request: ChatRequest):
    """
    Azure OpenAI 챗봇 API
    - 식당 안전 관련 질문 답변
    - 위생 정보 설명 및 가이드 제공
    """
    try:
        chat_service = ChatService()
        response = await chat_service.process_chat(request)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"챗봇 처리 중 오류가 발생했습니다: {str(e)}")

@router.get("/history/{session_id}")
async def get_chat_history(session_id: str):
    """
    채팅 히스토리 조회 API
    """
    try:
        chat_service = ChatService()
        history = await chat_service.get_chat_history(session_id)
        return {"history": history}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"채팅 히스토리 조회 중 오류가 발생했습니다: {str(e)}")
