from django.shortcuts import render, redirect
from .models import VinylRecord
from .forms import VinylRecordForm
from django.http import HttpResponse
from django.core import serializers
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.


@login_required(login_url='/login')
def show_main(request):
    vinyls = VinylRecord.objects.filter(user=request.user)
    context = {
        'name': request.user.username,
        'npm': '2306275286',
        'kelas': 'A',
        'aplikasi': "Reksa's Records",
        'vinyls': vinyls,
        'last_login': request.COOKIES.get('last_login')
    }
    return render(request, "main.html", context)


@login_required(login_url='/login')
def create_vinyl(request):
    form = VinylRecordForm(request.POST or None, request.FILES or None)

    if form.is_valid() and request.method == 'POST':
        vinyl_form = form.save(commit=False)
        vinyl_form.user = request.user
        vinyl_form.save()
        return redirect('main:show_main')

    context = {'form': form,
               'aplikasi': "Reksa's Records"}

    return render(request, "create_vinyl.html", context)


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    else:
        form = UserCreationForm()  # Unbound form
    context = {'form': form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
    else:
        form = AuthenticationForm()  # Unbound form
    context = {'form': form}
    return render(request, 'login.html', context)


def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return redirect('main:login')


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
