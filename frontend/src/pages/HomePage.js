import React, { useState } from 'react';
import {
  Container,
  Typography,
  Box,
  Grid,
  Card,
  CardContent,
  Button,
  TextField,
  Paper,
  Chip,
} from '@mui/material';
import {
  Security,
  Restaurant,
  Analytics,
  Chat,
  VoiceChat,
  CameraAlt,
} from '@mui/icons-material';

const HomePage = () => {
  const [searchQuery, setSearchQuery] = useState('');

  const features = [
    {
      icon: <Security color="primary" sx={{ fontSize: 40 }} />,
      title: 'AI 안전도 분석',
      description: '위생평가, 리뷰, 이미지를 종합한 AI 기반 안전도 예측',
    },
    {
      icon: <Restaurant color="primary" sx={{ fontSize: 40 }} />,
      title: '실시간 식당 검색',
      description: 'Naver Maps 연동으로 실시간 식당 정보 및 위치 검색',
    },
    {
      icon: <Analytics color="primary" sx={{ fontSize: 40 }} />,
      title: '위생 대시보드',
      description: '실시간 위생 등급, 위험 요소, 개선사항 분석',
    },
    {
      icon: <Chat color="primary" sx={{ fontSize: 40 }} />,
      title: 'AI 챗봇',
      description: 'Azure OpenAI 기반 식당 안전 상담 및 추천',
    },
    {
      icon: <VoiceChat color="primary" sx={{ fontSize: 40 }} />,
      title: '음성 검색',
      description: 'Azure Speech Services로 음성으로 식당 검색',
    },
    {
      icon: <CameraAlt color="primary" sx={{ fontSize: 40 }} />,
      title: '이미지 위생 체크',
      description: '사진 업로드로 즉시 위생 상태 분석',
    },
  ];

  const popularKeywords = [
    '강남역 맛집',
    '홍대 카페',
    '명동 한식',
    '이태원 양식',
    '신촌 치킨',
  ];

  const handleSearch = () => {
    if (searchQuery.trim()) {
      // TODO: 검색 페이지로 이동
      console.log('검색:', searchQuery);
    }
  };

  return (
    <Container maxWidth="lg" sx={{ py: 4 }}>
      {/* 히어로 섹션 */}
      <Box textAlign="center" sx={{ mb: 6 }}>
        <Typography variant="h2" component="h1" gutterBottom color="primary">
          SafeDining AI 🍽️🤖
        </Typography>
        <Typography variant="h5" color="text.secondary" gutterBottom>
          AI가 지켜주는 안전한 식탁
        </Typography>
        <Typography variant="body1" color="text.secondary" sx={{ mb: 4 }}>
          인공지능 기술로 식당의 위생 안전도를 분석하고 안전한 식사를 도와드립니다
        </Typography>

        {/* 검색 박스 */}
        <Paper elevation={3} sx={{ p: 2, mb: 3, maxWidth: 600, mx: 'auto' }}>
          <Box display="flex" gap={1}>
            <TextField
              fullWidth
              placeholder="식당명, 주소, 음식 종류를 검색해보세요..."
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              onKeyPress={(e) => e.key === 'Enter' && handleSearch()}
            />
            <Button
              variant="contained"
              onClick={handleSearch}
              sx={{ minWidth: 100 }}
            >
              검색
            </Button>
          </Box>
        </Paper>

        {/* 인기 검색어 */}
        <Box>
          <Typography variant="body2" color="text.secondary" sx={{ mb: 1 }}>
            인기 검색어:
          </Typography>
          <Box display="flex" justifyContent="center" flexWrap="wrap" gap={1}>
            {popularKeywords.map((keyword) => (
              <Chip
                key={keyword}
                label={keyword}
                onClick={() => setSearchQuery(keyword)}
                variant="outlined"
                size="small"
              />
            ))}
          </Box>
        </Box>
      </Box>

      {/* 주요 기능 */}
      <Typography variant="h4" component="h2" textAlign="center" gutterBottom>
        주요 기능
      </Typography>
      <Grid container spacing={3} sx={{ mb: 6 }}>
        {features.map((feature, index) => (
          <Grid item xs={12} md={6} lg={4} key={index}>
            <Card
              sx={{
                height: '100%',
                display: 'flex',
                flexDirection: 'column',
                textAlign: 'center',
                transition: 'transform 0.2s',
                '&:hover': {
                  transform: 'translateY(-4px)',
                },
              }}
            >
              <CardContent sx={{ flexGrow: 1, p: 3 }}>
                <Box sx={{ mb: 2 }}>{feature.icon}</Box>
                <Typography variant="h6" component="h3" gutterBottom>
                  {feature.title}
                </Typography>
                <Typography variant="body2" color="text.secondary">
                  {feature.description}
                </Typography>
              </CardContent>
            </Card>
          </Grid>
        ))}
      </Grid>

      {/* CTA 섹션 */}
      <Box textAlign="center" sx={{ py: 4, backgroundColor: '#f5f5f5', borderRadius: 2 }}>
        <Typography variant="h5" gutterBottom>
          지금 바로 시작해보세요!
        </Typography>
        <Typography variant="body1" color="text.secondary" sx={{ mb: 3 }}>
          AI가 분석한 안전한 식당을 찾아보세요
        </Typography>
        <Button
          variant="contained"
          size="large"
          onClick={() => setSearchQuery('')}
          sx={{ mr: 2 }}
        >
          식당 검색하기
        </Button>
        <Button variant="outlined" size="large">
          AI 챗봇 체험
        </Button>
      </Box>
    </Container>
  );
};

export default HomePage;
