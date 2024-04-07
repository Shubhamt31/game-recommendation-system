import React from 'react';
import { Card, CardMedia, CardContent, Typography, Rating } from '@mui/material';
import fifa from '../images/fifa.png'

const GameCard = ({game}) => {
  const { title, summary, rating } = game;

  return (
    <Card sx={{ maxWidth: 530 }}>
      <CardMedia component="img" height="160" image={fifa}/*{imageUrl}*/ alt=/*{name}*/'fifa' />
      <CardContent>
        <Typography gutterBottom variant="h5" component="div">
          {title}
        </Typography>
        <Rating name="game-rating" value={rating} precision={0.5} readOnly />
        <div>{summary}</div>
      </CardContent>
    </Card>
  );
};

export default GameCard;