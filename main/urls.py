from django.urls import path
from main.views import show_main, create_vinyl, show_xml, show_json, show_xml_by_id, show_json_by_id, register, login_user, logout_user, add_to_favorites, remove_from_favorites, edit_vinyl, delete_vinyl, show_favorites, remove_from_favorites_fav
from main.views import create_vinyl_ajax, add_to_favorites_ajax, remove_from_favorites_ajax, show_json_fav
app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create_vinyl/', create_vinyl, name='create_vinyl'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('add_to_favorites/<str:id>/', add_to_favorites, name='add_to_favorites'),
    path('remove_from_favorites/<str:id>/', remove_from_favorites, name='remove_from_favorites'),
    path('edit_vinyl/<str:id>/', edit_vinyl, name='edit_vinyl'),
    path('delete_vinyl/<str:id>/', delete_vinyl, name='delete_vinyl'),
    path('favorites/', show_favorites, name='show_favorites'),
    path('remove_from_favorites_fav/<str:id>/', remove_from_favorites_fav, name='remove_from_favorites_fav'),
    path('create_vinyl_ajax/', create_vinyl_ajax, name='create_vinyl_ajax'),
    path('add_to_favorites_ajax/<str:id>/', add_to_favorites_ajax, name='add_to_favorites_ajax'),
    path('remove_from_favorites_ajax/<str:id>/', remove_from_favorites_ajax, name='remove_from_favorites_ajax'),
    path('json_fav/', show_json_fav, name='show_json_fav'),
]