from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=70)
class Movie(models.Model):
    title = models.CharField(max_length=100)
    tconst = models.CharField(max_length=9)
    is_adult = models.BooleanField()
    start_year = models.IntegerField(null=True)
    genres = models.ManyToManyField(Genre)
