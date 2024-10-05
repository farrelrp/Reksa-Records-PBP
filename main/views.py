from django.shortcuts import get_object_or_404, render, redirect
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
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.conf import settings
# Create your views here.


@login_required(login_url='/login')
def show_main(request):
    
    context = {
        'name': request.user.username,
        'npm': '2306275286',
        'kelas': 'A',
        'aplikasi': "Reksa's Records",
        'last_login': request.COOKIES.get('last_login'),
        "MEDIA_URL": settings.MEDIA_URL,
        "genres": [genre[1] for genre in VinylRecord.GENRE_CHOICES], # Ambil genre dari VinylRecord
    }
    return render(request, "main.html", context)

@login_required(login_url='/login')
def show_favorites(request):
    vinyls = request.user.favorite_vinyls.all()
    context = {
        'name': request.user.username,
        'vinyls': vinyls,
        'last_login': request.COOKIES.get('last_login'),
        "MEDIA_URL": settings.MEDIA_URL,
    }
    return render(request, "favorites.html", context)


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

@csrf_exempt
@require_POST
def create_vinyl_ajax(request):
    if request.method == 'POST':
        album_name = request.POST.get("album_name")
        artist = request.POST.get("artist")
        release_year = request.POST.get("release_year")
        genre = request.POST.get("genre")
        price = request.POST.get("price")
        description = request.POST.get("description")

        vinyl = VinylRecord(
            album_name=album_name,
            artist=artist,
            release_year=release_year,
            genre=genre,
            price=price,
            description=description,
            user=request.user
        )

        vinyl.save()
        return HttpResponse(b"CREATED", status=201)
    return HttpResponseNotFound()

@csrf_exempt
@require_POST
def add_to_favorites_ajax(request, id):
    if request.method == 'POST':
        vinyl = get_object_or_404(VinylRecord, id=id)
        request.user.favorite_vinyls.add(vinyl)
        return HttpResponse(b"ADDED", status=201)
    return HttpResponseNotFound()


@csrf_exempt
@require_POST
def remove_from_favorites_ajax(request, id):
    if request.method == 'POST':
        vinyl = get_object_or_404(VinylRecord, id=id)
        request.user.favorite_vinyls.remove(vinyl)
        return HttpResponse(b"REMOVED", status=201)
    return HttpResponseNotFound()




@login_required(login_url='/login')
def add_to_favorites(request, id):
    vinyl = get_object_or_404(VinylRecord, id=id)
    request.user.favorite_vinyls.add(vinyl)
    return redirect('main:show_main')

@login_required(login_url='/login')
def remove_from_favorites(request, id):
    vinyl = get_object_or_404(VinylRecord, id=id)
    request.user.favorite_vinyls.remove(vinyl)
    return redirect('main:show_main')

def remove_from_favorites_fav(request, id):
    vinyl = get_object_or_404(VinylRecord, id=id)
    request.user.favorite_vinyls.remove(vinyl)
    return redirect('main:show_favorites')

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


@login_required(login_url='/login')
def show_json(request):
    query = request.GET.get('q', '')
    if query:
        vinyls = VinylRecord.objects.filter(
            Q(album_name__icontains=query) | 
            Q(artist__icontains=query) |
            Q(description__icontains=query)
        )
    else:
        vinyls = VinylRecord.objects.all()
    
    data = serializers.serialize('json', vinyls)
    return HttpResponse(data, content_type='application/json')

@login_required(login_url='/login')
def show_json_fav(request):
    query = request.GET.get('q', '')
    if query:
        vinyls = request.user.favorite_vinyls.filter(
            Q(album_name__icontains=query) | 
            Q(artist__icontains=query) |
            Q(description__icontains=query)
        )
    else:
        vinyls = request.user.favorite_vinyls.all()
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

def edit_vinyl(request, id):
    vinyl = VinylRecord.objects.get(id=id)
    form = VinylRecordForm(request.POST or None, instance=vinyl)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_main')
    context = {'form': form, 'vinyl': vinyl, 'aplikasi': "Reksa's Records"}
    return render(request, 'edit_vinyl.html', context)

def delete_vinyl(request, id):
    vinyl = VinylRecord.objects.get(id=id)
    vinyl.delete()
    return redirect('main:show_main')

# def show_favorites(request):
#     favorites = request.user.favorite_vinyls.all()
#     context = {'favorites': favorites}
#     return render(request, 'favorites.html', context) 
