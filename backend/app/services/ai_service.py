from app.models.prediction import SafetyScoreRequest, SafetyScoreResponse, SafetyFactor
from app.core.config import settings
from datetime import datetime

# OpenAI 선택적 임포트
try:
    import openai
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False

class AIService:
    def __init__(self):
        if OPENAI_AVAILABLE and settings.azure_openai_api_key:
            openai.api_key = settings.azure_openai_api_key
            openai.api_base = settings.azure_openai_endpoint
            openai.api_type = "azure"
            openai.api_version = "2023-12-01-preview"
        else:
            print("알림: OpenAI가 설치되지 않았거나 API 키가 설정되지 않았습니다. 더미 데이터로 동작합니다.")
    
    async def predict_safety_score(self, request: SafetyScoreRequest) -> SafetyScoreResponse:
        """
        AI 기반 안전도 점수 예측
        """
        try:
            # TODO: 실제 AI 모델을 이용한 예측 로직 구현
            # 현재는 더미 데이터 반환
            
            factors = [
                SafetyFactor(
                    factor="위생 검사 점수",
                    score=85.0,
                    weight=0.3,
                    description="정부 위생 검사 결과"
                ),
                SafetyFactor(
                    factor="고객 리뷰 분석",
                    score=78.5,
                    weight=0.25,
                    description="고객 리뷰에서 추출한 위생 관련 언급"
                ),
                SafetyFactor(
                    factor="시설 이미지 분석",
                    score=82.0,
                    weight=0.2,
                    description="업로드된 이미지의 AI 분석 결과"
                ),
                SafetyFactor(
                    factor="운영 기간",
                    score=90.0,
                    weight=0.15,
                    description="영업 지속성 및 안정성"
                ),
                SafetyFactor(
                    factor="위반 이력",
                    score=95.0,
                    weight=0.1,
                    description="과거 위반 사항 이력"
                )
            ]
            
            # 가중 평균 계산
            overall_score = sum(f.score * f.weight for f in factors)
            
            # 등급 계산
            if overall_score >= 90:
                grade = "S"
            elif overall_score >= 80:
                grade = "A"
            elif overall_score >= 70:
                grade = "B"
            elif overall_score >= 60:
                grade = "C"
            else:
                grade = "D"
            
            return SafetyScoreResponse(
                restaurant_id=request.restaurant_id,
                overall_score=overall_score,
                grade=grade,
                factors=factors,
                confidence=0.85,
                analysis_date=datetime.now(),
                recommendations=[
                    "냉장고 온도 관리 시스템 개선",
                    "직원 위생 교육 강화",
                    "정기적인 시설 점검 실시"
                ]
            )
            
        except Exception as e:
            raise Exception(f"AI 예측 처리 중 오류: {str(e)}")
    
    async def analyze_risk_factors(self, restaurant_id: str) -> dict:
        """
        위험 요소 분석
        """
        try:
            # TODO: Azure OpenAI를 이용한 실제 위험 분석 로직
            return {
                "restaurant_id": restaurant_id,
                "risk_level": "MEDIUM",
                "risk_factors": [
                    "계절적 식재료 보관 위험",
                    "고온 조리 과정의 온도 관리",
                    "많은 고객 대응으로 인한 위생 관리 소홀 가능성"
                ],
                "recommendations": [
                    "여름철 냉장 보관 온도 강화",
                    "조리 온도 모니터링 시스템 도입",
                    "피크 시간대 위생 체크리스트 운영"
                ],
                "confidence": 0.78
            }
            
        except Exception as e:
            raise Exception(f"위험 분석 처리 중 오류: {str(e)}")
