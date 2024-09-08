from django.db import models

# Create your models here.
class VinylRecord(models.Model):
    image = models.ImageField(upload_to='images/' , default='images/3b921c51dc99d9fb2be192af3ec14f72.jpg')
    album_name = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.album_name
