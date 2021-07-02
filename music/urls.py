from django.urls import path
from .views import JsonsongsView, JsonsongView, songsView


urlpatterns = [
  path('json/songs/', JsonsongsView, name='json-songs-view'),
  path('json/song/<int:pk>/', JsonsongView, name='json-song-view'),

  path('music-player/', songsView, name='songs-view'),
]