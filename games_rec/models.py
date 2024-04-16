from django.db import models
from django.contrib.postgres.fields import ArrayField

class Organization(models.Model):
    """
    Model to represent organizations associated with games.
    """
    name = models.CharField(max_length=255)

class Genre(models.Model):
    """
    Model to represent genres of games.
    """
    name = models.CharField(max_length=255)

class Game(models.Model):
    """
    Model to represent a game.
    """
    title = models.CharField(max_length=100)
    release_date = models.DateField(null=True)
    organizations_raw = ArrayField(models.CharField(max_length=200))
    organizations = models.ManyToManyField(Organization)
    rating = models.FloatField(null=True)
    times_listed = models.IntegerField()
    number_of_reviews = models.IntegerField()
    genres_raw = ArrayField(models.CharField(max_length=200))
    genres = models.ManyToManyField(Genre, related_name='games')
    summary = models.CharField(null=True, max_length=4000)
    reviews_raw = ArrayField(models.CharField(max_length=2000))
    plays = models.IntegerField()
    playing = models.IntegerField()
    backlogs = models.IntegerField()
    wishlist = models.IntegerField()
    image_url = models.CharField(max_length=2000, null=True)

class Review(models.Model):
    """
    Model to represent a review of a game.
    """
    comment = models.CharField(max_length=4000)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='reviews')
