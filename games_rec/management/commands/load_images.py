from django.core.management.base import BaseCommand
from games_rec.models import Game
import requests
from bs4 import BeautifulSoup

class Command(BaseCommand):
    help = 'Description of my command'

    def handle(self, *args, **kwargs):
        games = Game.objects.all()
        for game in games:
            search_url = f'https://images.search.yahoo.com/search/images;_ylt=Awr.170.whNmDr4U4gdXNyoA;_ylu=Y29sbwNncTEEcG9zAzEEdnRpZAMEc2VjA3BpdnM-?p={game.title}+vidieo+game&fr2=piv-web&fr=yfp-t-s#id=0&iurl=https%3A%2F%2Fstatic.bandainamcoent.eu%2Fhigh%2Felden-ring%2Felden-ring%2F00-page-setup%2Felden-ring-new-header-mobile.jpg&action=close'  
            response = requests.get(search_url)
            print(game.id)
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                images = soup.find_all('img')
                print(len(images))
                if len(images) > 15:
                    first_image = images[15]
                    print(first_image)
                    if first_image:
                        url = ''
                        if first_image.get('data-src'):
                            url = first_image['data-src']
                        elif first_image.get('src'):
                            url = first_image['src']
                        print(f'ur={url}')
                        game.image_url = url
                        game.save()
