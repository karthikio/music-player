from posixpath import join
from django.shortcuts import redirect, render
from django.http import JsonResponse
from .models import Music
import json
from django.core import serializers
from .forms import MusicForm


def jsonsongsView(request):
  qs = Music.objects.all()
  serializer = serializers.serialize('json', qs)
  data = json.loads(serializer)
  return JsonResponse(data, safe=False)

def jsonsongView(request, pk):
  obj = [Music.objects.get(pk=pk)]
  serializer = serializers.serialize('json', obj)
  data = json.loads(serializer)
  return JsonResponse(data, safe=False)


def songPostView(request):
  form = MusicForm()
  if request.method == "POST":
    form = MusicForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      return redirect('songs-view')
  else: 
    form = MusicForm()
  
  context = {
    'form': form,
  }
  return render(request, 'music/upload.html', context)


def songsView(request):
  return render(request, 'music/songs.html', {})