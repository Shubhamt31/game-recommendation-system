from django.core.management.base import BaseCommand
import requests
import json
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
        print('start')
        with open('data/games.json', 'r') as file:
            games_input = json.load(file)
            print('Loading images from yahoo')
            for i in range(0,len(games_input),10):
                has_changes = False
                for item in games_input[i:i+10]:
                    print(f'Loading image for {item['id']} {item['title']}')
                    if 'image_url' in item:
                        continue
                    has_changes = True
                    search_url = f'https://images.search.yahoo.com/search/images?p={item['title']}+video+game'
                    response = requests.get(search_url)
                    if response.status_code == 200:
                        soup = BeautifulSoup(response.content, 'html.parser')
                        images = soup.find_all('img')
                        if len(images) > 15:
                            first_image = images[15]
                            if first_image:
                                url = first_image.get('data-src') or first_image.get('src')
                                item['image_url'] = url
                if has_changes:
                    with open('data/games.json', 'w') as file:
                        json.dump(games_input, file, indent=2)
        print('Images are loaded successfully')