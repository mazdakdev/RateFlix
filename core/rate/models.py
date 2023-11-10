from django.db import models
from django.conf import settings
from movie.models import Movie
# from django_unixdatetimefield import UnixDateTimeField

class Rate(models.Model):
    rating = models.IntegerField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    imdb_user = models.IntegerField(null=True, blank=True)
    movie = models.ForeignKey(Movie, on_delete=models.SET_NULL, null=True)
    timestamp = models.BigIntegerField()