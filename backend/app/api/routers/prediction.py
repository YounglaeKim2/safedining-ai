from fastapi import APIRouter, HTTPException
from app.models.prediction import SafetyScoreRequest, SafetyScoreResponse
from app.services.ai_service import AIService

router = APIRouter()

@router.post("/safety-score", response_model=SafetyScoreResponse)
async def predict_safety_score(request: SafetyScoreRequest):
    """
    AI 안전도 예측 API
    - 위생평가 데이터, 리뷰, 이미지 등을 종합하여 안전도 점수 예측
    - Azure OpenAI 기반 분석
    """
    try:
        ai_service = AIService()
        result = await ai_service.predict_safety_score(request)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"안전도 예측 중 오류가 발생했습니다: {str(e)}")

@router.post("/risk-analysis")
async def analyze_risk_factors(restaurant_id: str):
    """
    위험 요소 분석 API
    - 식당의 잠재적 위험 요소 분석
    - 개선 권장사항 제공
    """
    try:
        ai_service = AIService()
        analysis = await ai_service.analyze_risk_factors(restaurant_id)
        return analysis
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"위험 요소 분석 중 오류가 발생했습니다: {str(e)}")
