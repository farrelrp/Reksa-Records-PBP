from django.forms import ModelForm
from main.models import VinylRecord

class VinylRecordForm(ModelForm):
    class Meta:
        model = VinylRecord
        fields = ['image', 'album_name', 'artist', 'price', 'description']