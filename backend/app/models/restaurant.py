from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class Restaurant(BaseModel):
    id: str
    name: str
    address: str
    phone: Optional[str] = None
    category: str
    latitude: float
    longitude: float
    business_license: Optional[str] = None
    created_at: datetime
    updated_at: datetime

class RestaurantResponse(BaseModel):
    id: str
    name: str
    address: str
    phone: Optional[str] = None
    category: str
    latitude: float
    longitude: float
    safety_score: Optional[float] = None
    hygiene_grade: Optional[str] = None
    distance: Optional[float] = None  # 검색 위치로부터의 거리 (미터)

class HygieneInspection(BaseModel):
    inspection_date: datetime
    inspector: str
    violations: List[str]
    grade: str  # 우수, 좋음, 보통, 나쁨
    score: int  # 0-100

class HygieneReport(BaseModel):
    restaurant_id: str
    restaurant_name: str
    current_grade: str
    current_score: int
    inspections: List[HygieneInspection]
    ai_safety_score: Optional[float] = None
    risk_factors: List[str]
    recommendations: List[str]
    last_updated: datetime
