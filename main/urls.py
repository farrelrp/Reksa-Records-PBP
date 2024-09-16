from django.urls import path
from main.views import show_main, create_vinyl

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create_vinyl/', create_vinyl, name='create_vinyl')
]