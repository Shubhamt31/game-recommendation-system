from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from . import models
from . import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework import status
from .scrape_images import scrape_first_image

class GenreViewset(APIView):
    def get(self, request, id=None):
        if id:
            item = models.Genre.objects.get(id=id)
            serializer = serializers.GenreSerializer(item)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        queryset = models.Genre.objects.all().order_by('name')
        serializer = serializers.GenreSerializer(queryset, many=True)
        return Response({"status": "success", "data": serializer.data}) 

class GamesViewset(APIView, PageNumberPagination):
    page_size=8

    def get_image_url(self, game_name):
        return scrape_first_image(game_name)
    
    def get(self, request, id=None):
        if id:
            item = models.Game.objects.get(id=id)
            serializer = serializers.GamesSerializer(item)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

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
        serialized_data = serializer.data
        for game_data in serialized_data:
            game_name = game_data.get('title') 
            if game_name:
                game_data['image_url'] = self.get_image_url(game_name)
        return self.get_paginated_response(serialized_data)

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