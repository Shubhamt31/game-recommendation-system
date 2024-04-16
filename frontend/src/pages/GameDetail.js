import React, { useEffect, useState } from 'react';
import { Grid } from '@material-ui/core';
import bgImage from '../images/img.png';
import axios from 'axios';
import {  useParams } from 'react-router-dom';
import GameDetailCard from '../components/GameDetailCard';
import GameCard from '../components/GameCard';
import { makeStyles } from '@material-ui/core/styles';
import config from '../config';



const useStyles = makeStyles((theme) => ({
  form: {
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
  },
  button: {
    marginTop: '1rem',
    backgroundColor: '#d32f2f',
    color: '#ffffff',
    '&:hover': {
      backgroundColor: '#b71c1c',
    },
  },
  gridContainer: {
    padding: '2rem',
    [theme.breakpoints.down('sm')]: {
      flexDirection: 'column',
    },
  },
  gridItem: {
    marginBottom: '2rem',
    [theme.breakpoints.down('sm')]: {
      marginBottom: '1rem',
    },
  },
}));

const GameDetail = () => {
  const [game, setGame] = useState();
  const [recomendation,setRecomendation] = useState();
  const { id } = useParams();
  const classes = useStyles();
  // const navigate = useNavigate();
  const baseUrl = config.backendURL;
  useEffect(() => {
    axios.get(`${baseUrl}/games/${id}`).then((res) => {
      setGame(res.data.data);
      setRecomendation(res.data.recomendation);
    })
  }, [id])


  return (
    <div
      style={{
        backgroundImage: `url(${bgImage})`,
        backgroundSize: 'cover',
        backgroundPosition: 'center',
        height: '100%',
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'center',
      }}
    >
      <div
        style={{
          backgroundColor: 'rgba(255, 255, 255, 0.90)',
          borderRadius: '1rem',
          display: 'flex',
          flexDirection: 'column',
          justifyContent: 'center',
          alignItems: 'center',
          width: '80%',
          maxWidth: '1200px',
          padding: '2rem',
          boxSizing: 'border-box',
          margin: '40px'
        }}
      >
        {game && <GameDetailCard game={game} />}
      </div>
    </div>
  );
};

export default GameDetail;