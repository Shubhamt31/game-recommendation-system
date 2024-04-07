import React, { useEffect, useState } from 'react';
import { makeStyles } from '@material-ui/core/styles';
import axios from 'axios';
import {  useSearchParams } from 'react-router-dom';
import GameCard from '../components/GameCard';

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
}));

const SearchResult = () => {
  const classes = useStyles();
  const [ params ] = useSearchParams();
  const [genres, setGenres] = useState([]);
  const [games, setGames] = useState([]);
  const [ratings, setRatings] = useState([]);
  const baseUrl = 'http://localhost:8000/api';
  useEffect(() => {
    axios.get(`${baseUrl}/games`, {params}).then((res) => {
      setGames(res.data.results)
    })
  }, [params])

  return games.map((game) => (<GameCard key={game.id} game={game} />));
};

export default SearchResult;