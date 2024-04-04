from django.urls import path
from .views import GamesViewset


urlpatterns = [
    path('games/', GamesViewset.as_view()),
    path('games/<int:id>', GamesViewset.as_view())
]