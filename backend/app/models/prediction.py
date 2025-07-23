from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class SafetyScoreRequest(BaseModel):
    restaurant_id: str
    include_reviews: bool = True
    include_images: bool = True
    include_inspection_history: bool = True

class SafetyFactor(BaseModel):
    factor: str
    score: float  # 0-100
    weight: float  # 가중치
    description: str

class SafetyScoreResponse(BaseModel):
    restaurant_id: str
    overall_score: float  # 0-100
    grade: str  # S, A, B, C, D
    factors: List[SafetyFactor]
    confidence: float  # 예측 신뢰도
    analysis_date: datetime
    recommendations: List[str]

class RiskAnalysis(BaseModel):
    risk_level: str  # HIGH, MEDIUM, LOW
    risk_factors: List[str]
    probability: float  # 위험 발생 확률
    impact: str  # 위험 영향도
    mitigation_strategies: List[str]
