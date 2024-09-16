from django.shortcuts import render, redirect
from .models import VinylRecord
from .forms import VinylRecordForm
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
    form = VinylRecordForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('main:show_main')
    
    context = {'form' : form,
               'aplikasi' : "Reksa's Records"}
    
    return render(request, "create_vinyl.html", context)

def show_xml(request):
    vinyls = VinylRecord.objects.all()
    data = serializers.serialize('xml', vinyls)
    return HttpResponse(data, content_type='application/xml')

def show_json(request):
    vinyls = VinylRecord.objects.all()
    data = serializers.serialize('json', vinyls)
    return HttpResponse(data, content_type='application/json')

def show_xml_by_id(request, id):
    vinyls = VinylRecord.objects.filter(id=id)
    data = serializers.serialize('xml', vinyls)
    return HttpResponse(data, content_type='application/xml')

def show_json_by_id(request, id):
    vinyls = VinylRecord.objects.filter(id=id)
    data = serializers.serialize('json', vinyls)
    return HttpResponse(data, content_type='application/json')

