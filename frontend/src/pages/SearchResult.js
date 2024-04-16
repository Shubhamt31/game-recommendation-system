import React, { useEffect, useState } from 'react';
import { Button, Grid } from '@material-ui/core';
import { makeStyles } from '@material-ui/core/styles';
import bgImage from '../images/img.png';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import { useSearchParams } from 'react-router-dom';
import GameCard from '../components/GameCard';
import Pagination from '@mui/material/Pagination'
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

const SearchResult = () => {
  const classes = useStyles();
  const [ params ] = useSearchParams();
  const [games, setGames] = useState([]);
  const [count, setCount] = useState(0)
  const navigate = useNavigate();
  const baseUrl = config.backendURL;
  const loadData = (paramsN) => {
    axios.get(`${baseUrl}/games`, {params: paramsN}).then((res) => {
      setGames(res.data.results)
      setCount(res.data.count)
    })
  }
  useEffect(() => {
    loadData(params);
  }, [params])

  const changePage  = (page) => {
   params.set('page', page) 
   navigate(`/search-result?${params.toString()}`)
  }

  return (
    <div
      style={{
        backgroundImage: `url(${bgImage})`,
        backgroundSize: 'cover',
        backgroundPosition: 'center',
        height:'100%',
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
          margin:'40px'
        }}
      >
        <h1>Top Results:</h1>
        <Grid container spacing={1} className={classes.gridContainer}>
          {games.map((game) => (
            <Grid item xs={12} sm={6} md={3} key={game.id} className={classes.gridItem}>
              <GameCard game={game} />
            </Grid>
          ))}
        </Grid>
        <Pagination count={Math.ceil(count/10)} page={parseInt(params.get('page') ?? 1)} onChange={(e, page) => changePage(page)} color="error" />
        <Button
          variant="contained"
          className={classes.button}
          size="large"
          onClick={() => navigate('/search')}
        >
          Back to Search
        </Button>
      </div>
    </div>
  );
};

export default SearchResult;