from django.core.management.base import BaseCommand
from games_rec.models import Game, Genre, Organization, Review
from datetime import datetime
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle

class Command(BaseCommand):
    """
    A management command to develop a machine learning model to suggest similar games.
    """

    help = 'Develop a ML model to suggest similar games'

    def handle(self, *args, **kwargs):
        """
        Handles the development of a machine learning model to suggest similar games.
        """
        # Retrieve all games from the database
        games = Game.objects.all()
        # Ensure summaries are not None
        for game in games:
            if game.summary is None:
                game.summary = ''

        # Prepare data for ML model
        games_data = list(games.values('id', 'title', 'genres_raw', 'summary'))
        df = pd.DataFrame(games_data)
        df['summary'] = df['summary'].fillna('')

        # Vectorize summaries and genres
        vectorizer = TfidfVectorizer(stop_words='english')
        summary_vectors = vectorizer.fit_transform(df['summary'])
        genre_vectors = vectorizer.fit_transform([' '.join(genres) for genres in df['genres_raw']])

        # Compute similarity matrices
        summary_similarity_matrix = cosine_similarity(summary_vectors)
        genre_similarity_matrix = cosine_similarity(genre_vectors)

        # Combine similarity matrices
        combined_similarity = 0.7 * summary_similarity_matrix + 0.3 * genre_similarity_matrix

        # Save data and model
        with open('data/games_df.pkl', 'wb') as f:
            pickle.dump(df, f)
        with open('data/combined_similarity.pkl', 'wb') as f:
            pickle.dump(combined_similarity, f)
