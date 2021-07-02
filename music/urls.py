from django.urls import path
from .views import jsonsongsView, jsonsongView, songsView, songPostView


urlpatterns = [
  path('json/songs/', jsonsongsView, name='json-songs-view'),
  path('json/song/<int:pk>/', jsonsongView, name='json-song-view'),

  path('music-player/', songsView, name='songs-view'),
  path('upload/', songPostView, name='song-post-view'),
]