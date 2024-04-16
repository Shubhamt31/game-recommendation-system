from django.urls import path
from .views import GamesViewset, GenreViewset

urlpatterns = [
    path('genres/', GenreViewset.as_view()),
    path('games/', GamesViewset.as_view()),
    path('games/<int:id>', GamesViewset.as_view()),
]