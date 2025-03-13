from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField
from django.db import models

class User(AbstractUser):
    age = models.IntegerField(null=True)
    gender = models.CharField(max_length=20, choices=[
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    ])
    favorite_genres = ArrayField(
        models.CharField(max_length=50),
        blank=True,
        null=True
    )

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey('movies.Movie', on_delete=models.CASCADE)
    rating = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'movie')