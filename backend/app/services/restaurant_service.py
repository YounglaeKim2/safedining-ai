from typing import List, Optional
from app.models.restaurant import Restaurant, RestaurantResponse, HygieneReport
import json

# 선택적 임포트
try:
    from app.utils.database import get_cosmos_client
    COSMOS_AVAILABLE = True
except ImportError:
    COSMOS_AVAILABLE = False

try:
    from app.utils.cache import get_redis_client
    REDIS_AVAILABLE = True
except ImportError:
    REDIS_AVAILABLE = False

class RestaurantService:
    def __init__(self):
        self.db_client = get_cosmos_client() if COSMOS_AVAILABLE else None
        self.redis_client = None  # Redis 연결은 나중에 구현
        # 임시 인메모리 캐시
        self._cache = {}
    
    async def search_restaurants(
        self, 
        query: str,
        latitude: Optional[float] = None,
        longitude: Optional[float] = None,
        radius: int = 1000,
        limit: int = 20
    ) -> List[RestaurantResponse]:
        """
        식당 검색 서비스
        """
        # 캐시 키 생성
        cache_key = f"search:{query}:{latitude}:{longitude}:{radius}:{limit}"
        
        # 인메모리 캐시에서 확인
        if cache_key in self._cache:
            return [RestaurantResponse(**item) for item in self._cache[cache_key]]
        
        # TODO: Cosmos DB에서 실제 검색 로직 구현
        # 현재는 더미 데이터 반환
        dummy_restaurants = [
            RestaurantResponse(
                id="rest_001",
                name=f"맛있는 식당 {i}",
                address=f"서울시 강남구 테헤란로 {i}번길 123",
                phone="02-1234-5678",
                category="한식",
                latitude=37.5665 + (i * 0.001),
                longitude=126.9780 + (i * 0.001),
                safety_score=85.5,
                hygiene_grade="좋음",
                distance=100 * i
            ) for i in range(1, min(limit + 1, 6))
        ]
        
        # 인메모리 캐시에 저장
        self._cache[cache_key] = [item.dict() for item in dummy_restaurants]
        
        return dummy_restaurants
    
    async def get_restaurant_by_id(self, restaurant_id: str) -> Optional[RestaurantResponse]:
        """
        식당 상세 정보 조회
        """
        cache_key = f"restaurant:{restaurant_id}"
        
        # 인메모리 캐시에서 확인
        if cache_key in self._cache:
            return RestaurantResponse(**self._cache[cache_key])
        
        # TODO: Cosmos DB에서 실제 조회 로직 구현
        dummy_restaurant = RestaurantResponse(
            id=restaurant_id,
            name="맛있는 식당",
            address="서울시 강남구 테헤란로 123",
            phone="02-1234-5678",
            category="한식",
            latitude=37.5665,
            longitude=126.9780,
            safety_score=85.5,
            hygiene_grade="좋음"
        )
        
        # 인메모리 캐시에 저장
        self._cache[cache_key] = dummy_restaurant.dict()
        
        return dummy_restaurant
    
    async def get_hygiene_report(self, restaurant_id: str) -> Optional[HygieneReport]:
        """
        위생평가 보고서 조회
        """
        cache_key = f"hygiene:{restaurant_id}"
        
        # 인메모리 캐시에서 확인
        if cache_key in self._cache:
            return HygieneReport(**self._cache[cache_key])
        
        # TODO: 실제 위생평가 데이터 조회 로직 구현
        from datetime import datetime
        from app.models.restaurant import HygieneInspection
        
        dummy_report = HygieneReport(
            restaurant_id=restaurant_id,
            restaurant_name="맛있는 식당",
            current_grade="좋음",
            current_score=85,
            inspections=[
                HygieneInspection(
                    inspection_date=datetime.now(),
                    inspector="김검사관",
                    violations=["냉장고 온도 관리 미흡"],
                    grade="좋음",
                    score=85
                )
            ],
            ai_safety_score=87.5,
            risk_factors=["냉장보관 온도"],
            recommendations=["냉장고 온도 체크 주기 단축"],
            last_updated=datetime.now()
        )
        
        # 인메모리 캐시에 저장
        self._cache[cache_key] = dummy_report.dict()
        
        return dummy_report
