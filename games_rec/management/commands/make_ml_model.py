from django.core.management.base import BaseCommand
from games_rec.models import Game, Genre, Organization, Review
from datetime import UTC, datetime
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle

class Command(BaseCommand):
    help = 'Develop a ML model to suggest similar games'

    def handle(self, *args, **kwargs):
        games = Game.objects.all()
        for game in games:
            if game.summary is None:
                print('changing')
                game.summary = ''

        games_data = list(games.values('id', 'title', 'genres_raw', 'summary'))
        df = pd.DataFrame(games_data)
        df['summary'] = df['summary'].fillna('')
        print(df.head())
        vectorizer = TfidfVectorizer(stop_words='english')
        summary_vectors = vectorizer.fit_transform(df['summary'])
        genre_vectors = vectorizer.fit_transform([' '.join(genres) for genres in df['genres_raw']])

        summary_similarity_matrix = cosine_similarity(summary_vectors)
        genre_similarity_matrix = cosine_similarity(genre_vectors)

        combined_similarity = 0.7 * summary_similarity_matrix + 0.3 * genre_similarity_matrix
        with open('data/games_df.pkl', 'wb') as f:
            pickle.dump(df, f)
        with open('data/combined_similarity.pkl', 'wb') as f:
            pickle.dump(combined_similarity, f)

        # pickle.dump(summary_similarity_matrix, 'data/summar_matrix.pd', 'wb')
        # pickle.dump(genre_similarity_matrix, 'data/summar_matrix.pd', 'wb')


