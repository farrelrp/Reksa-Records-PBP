from django.db import models

# Create your models here.
class VinylRecord(models.Model):
    album_name = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.album_name
    
