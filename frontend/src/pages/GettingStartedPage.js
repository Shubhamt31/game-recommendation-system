import React from 'react';
import { Button, Link } from '@mui/material';
import bgImage from '../images/img.png';

const GettingStartedPage = () => {
  const handleClick = () => {
    window.location.href = '/search';
  };

  return (
    <div
      style={{
        backgroundImage: `url(${bgImage})`,
        backgroundSize: 'cover',
        backgroundPosition: 'center',
        height: '100vh',
        width: '100vw',
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'center',
      }}
    >
      <div
        style={{
          backgroundColor: 'rgba(255, 255, 255, 0.90)',
          padding: '2rem',
          borderRadius: '1rem',
          display: 'flex',
          flexDirection: 'column',
          justifyContent: 'center',
          alignItems: 'center',
        }}
      >
        <h1>Welcome to our Games Scouting App!</h1>
        <Button
          variant="contained"
          color="error"
          size="large"
          component={Link}
          to="/games"
          onClick={handleClick}
        >
          Get Started 
        </Button>
      </div>
    </div>
  );
};

export default GettingStartedPage;