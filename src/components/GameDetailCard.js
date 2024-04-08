import React from 'react';
import { Card, CardMedia, CardContent, Typography, Rating } from '@mui/material';
import { Button, Divider } from '@material-ui/core';
import { useNavigate } from 'react-router-dom';

const GameDetailCard = ({ game }) => {
  const { id, title, summary, image_url, rating, reviews_raw } = game;
  const navigate = useNavigate();
  return (
    <Card>
      <CardMedia component="img" height="360" image={image_url} alt={title} />
      <CardContent>
        <Typography gutterBottom variant="h5" component="div">
          {title}
        </Typography>
        <Rating name="game-rating" value={rating} precision={0.5} readOnly />
        <Typography style={{ fontSize: '20px' }}>
          {summary}
        </Typography>
        <Card>
          <CardContent>
            <Typography gutterBottom variant="h5" component="div">
              Reviews
            </Typography>
            {reviews_raw.map(rev => <React.Fragment key={rev}><Typography style={{ marginBottom: '20px' }}>{rev}</Typography>
              <Divider />
            </React.Fragment>)}
          </CardContent>
        </Card>
        <Button onClick={() => navigate(-1)}>Go Back to Search Result</Button>
      </CardContent>
    </Card>
  );
};

export default GameDetailCard;