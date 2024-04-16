import React, { useEffect, useState } from 'react';
import { Card, CardMedia, CardContent, Typography, Rating } from '@mui/material';
import { Button, Divider, Grid } from '@material-ui/core';
import { useNavigate,useParams } from 'react-router-dom';
import { makeStyles } from '@material-ui/core/styles';
import GameCard from '../components/GameCard';
import axios from 'axios';
import config from '../config';

const useStyles = makeStyles((theme) => ({
  button: {
    marginTop: '1rem',
    backgroundColor: '#d32f2f',
    color: '#ffffff',
    '&:hover': {
      backgroundColor: '#b71c1c',
    },
}}));

const GameDetailCard = ({ game }) => {
  const { title, summary, image_url, rating, reviews_raw } = game;
  const [recomendations,setRecomendations] = useState([]);
  const { id } = useParams();
  const classes = useStyles();
  const navigate = useNavigate();
  const baseUrl = config.backendURL;
  useEffect(() => {
    axios.get(`${baseUrl}/games/${id}`).then((res) => {
      setRecomendations(res.data.recommended_games);
    })
  }, [id])
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
        <div>
          <h3>Recomendations:</h3>
          <Grid container spacing={1} className={classes.gridContainer}>
          {recomendations.map((recomendation) => (
            <Grid item xs={12} sm={6} md={3} key={recomendation.id} className={classes.gridItem}>
              <GameCard game={recomendation} />
            </Grid>
          ))}
          </Grid>
        </div>
        <Button variant="contained"
          className={classes.button}
          size="large" onClick={() => navigate(-1)}>Go Back to Search Result</Button>
      </CardContent>
    </Card>
  );
};

export default GameDetailCard;