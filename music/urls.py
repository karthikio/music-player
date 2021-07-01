from django.urls import path
from .views import songsView


urlpatterns = [
  path('', songsView, name='songs-view'),
]