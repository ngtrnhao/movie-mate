from django.db import models
from django.contrib.postgres.fields import ArrayField

class Movie(models.Model):
    title = models.CharField(max_length=255)
    overview = models.TextField()
    release_date = models.DateField()
    genres = ArrayField(models.CharField(max_length=50))
    actors = ArrayField(models.CharField(max_length=255))
    directors = models.CharField(max_length=255)
    poster_url = models.URLField()
    imdb_rating = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
# Create your models here.
