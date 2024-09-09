from django.shortcuts import render
from .models import VinylRecord

# Create your views here.
def show_main(request):
    vinyls = VinylRecord.objects.all()
    context = {
        'name': 'Farrel Reksa Prawira',
        'npm' : '2306275286',
        'kelas' : 'A',
        'aplikasi' : "Reksa's Records",
        'vinyls' : vinyls
    }
    return render(request, "main.html", context)