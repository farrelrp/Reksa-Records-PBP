from django.shortcuts import render, redirect
from .models import VinylRecord
from django.http import HttpResponse
from django.core import serializers

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

def create_vinyl(request):
    form = VinylRecordForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('main:show_main')
    
    context = {'form' : form}
    
    return render(request, "create_vinyl.html", context)
