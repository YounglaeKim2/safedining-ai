import React from 'react';
import { Container, Typography, Box } from '@mui/material';

const ChatPage = () => {
  return (
    <Container maxWidth="lg" sx={{ py: 4 }}>
      <Typography variant="h4" component="h1" gutterBottom>
        AI 챗봇 💬
      </Typography>
      <Box>
        {/* TODO: 챗봇 인터페이스 구현 */}
        <Typography variant="body1">
          AI 챗봇 인터페이스 구현 예정
        </Typography>
      </Box>
    </Container>
  );
};

export default ChatPage;
