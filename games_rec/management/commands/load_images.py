from django.core.management.base import BaseCommand
from games_rec.models import Game
import requests
from bs4 import BeautifulSoup

class Command(BaseCommand):
    """
    A management command to fetch and update image URLs for games from Yahoo image search.
    """

    help = 'Fetches and updates image URLs for games from Yahoo image search.'

    def handle(self, *args, **kwargs):
        """
        Fetches and updates image URLs for games.
        """
        games = Game.objects.all()
        for game in games:
            if game.image_url:
                continue
            search_url = f'https://images.search.yahoo.com/search/images?p={game.title}+video+game'
            response = requests.get(search_url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                images = soup.find_all('img')
                if len(images) > 15:
                    first_image = images[15]
                    if first_image:
                        url = first_image.get('data-src') or first_image.get('src')
                        game.image_url = url
                        game.save()
