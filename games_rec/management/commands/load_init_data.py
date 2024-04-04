from django.core.management.base import BaseCommand
from games_rec.models import Game, Genre, Organization, Review
import json
from datetime import UTC, datetime

class Command(BaseCommand):
    help = 'Description of my command'

    def handle(self, *args, **kwargs):
        with open('data/genres.json', 'r') as file:
            genres_input = json.load(file)
            genres = []
            for item in genres_input:
                genres.append(Genre(name=item['name'], id=item['id']))
            try:
                Genre.objects.bulk_create(genres)
            except:
                pass
        with open('data/organizations.json', 'r') as file:
            genres_input = json.load(file)
            genres = []
            for item in genres_input:
                genres.append(Organization(name=item['name'], id=item['id']))
            Organization.objects.bulk_create(genres)
            
        with open('data/games.json', 'r') as file:
            games_input = json.load(file)
            for item in games_input:
                game = Game.objects.create(
                    title=item['title'],
                    release_date=  datetime.fromtimestamp(item['release_date']/1000) if item['release_date'] else None,
                    organizations_raw=item['organizations'],
                    rating=item['rating'],
                    times_listed=item['times_listed'],
                    number_of_reviews=item['no_of_reviews'],
                    genres_raw=item['genres'],
                    summary=item['summary'],
                    reviews_raw=item['reviews'],
                )
                for name in item['organizations']:
                    org = Organization.objects.filter(name=name).first()
                    game.orgnaizations.add(org)
                for name in item['genres']:
                    genre = Genre.objects.filter(name=name).first()
                    game.genres.add(genre)
                for comment in item['reviews']:
                    Review.objects.create(comment=comment, game=game)