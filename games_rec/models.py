from django.db import models
from django.contrib.postgres.fields import ArrayField
class Organization(models.Model):
    name = models.CharField(max_length=255)
class Genre(models.Model):
    name = models.CharField(max_length=255)

# Create your models here.
class Game(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField(null=True)
    organizations_raw = ArrayField(models.CharField(max_length=200))
    orgnaizations = models.ManyToManyField(Organization)
    rating = models.FloatField(null=True)
    times_listed = models.IntegerField()
    number_of_reviews = models.IntegerField()
    genres_raw = ArrayField(models.CharField(max_length=200))
    genres = models.ManyToManyField(Genre)
    summary = models.CharField(null=True, max_length=4000)
    reviews_raw = ArrayField(models.CharField(max_length=2000))

class Review(models.Model):
    comment = models.CharField(max_length=4000)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='reviews')