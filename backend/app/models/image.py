from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class ImageAnalysisResult(BaseModel):
    category: str
    confidence: float
    description: str

class HygieneIssue(BaseModel):
    issue_type: str
    severity: str  # HIGH, MEDIUM, LOW
    location: str
    description: str
    recommendation: str

class ImageAnalysisResponse(BaseModel):
    overall_score: float  # 0-100
    grade: str  # A, B, C, D, F
    detected_objects: List[ImageAnalysisResult]
    hygiene_issues: List[HygieneIssue]
    positive_aspects: List[str]
    recommendations: List[str]
    analysis_date: datetime

class FoodSafetyAnalysis(BaseModel):
    food_type: str
    freshness_score: float  # 0-100
    cooking_level: str  # raw, undercooked, well-done, overcooked
    temperature_warning: Optional[str] = None
    contamination_risk: str  # LOW, MEDIUM, HIGH
    safety_recommendations: List[str]
