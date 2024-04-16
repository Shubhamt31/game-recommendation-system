from rest_framework import serializers
from .models import Game, Genre

class GamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        # field = ('title', 'release_date', 'team','ratings', 'times_listed', 'number_of_reviews','genres', 'summary', 'reviews','plays', 'playing','backlogs', 'wishlist')
        fields = '__all__'

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        # field = ('title', 'release_date', 'team','ratings', 'times_listed', 'number_of_reviews','genres', 'summary', 'reviews','plays', 'playing','backlogs', 'wishlist')
        fields = '__all__'