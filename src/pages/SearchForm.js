import React, { useState } from 'react';
import { Button, Checkbox, FormControlLabel, TextField } from '@material-ui/core';
import { makeStyles } from '@material-ui/core/styles';
import bgImage from '../images/img.png';

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

const SearchPage = () => {
  const classes = useStyles();
  const [genres, setGenres] = useState([]);

  const handleChange = (event) => {
    const { name, checked } = event.target;
    if (checked) {
      setGenres([...genres, name]);
    } else {
      setGenres(genres.filter((genre) => genre !== name));
    }
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    console.log('Searching for games with genres:', genres);
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
          margin:'4rem',
          alignItems: 'center',
        }}
      >
        <h1>Search for Games</h1>
        <form className={classes.form} onSubmit={handleSubmit}>
          <TextField
            label="Search by title"
            variant="outlined"
            fullWidth
            margin="normal"
          />
          <div>
            <h5>Genres:</h5>
            {[
              'Adventure',
              'RPG',
              'Brawler',
              'Indie',
              'Turn Based Strategy',
              'Platform',
              'Simulator',
              'Strategy',
              'Puzzle',
              'Shooter',
              'Music',
              'Fighting',
              'Arcade',
              'Visual Novel',
              'Card & Board Game',
              'Tactical',
              'Racing',
              'Point-and-Click',
              'MOBA',
              'Sport',
              'Real Time Strategy',
              'Quiz/Trivia',
              'Pinball',
            ].map((genre) => (
              <FormControlLabel
                key={genre}
                control={<Checkbox name={genre} onChange={handleChange} />}
                label={genre}
              />
            ))}
          </div>
          <div>
            
          </div>
          <Button
            variant="contained"
            className={classes.button}
            size="large"
            type="submit"
          >
            Search
          </Button>
        </form>
      </div>
    </div>
  );
};

export default SearchPage;