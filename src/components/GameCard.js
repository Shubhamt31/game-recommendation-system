import React from 'react';
import { Card, CardMedia, CardContent, Typography, Rating } from '@mui/material';
// import fifa from '../images/fifa.png'

const GameCard = ({game}) => {
  const { title,image_url, rating } = game;

  return (
    <Card sx={{ maxWidth: 230 }}>
      <CardMedia component="img" height="160" image={image_url} alt={title} />
      <CardContent>
        <Typography gutterBottom variant="h5" component="div">
          {title}
        </Typography>
        <Rating name="game-rating" value={rating} precision={0.5} readOnly />
      </CardContent>
    </Card>
  );
};

export default GameCard;