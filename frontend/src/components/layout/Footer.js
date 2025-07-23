import React from 'react';
import { Box, Typography, Container, Link } from '@mui/material';

const Footer = () => {
  return (
    <Box
      component="footer"
      sx={{
        backgroundColor: 'primary.main',
        color: 'white',
        py: 3,
        mt: 'auto',
      }}
    >
      <Container maxWidth="lg">
        <Typography variant="body2" align="center">
          © 2024 SafeDining AI. AI가 지켜주는 안전한 식탁.
        </Typography>
        <Typography variant="body2" align="center" sx={{ mt: 1 }}>
          <Link href="#" color="inherit" sx={{ mx: 1 }}>
            개인정보처리방침
          </Link>
          |
          <Link href="#" color="inherit" sx={{ mx: 1 }}>
            이용약관
          </Link>
          |
          <Link href="#" color="inherit" sx={{ mx: 1 }}>
            고객센터
          </Link>
        </Typography>
      </Container>
    </Box>
  );
};

export default Footer;
