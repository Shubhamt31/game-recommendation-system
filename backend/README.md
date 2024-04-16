
![Logo](https://res.cloudinary.com/dnzbo3wfx/image/upload/c_thumb,w_200,g_face/v1713116986/Screenshot_2024-04-14_231739_w4v9dr.png)

# Game Scout Backend

Welcome to Game Scout - your ultimate destination for discovering new games and making informed choices! Our frontend interface provides a seamless and intuitive experience for users to explore a vast array of games, complete with summaries, reviews, ratings, and personalized suggestions powered by cutting-edge machine learning models.
## About Game Recommendation Model

Our recommendation model suggests games based on a blend of their summaries and genres. Using TF-IDF vectorization, it quantifies textual data and computes cosine similarity scores. The model integrates both summary and genre similarities, with summaries weighted at 70% and genres at 30%. This approach provides personalized game recommendations for users, enhancing their gaming experience.

## Features

- **Game Recommendation**: Utilizes game summaries and genres for recommendations.
- **Hybrid Similarity Scoring**: Converts textual data to numerical representations, calculates game similarity via Cosine Similarity, and blends summary and genre similarities for personalized recommendations.
- **Filtering and Searching**: Additional features for enhanced user experience.
- **Django Integration**: Seamlessly integrates with Django web framework.
- **PostgreSQL Database**: Stores game data for efficient retrieval and management.
 





## App and Execution Flowcharts


![App Screenshot](https://res.cloudinary.com/dnzbo3wfx/image/upload/v1713297489/Screenshot_2024-04-17_012738_cdss3u.png)

![App Screenshot](https://res.cloudinary.com/dnzbo3wfx/image/upload/v1713206637/Screenshot_2024-04-16_001253_b95afv.png)

