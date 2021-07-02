from posixpath import join
from django.shortcuts import redirect, render
from django.http import JsonResponse
from .models import Music
import json
from django.core import serializers


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


def jsonPostview(request):
  # if request.method == "POST":
  pass


def songsView(request):
  return render(request, 'music/songs.html', {})