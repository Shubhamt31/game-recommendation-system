from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from . import models
from . import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework import status
import pickle

class GenreViewset(APIView):
    """
    API endpoint that allows viewing of genres or a specific genre by ID.
    """
    def get(self, request, id=None):
        """
        Retrieves either all genres or a specific genre by ID.
        """
        if id:
            # Retrieve a specific genre by ID
            item = models.Genre.objects.get(id=id)
            serializer = serializers.GenreSerializer(item)
            return Response({"status": "success", "data": serializer.data }, status=status.HTTP_200_OK)

        # Retrieve all genres
        queryset = models.Genre.objects.all().order_by('name')
        serializer = serializers.GenreSerializer(queryset, many=True)
        return Response({"status": "success", "data": serializer.data}) 

class GamesViewset(APIView, PageNumberPagination):
    """
    API endpoint that allows viewing of games with optional filtering and recommendation based on game by ID.
    """
    page_size=8

    def get(self, request, id=None):
        """
        Retrieves either game recommendation based on game by ID or games with optional filtering.
        """
        if id:
            # Retrieve a similar games by ID
            item = models.Game.objects.get(id=id)
            serializer = serializers.GamesSerializer(item)
            df = None
            combined_matrix = None
            with open('data/games_df.pkl', 'rb') as f:
                df = pickle.load(f)
            with open('data/combined_similarity.pkl', 'rb') as f:
                combined_matrix = pickle.load(f)

            curr_index = df[df['id'] == id].index[0]

            similarity = combined_matrix[curr_index]

            similar_game_indices = similarity.argsort()[::-1][1:9]
            recommended_games_id = df.iloc[similar_game_indices]['id'].tolist()
            recommended_games = models.Game.objects.filter(id__in=recommended_games_id)
            recommended_serializer = serializers.GamesSerializer(recommended_games, many=True)
            return Response({"status": "success", "data": serializer.data, "recommended_games": recommended_serializer.data}, status=status.HTTP_200_OK)

        # Retrieve all games
        queryset = models.Game.objects.all()

        # Optional filtering by title
        title = request.query_params.get('title')
        if title and title != '':
            queryset = queryset.filter(title__icontains=title)

        # Optional filtering by rating
        rating = request.query_params.get('rating')
        if rating  and rating != '':
            queryset = queryset.filter(rating__range=(float(rating), float(rating) + 0.9))

        # Optional filtering by genres
        genres = request.query_params.getlist('genres')
        if genres:
            genres = [i for i in genres if i ]
            if len(genres):
                queryset = queryset.filter(genres__in=genres)

        # Paginate the results
        results = self.paginate_queryset(queryset, request, view=self)
        serializer = serializers.GamesSerializer(results, many=True)
        return self.get_paginated_response(serializer.data)
