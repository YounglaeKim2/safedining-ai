import apiClient from './api';

export const restaurantService = {
  // 식당 검색
  searchRestaurants: async (params) => {
    const response = await apiClient.get('/api/restaurants/search', { params });
    return response.data;
  },

  // 식당 상세 정보
  getRestaurant: async (id) => {
    const response = await apiClient.get(`/api/restaurants/${id}`);
    return response.data;
  },

  // 위생평가 조회
  getHygieneReport: async (id) => {
    const response = await apiClient.get(`/api/restaurants/${id}/hygiene`);
    return response.data;
  },
};

export const predictionService = {
  // AI 안전도 예측
  predictSafetyScore: async (data) => {
    const response = await apiClient.post('/api/predict/safety-score', data);
    return response.data;
  },

  // 위험 요소 분석
  analyzeRiskFactors: async (restaurantId) => {
    const response = await apiClient.post('/api/predict/risk-analysis', {
      restaurant_id: restaurantId,
    });
    return response.data;
  },
};

export const chatService = {
  // 챗봇 대화
  sendMessage: async (data) => {
    const response = await apiClient.post('/api/chat', data);
    return response.data;
  },

  // 채팅 히스토리
  getChatHistory: async (sessionId) => {
    const response = await apiClient.get(`/api/chat/history/${sessionId}`);
    return response.data;
  },
};

export const voiceService = {
  // 음성 분석
  analyzeVoice: async (audioFile) => {
    const formData = new FormData();
    formData.append('audio_file', audioFile);
    
    const response = await apiClient.post('/api/voice/analyze', formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    });
    return response.data;
  },

  // 텍스트 음성 변환
  textToSpeech: async (text, language = 'ko-KR') => {
    const response = await apiClient.post('/api/voice/text-to-speech', {
      text,
      language,
    });
    return response.data;
  },
};

export const imageService = {
  // 이미지 위생 체크
  checkHygiene: async (imageFile) => {
    const formData = new FormData();
    formData.append('image_file', imageFile);
    
    const response = await apiClient.post('/api/image/hygiene-check', formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    });
    return response.data;
  },

  // 음식 안전성 분석
  analyzeFoodSafety: async (imageFile) => {
    const formData = new FormData();
    formData.append('image_file', imageFile);
    
    const response = await apiClient.post('/api/image/food-safety', formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    });
    return response.data;
  },
};
