import React from 'react';
import { Container, Typography, Box } from '@mui/material';

const DashboardPage = () => {
  return (
    <Container maxWidth="lg" sx={{ py: 4 }}>
      <Typography variant="h4" component="h1" gutterBottom>
        AI 위생 대시보드 📊
      </Typography>
      <Box>
        {/* TODO: 대시보드 구현 */}
        <Typography variant="body1">
          AI 위생 대시보드 구현 예정
        </Typography>
      </Box>
    </Container>
  );
};

export default DashboardPage;
