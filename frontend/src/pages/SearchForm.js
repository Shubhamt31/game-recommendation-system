import React, { useEffect, useState } from 'react';
import { Button, Checkbox, FormControlLabel, Radio, RadioGroup, TextField } from '@material-ui/core';
import { makeStyles } from '@material-ui/core/styles';
import bgImage from '../images/img.png';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
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
}));

const SearchPage = () => {
  const classes = useStyles();
  const [title, setTitle] = useState()
  const [selectedGenres, setSelectedGenres] = useState([]);
  const [genres, setGenres] = useState([]);
  const [selectedRating, setSelectedRating] = useState('');
  const navigate = useNavigate();
  const baseUrl = config.backendURL;
  useEffect(() => {
    axios.get(`${baseUrl}/genres/`).then((res) => {
      setGenres(res.data.data)
    })
  }, [])
  const handleChange = (event) => {
    const { value, checked } = event.target;
    if (checked) {
      setSelectedGenres([...selectedGenres, value]);
    } else {
      setSelectedGenres(selectedGenres.filter((genre) => genre !== parseInt(value)));
    }
  };
  const handleChangeRating = (event) => {
    const { value, checked } = event.target;
    if (checked) {
      setSelectedRating(parseInt(value));
    } else {
      setSelectedRating('');
    }
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    const params = new URLSearchParams()
    if (selectedGenres.length) {
      selectedGenres.forEach(genre => params.append('genres', genre))
    }
    if (title) {
      params.append('title', title)
    }
    if (selectedRating) {
      params.append('rating', selectedRating)
    }
    navigate({ pathname: '/search-result', search: '?' + params.toString() })
  };

  

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
          padding: '2rem',
          borderRadius: '1rem',
          display: 'flex',
          flexDirection: 'column',
          justifyContent: 'center',
          margin: '4rem',
          overflowX: 'hidden',
          overflowY: 'hidden',
          alignItems: 'center',
        }}
      >
        <h1>Search for Games</h1>
        <form className={classes.form} onSubmit={handleSubmit}>
          <TextField
            label="Search by title"
            variant="outlined"
            fullWidth
            onChange={(e) => setTitle(e.target.value)}
            margin="normal"
          />
          <div>
            <h5>Genres:</h5>
            {genres.map((genre) => (
              <FormControlLabel
                key={genre.id}
                control={<Checkbox name='genre' onChange={handleChange} />}
                value={genre.id}
                label={genre.name}
              />
            ))}
            <h5>Ratings:</h5>
            <RadioGroup
              value={selectedRating}
              onChange={(e) => handleChangeRating(e)}
              name='ratings'
              row
            >
              {[
                { label: '5 ', value: 5 }, { label: '4+ ', value: 4 }, { label: '3+ ', value: 3 }, { label: '2+', value: 2 }, { label: '1', value: 1 }
              ].map((rating) => (
                <FormControlLabel
                  key={rating.value}
                  value={rating.value}
                  control={<Radio />}
                  label={rating.label}
                />
              ))}
            </RadioGroup>
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