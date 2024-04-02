from django.urls import path
from .views import GamesViewset


urlpatterns = [
    path('games_rec/', GamesViewset.as_view()),
    path('games_rec/<int:id>', GamesViewset.as_view())
]