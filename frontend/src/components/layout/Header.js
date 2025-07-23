import React from 'react';
import {
  AppBar,
  Toolbar,
  Typography,
  Button,
  Box,
  IconButton,
  Badge,
} from '@mui/material';
import {
  Restaurant,
  Notifications,
  Search,
  Chat,
  Dashboard,
} from '@mui/icons-material';
import { useNavigate, useLocation } from 'react-router-dom';

const Header = () => {
  const navigate = useNavigate();
  const location = useLocation();

  const menuItems = [
    { label: '홈', path: '/', icon: <Restaurant /> },
    { label: '검색', path: '/search', icon: <Search /> },
    { label: '대시보드', path: '/dashboard', icon: <Dashboard /> },
    { label: '챗봇', path: '/chat', icon: <Chat /> },
  ];

  return (
    <AppBar position="fixed" elevation={2}>
      <Toolbar>
        <Typography
          variant="h6"
          component="div"
          sx={{ flexGrow: 1, cursor: 'pointer' }}
          onClick={() => navigate('/')}
        >
          🍽️ SafeDining AI 🤖
        </Typography>

        <Box sx={{ display: { xs: 'none', md: 'flex' } }}>
          {menuItems.map((item) => (
            <Button
              key={item.path}
              color="inherit"
              startIcon={item.icon}
              onClick={() => navigate(item.path)}
              sx={{
                backgroundColor:
                  location.pathname === item.path
                    ? 'rgba(255,255,255,0.1)'
                    : 'transparent',
              }}
            >
              {item.label}
            </Button>
          ))}
        </Box>

        <IconButton color="inherit">
          <Badge badgeContent={3} color="error">
            <Notifications />
          </Badge>
        </IconButton>
      </Toolbar>
    </AppBar>
  );
};

export default Header;
