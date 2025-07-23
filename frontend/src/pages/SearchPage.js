import React, { useState } from 'react';
import {
  Container,
  Typography,
  Box,
  Grid,
  TextField,
  Button,
  Card,
  CardContent,
  Chip,
  Paper,
  List,
  ListItem,
  ListItemText,
  Divider,
} from '@mui/material';
import {
  Search,
  LocationOn,
  Star,
  Security,
} from '@mui/icons-material';

const SearchPage = () => {
  const [searchQuery, setSearchQuery] = useState('');
  const [searchResults, setSearchResults] = useState([]);
  const [isSearching, setIsSearching] = useState(false);

  // 더미 검색 결과
  const dummyResults = [
    {
      id: 'rest_001',
      name: '맛있는 한식당',
      address: '서울시 강남구 테헤란로 123',
      category: '한식',
      safetyScore: 87.5,
      hygieneGrade: '우수',
      distance: 250,
      rating: 4.5,
    },
    {
      id: 'rest_002',
      name: '깨끗한 카페',
      address: '서울시 강남구 강남대로 456',
      category: '카페',
      safetyScore: 92.0,
      hygieneGrade: '우수',
      distance: 480,
      rating: 4.7,
    },
    // 더 많은 더미 데이터...
  ];

  const handleSearch = async () => {
    if (!searchQuery.trim()) return;

    setIsSearching(true);
    // TODO: 실제 API 호출
    setTimeout(() => {
      setSearchResults(dummyResults);
      setIsSearching(false);
    }, 1000);
  };

  const getSafetyColor = (score) => {
    if (score >= 90) return 'success';
    if (score >= 80) return 'warning';
    if (score >= 70) return 'info';
    return 'error';
  };

  const getSafetyLabel = (score) => {
    if (score >= 90) return '매우 안전';
    if (score >= 80) return '안전';
    if (score >= 70) return '보통';
    return '주의';
  };

  return (
    <Container maxWidth="lg" sx={{ py: 4 }}>
      <Typography variant="h4" component="h1" gutterBottom>
        식당 검색 🔍
      </Typography>

      {/* 검색 박스 */}
      <Paper elevation={2} sx={{ p: 3, mb: 4 }}>
        <Grid container spacing={2} alignItems="center">
          <Grid item xs={12} md={8}>
            <TextField
              fullWidth
              placeholder="식당명, 주소, 음식 종류를 입력하세요"
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              onKeyPress={(e) => e.key === 'Enter' && handleSearch()}
              InputProps={{
                startAdornment: <Search sx={{ mr: 1, color: 'text.secondary' }} />,
              }}
            />
          </Grid>
          <Grid item xs={12} md={2}>
            <Button
              fullWidth
              variant="contained"
              onClick={handleSearch}
              disabled={isSearching}
              sx={{ height: 56 }}
            >
              {isSearching ? '검색 중...' : '검색'}
            </Button>
          </Grid>
          <Grid item xs={12} md={2}>
            <Button
              fullWidth
              variant="outlined"
              sx={{ height: 56 }}
            >
              필터
            </Button>
          </Grid>
        </Grid>
      </Paper>

      {/* 검색 결과 */}
      {searchResults.length > 0 && (
        <Box>
          <Typography variant="h6" gutterBottom>
            검색 결과 ({searchResults.length}건)
          </Typography>
          
          <Grid container spacing={3}>
            {searchResults.map((restaurant) => (
              <Grid item xs={12} key={restaurant.id}>
                <Card elevation={2} sx={{ '&:hover': { elevation: 4 } }}>
                  <CardContent>
                    <Grid container spacing={2} alignItems="center">
                      <Grid item xs={12} md={6}>
                        <Typography variant="h6" component="h3" gutterBottom>
                          {restaurant.name}
                        </Typography>
                        <Box display="flex" alignItems="center" sx={{ mb: 1 }}>
                          <LocationOn fontSize="small" color="text.secondary" />
                          <Typography variant="body2" color="text.secondary" sx={{ ml: 0.5 }}>
                            {restaurant.address}
                          </Typography>
                        </Box>
                        <Box display="flex" alignItems="center" gap={1}>
                          <Chip label={restaurant.category} size="small" />
                          <Typography variant="body2" color="text.secondary">
                            {restaurant.distance}m
                          </Typography>
                          <Box display="flex" alignItems="center">
                            <Star fontSize="small" color="warning" />
                            <Typography variant="body2" sx={{ ml: 0.5 }}>
                              {restaurant.rating}
                            </Typography>
                          </Box>
                        </Box>
                      </Grid>
                      
                      <Grid item xs={12} md={3}>
                        <Box textAlign="center">
                          <Typography variant="body2" color="text.secondary">
                            AI 안전도 점수
                          </Typography>
                          <Typography variant="h4" color="primary">
                            {restaurant.safetyScore}
                          </Typography>
                          <Chip
                            label={getSafetyLabel(restaurant.safetyScore)}
                            color={getSafetyColor(restaurant.safetyScore)}
                            size="small"
                          />
                        </Box>
                      </Grid>
                      
                      <Grid item xs={12} md={3}>
                        <Box textAlign="center">
                          <Typography variant="body2" color="text.secondary">
                            위생 등급
                          </Typography>
                          <Chip
                            label={restaurant.hygieneGrade}
                            color="primary"
                            sx={{ mb: 1 }}
                          />
                          <br />
                          <Button
                            variant="contained"
                            size="small"
                            startIcon={<Security />}
                          >
                            상세 보기
                          </Button>
                        </Box>
                      </Grid>
                    </Grid>
                  </CardContent>
                </Card>
              </Grid>
            ))}
          </Grid>
        </Box>
      )}

      {/* 검색 결과가 없을 때 */}
      {searchResults.length === 0 && !isSearching && (
        <Paper elevation={1} sx={{ p: 4, textAlign: 'center' }}>
          <Typography variant="h6" color="text.secondary" gutterBottom>
            검색 결과가 없습니다
          </Typography>
          <Typography variant="body2" color="text.secondary">
            다른 키워드로 검색해보세요
          </Typography>
        </Paper>
      )}
    </Container>
  );
};

export default SearchPage;
