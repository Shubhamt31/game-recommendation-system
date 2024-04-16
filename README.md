
![Logo](https://res.cloudinary.com/dnzbo3wfx/image/upload/c_thumb,w_200,g_face/v1713116986/Screenshot_2024-04-14_231739_w4v9dr.png)


# Game Scout Backend

Welcome to Game Scout - your ultimate destination for discovering new games and making informed choices! Our frontend interface provides a seamless and intuitive experience for users to explore a vast array of games, complete with summaries, reviews, ratings, and personalized suggestions powered by cutting-edge machine learning models.

## About Game Recommendation Model

Our recommendation model suggests games based on a blend of their summaries and genres. Using TF-IDF vectorization, it quantifies textual data and computes cosine similarity scores. The model integrates both summary and genre similarities, with summaries weighted at 70% and genres at 30%. This approach provides personalized game recommendations for users, enhancing their gaming experience.

## Features

- Search: Effortlessly find your desired games through our powerful search functionality.
- Summaries: Get quick insights into game details and summaries to make informed decisions.
- Reviews & Ratings: Explore user reviews and ratings to gauge the quality of games.
- Personalized Suggestions: Benefit from our machine learning algorithms that tailor suggestions based on your search history and preferences.

## Environment Variables

To run this project,

Copy the .env.example to .env and modify the values as per need.

## Setup and Execution flowdigram 


![App Screenshot](https://res.cloudinary.com/dnzbo3wfx/image/upload/v1713206636/Screenshot_2024-04-15_235552_zbfzau.png)

![App Screenshot](https://res.cloudinary.com/dnzbo3wfx/image/upload/v1713206637/Screenshot_2024-04-16_001253_b95afv.png)


## Installation

If you wish to use Windows as the host, it's a good idea to read through the
https://docs.docker.com/desktop/install/windows-install/

Once the docker is installed, go to the project directory and do `docker-compose up`.

    
## Demo

https://res.cloudinary.com/dnzbo3wfx/video/upload/v1713119545/Recording_2024-04-14_235943_zqdhme.mp4

