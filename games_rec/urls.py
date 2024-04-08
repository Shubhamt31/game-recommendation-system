from django.urls import path
from .views import GamesViewset, GenreViewset
from .scrape_images import get_game_images


urlpatterns = [
    path('genres/', GenreViewset.as_view()),
    path('games/', GamesViewset.as_view()),
    path('games/<int:id>', GamesViewset.as_view()),
    path('api/games/', get_game_images, name='get_game_images'),
]