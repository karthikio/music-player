from posixpath import join
from django.shortcuts import render
from django.http import JsonResponse
from .models import Music
import json
from django.core import serializers


def songsView(request):
  qs = Music.objects.all()
  serializer = serializers.serialize('json', qs)
  data = json.loads(serializer)
  return JsonResponse(data, safe=False)

