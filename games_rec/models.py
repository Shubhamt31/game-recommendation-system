from django.db import models

# Create your models here.
class Games(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.CharField(max_length=300)
    team = models.CharField(max_length=300)
    rating = models.CharField(max_length=300)
    times_listed = models.CharField(max_length=300)
    number_of_reviews = models.CharField(max_length=300)
    genres = models.CharField(max_length=300)
    summary = models.CharField(max_length=300)
    reviews = models.CharField(max_length=300)
    plays = models.CharField(max_length=300)
    playing = models.CharField(max_length=300)
    backlogs = models.CharField(max_length=300)
    wishlist = models.CharField(max_length=300)