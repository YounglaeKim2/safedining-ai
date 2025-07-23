from fastapi import UploadFile
from app.models.image import ImageAnalysisResponse, ImageAnalysisResult, HygieneIssue, FoodSafetyAnalysis
import tempfile
import os
from datetime import datetime

# Pillow 선택적 임포트
try:
    from PIL import Image
    PILLOW_AVAILABLE = True
except ImportError:
    PILLOW_AVAILABLE = False

class ImageService:
    def __init__(self):
        pass
    
    async def analyze_hygiene(self, image_file: UploadFile) -> ImageAnalysisResponse:
        """
        이미지에서 위생 상태 분석
        """
        try:
            # 임시 파일에 이미지 저장
            with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp_file:
                content = await image_file.read()
                temp_file.write(content)
                temp_file_path = temp_file.name
            
            try:
                # 이미지 분석
                analysis_results = await self._analyze_image_for_hygiene(temp_file_path)
                
                return analysis_results
                
            finally:
                # 임시 파일 삭제
                os.unlink(temp_file_path)
                
        except Exception as e:
            raise Exception(f"이미지 분석 중 오류: {str(e)}")
    
    async def _analyze_image_for_hygiene(self, image_path: str) -> ImageAnalysisResponse:
        """
        위생 상태 이미지 분석
        """
        try:
            # Pillow가 없는 경우 경고 메시지와 함께 더미 데이터 반환
            if not PILLOW_AVAILABLE:
                print("경고: Pillow가 설치되지 않았습니다. 실제 이미지 분석을 위해서는 'pip install pillow' 실행이 필요합니다.")
            
            # TODO: 실제 AI 모델을 이용한 이미지 분석 구현
            # 현재는 더미 데이터 반환
            
            detected_objects = [
                ImageAnalysisResult(
                    category="주방 용기",
                    confidence=0.95,
                    description="깨끗한 스테인리스 용기"
                ),
                ImageAnalysisResult(
                    category="조리대",
                    confidence=0.88,
                    description="정리된 조리 공간"
                ),
                ImageAnalysisResult(
                    category="직원",
                    confidence=0.92,
                    description="위생모 착용한 직원"
                )
            ]
            
            hygiene_issues = [
                HygieneIssue(
                    issue_type="청소 상태",
                    severity="LOW",
                    location="바닥",
                    description="일부 물기 발견",
                    recommendation="바닥 건조 상태 유지"
                )
            ]
            
            return ImageAnalysisResponse(
                overall_score=82.5,
                grade="B",
                detected_objects=detected_objects,
                hygiene_issues=hygiene_issues,
                positive_aspects=[
                    "직원 위생복 착용 양호",
                    "조리 기구 정리 상태 좋음",
                    "전반적인 청결 상태 양호"
                ],
                recommendations=[
                    "바닥 건조 상태 유지",
                    "정기적인 환기 실시",
                    "조리대 소독 강화"
                ],
                analysis_date=datetime.now()
            )
            
        except Exception as e:
            raise Exception(f"위생 분석 중 오류: {str(e)}")
    
    async def analyze_food_safety(self, image_file: UploadFile) -> FoodSafetyAnalysis:
        """
        음식 안전성 분석
        """
        try:
            # 임시 파일에 이미지 저장
            with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp_file:
                content = await image_file.read()
                temp_file.write(content)
                temp_file_path = temp_file.name
            
            try:
                # 음식 안전성 분석
                analysis = await self._analyze_food_image(temp_file_path)
                
                return analysis
                
            finally:
                # 임시 파일 삭제
                os.unlink(temp_file_path)
                
        except Exception as e:
            raise Exception(f"음식 안전성 분석 중 오류: {str(e)}")
    
    async def _analyze_food_image(self, image_path: str) -> FoodSafetyAnalysis:
        """
        음식 이미지 안전성 분석
        """
        try:
            # TODO: 실제 AI 모델을 이용한 음식 분석 구현
            
            return FoodSafetyAnalysis(
                food_type="한식 정식",
                freshness_score=88.5,
                cooking_level="well-done",
                temperature_warning=None,
                contamination_risk="LOW",
                safety_recommendations=[
                    "적절한 조리 온도 유지됨",
                    "신선한 재료 사용 추정",
                    "위생적인 플레이팅"
                ]
            )
            
        except Exception as e:
            raise Exception(f"음식 분석 중 오류: {str(e)}")
