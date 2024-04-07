import React from 'react';
import { Card, CardMedia, CardContent, Typography, Rating } from '@mui/material';
import fifa from '../images/fifa.png'

const GameCard = (/*{ game }*/) => {
//   const { name, imageUrl, rating } = game;

  return (
    <Card sx={{ maxWidth: 230 }}>
      <CardMedia component="img" height="160" image={fifa}/*{imageUrl}*/ alt=/*{name}*/'fifa' />
      <CardContent>
        <Typography gutterBottom variant="h5" component="div">
          Fifa
        </Typography>
        <Rating name="game-rating" value=/*{rating}*/ '4' precision={0.5} readOnly />
      </CardContent>
    </Card>
  );
};

export default GameCard;