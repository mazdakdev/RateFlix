from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=70)
class Movie(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    title = models.CharField(max_length=100)
    genres = models.ManyToManyField(Genre)
