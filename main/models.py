from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.
class VinylRecord(models.Model):
    GENRE_CHOICES = [
        ('rock', 'Rock'),
        ('pop', 'Pop'),
        ('jazz', 'Jazz'),
        ('classical', 'Classical'),
        ('hiphop', 'Hip Hop'),
        ('indie', 'Indie'),
        ('electronic', 'Electronic'),
        ('country', 'Country'),
        ('rhythm_and_blues', 'Rhythm and Blues'),
        ('other', 'Other'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.ImageField(upload_to='')
    album_name = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    genre = models.CharField(max_length=100, choices=GENRE_CHOICES)
    price = models.IntegerField()
    description = models.CharField(max_length=100)
    favorited_by = models.ManyToManyField(User, related_name='favorite_vinyls', blank=True)

    def __str__(self):
        return self.album_name
    
    