from django.core.management.base import BaseCommand
from games_rec.models import Game, Genre, Organization, Review
import json
from datetime import datetime

class Command(BaseCommand):
    """
    A management command to populate the database with data from JSON files.
    """

    help = 'Populates the database with data from JSON files.'

    def handle(self, *args, **kwargs):
        """
        Handles the population of database with data from JSON files.
        """
        # Load genres from JSON and create Genre objects
        with open('data/genres.json', 'r') as file:
            genres_input = json.load(file)
            genres = []
            for item in genres_input:
                if item['name']:
                    genres.append(Genre(name=item['name'], id=item['id']))
            try:
                Genre.objects.bulk_create(genres)
            except:
                pass
        
        # Load organizations from JSON and create Organization objects
        with open('data/organizations.json', 'r') as file:
            organizations_input = json.load(file)
            organizations = []
            for item in organizations_input:
                organizations.append(Organization(name=item['name'], id=item['id']))
            Organization.objects.bulk_create(organizations)
            
        # Load games from JSON and create Game objects
        with open('data/games.json', 'r') as file:
            games_input = json.load(file)
            for item in games_input:
                # Check if the game already exists in the database
                exists = Game.objects.filter(title=item['title']).count()
                if not exists:
                    # Create a new Game object
                    game = Game.objects.create(
                        title=item['title'],
                        release_date=datetime.fromtimestamp(item['release_date'] / 1000) if item['release_date'] else None,
                        organizations_raw=item['organizations'],
                        rating=item['rating'],
                        times_listed=item['times_listed'],
                        number_of_reviews=item['no_of_reviews'],
                        genres_raw=item['genres'],
                        summary=item['summary'],
                        plays=item['plays'],
                        playing=item['playing'],
                        backlogs=item['backlogs'],
                        wishlist=item['wishlist'],
                        reviews_raw=item['reviews'],
                    )
                    # Add organizations to the game
                    for name in item['organizations']:
                        org = Organization.objects.filter(name=name).first()
                        if org:
                            game.organizations.add(org)
                    # Add genres to the game
                    for name in item['genres']:
                        genre = Genre.objects.filter(name=name).first()
                        if genre:
                            game.genres.add(genre)
                    # Create reviews for the game
                    for comment in item['reviews']:
                        Review.objects.create(comment=comment, game=game)
