import React from 'react';
import { Container, Typography, Box } from '@mui/material';

const RestaurantDetailPage = () => {
  return (
    <Container maxWidth="lg" sx={{ py: 4 }}>
      <Typography variant="h4" component="h1" gutterBottom>
        식당 상세 정보
      </Typography>
      <Box>
        {/* TODO: 식당 상세 정보 구현 */}
        <Typography variant="body1">
          식당 상세 정보 페이지 구현 예정
        </Typography>
      </Box>
    </Container>
  );
};

export default RestaurantDetailPage;
