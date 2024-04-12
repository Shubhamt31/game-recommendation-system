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
    def get(self, request, id=None):
        if id:
            item = models.Genre.objects.get(id=id)
            serializer = serializers.GenreSerializer(item)
            return Response({"status": "success", "data": serializer.data }, status=status.HTTP_200_OK)

        queryset = models.Genre.objects.all().order_by('name')
        serializer = serializers.GenreSerializer(queryset, many=True)
        return Response({"status": "success", "data": serializer.data}) 

class GamesViewset(APIView, PageNumberPagination):
    page_size=8

    def get(self, request, id=None):
        if id:
            item = models.Game.objects.get(id=id)
            serializer = serializers.GamesSerializer(item)
            df = None
            combined_matrix = None
            with open('data/games_df.pkl', 'rb') as f:
                df = pickle.load(f)
            with open('data/combined_similarity.pkl', 'rb') as f:
                combined_matrix = pickle.load(f)

            title_index = df[df['id'] == 1].index[0]

            similarity = combined_matrix[title_index]

            similar_game_indices = similarity.argsort()[::-1][1:10]
            recommended_games_id = df.iloc[similar_game_indices]['id'].tolist()
            recommended_games = models.Game.objects.filter(id__in=recommended_games_id)
            recommended_serializer = serializers.GamesSerializer(recommended_games, many=True)
            return Response({"status": "success", "data": serializer.data, "recommended_games": recommended_serializer.data}, status=status.HTTP_200_OK)

        queryset = models.Game.objects.all()
        title = request.query_params.get('title')
        if title and title != '':
            queryset = queryset.filter(title__icontains=title)


        rating = request.query_params.get('rating')
        if rating  and rating != '':
            queryset = queryset.filter(rating__range=(float(rating), float(rating) + 0.9))


        genres = request.query_params.getlist('genres')
        if genres:
            genres = [i for i in genres if i ]
            if len(genres):
                queryset = queryset.filter(genres__in=genres)

        
        results = self.paginate_queryset(queryset, request, view=self)
        serializer = serializers.GamesSerializer(results, many=True)
        return self.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = serializers.GamesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id=None):
        item = models.Game.objects.get(id=id)
        serializer = serializers.GamesSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None):
        item = models.Game.objects.filter(id=id)
        print(item)
        item.delete()
        return Response({"status": "success", "data": "Item Deleted"})