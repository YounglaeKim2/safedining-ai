from fastapi import APIRouter, HTTPException, UploadFile, File
from app.models.image import ImageAnalysisResponse
from app.services.image_service import ImageService

router = APIRouter()

@router.post("/hygiene-check", response_model=ImageAnalysisResponse)
async def check_hygiene(image_file: UploadFile = File(...)):
    """
    이미지 위생 체크 API
    - 업로드된 이미지에서 위생 상태 분석
    - AI 기반 위생 점수 및 개선사항 제공
    """
    try:
        if not image_file.content_type.startswith('image/'):
            raise HTTPException(status_code=400, detail="이미지 파일만 업로드 가능합니다")
        
        image_service = ImageService()
        result = await image_service.analyze_hygiene(image_file)
        return result
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"이미지 분석 중 오류가 발생했습니다: {str(e)}")

@router.post("/food-safety")
async def analyze_food_safety(image_file: UploadFile = File(...)):
    """
    음식 안전성 분석 API
    - 음식 이미지에서 신선도, 조리 상태 등 분석
    """
    try:
        if not image_file.content_type.startswith('image/'):
            raise HTTPException(status_code=400, detail="이미지 파일만 업로드 가능합니다")
        
        image_service = ImageService()
        result = await image_service.analyze_food_safety(image_file)
        return result
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"음식 안전성 분석 중 오류가 발생했습니다: {str(e)}")
