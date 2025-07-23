from fastapi import APIRouter, HTTPException, Query
from typing import List, Optional
from app.models.restaurant import Restaurant, RestaurantResponse, HygieneReport
from app.services.restaurant_service import RestaurantService

router = APIRouter()

@router.get("/search", response_model=List[RestaurantResponse])
async def search_restaurants(
    query: str = Query(..., description="검색할 식당명 또는 키워드"),
    latitude: Optional[float] = Query(None, description="위도"),
    longitude: Optional[float] = Query(None, description="경도"),
    radius: Optional[int] = Query(1000, description="검색 반경(미터)"),
    limit: Optional[int] = Query(20, description="결과 개수 제한")
):
    """
    식당 검색 API
    - 식당명, 주소, 키워드로 검색
    - 위치 기반 검색 지원
    """
    try:
        service = RestaurantService()
        restaurants = await service.search_restaurants(
            query=query,
            latitude=latitude,
            longitude=longitude,
            radius=radius,
            limit=limit
        )
        return restaurants
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"검색 중 오류가 발생했습니다: {str(e)}")

@router.get("/{restaurant_id}/hygiene", response_model=HygieneReport)
async def get_hygiene_report(restaurant_id: str):
    """
    식당 위생평가 조회 API
    - 정부 공공데이터 기반 위생평가 정보
    - AI 예측 안전도 점수 포함
    """
    try:
        service = RestaurantService()
        report = await service.get_hygiene_report(restaurant_id)
        if not report:
            raise HTTPException(status_code=404, detail="위생평가 정보를 찾을 수 없습니다")
        return report
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"위생평가 조회 중 오류가 발생했습니다: {str(e)}")

@router.get("/{restaurant_id}", response_model=RestaurantResponse)
async def get_restaurant(restaurant_id: str):
    """
    식당 상세 정보 조회 API
    """
    try:
        service = RestaurantService()
        restaurant = await service.get_restaurant_by_id(restaurant_id)
        if not restaurant:
            raise HTTPException(status_code=404, detail="식당 정보를 찾을 수 없습니다")
        return restaurant
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"식당 정보 조회 중 오류가 발생했습니다: {str(e)}")
