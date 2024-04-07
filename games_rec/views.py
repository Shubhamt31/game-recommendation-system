from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from . import models
from . import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework import status


class GamesViewset(APIView, PageNumberPagination):
    page_size=10
    def get(self, request, id=None):
        if id:
            item = models.Game.objects.get(id=id)
            serializer = serializers.GamesSerializer(item)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        queryset = models.Game.objects.all()
        title = request.query_params.get('title')
        if title:
            queryset = queryset.filter(title__contains=title)


        rating = request.query_params.get('rating')
        if rating:
            queryset = queryset.filter(rating__range=(float(rating), float(rating) + 0.9))


        genres = request.query_params.getlist('genres')
        if genres:
            queryset = queryset.filter(genres__name__in=genres)

        
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