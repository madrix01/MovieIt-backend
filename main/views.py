from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import viewsets, permissions
from .models import * 
from .serializers import *

class GenreView(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerailizers
    permission_class = (permissions.IsAuthenticatedOrReadOnly)


def home(request):
    return JsonResponse("{'page':'home'}", safe=False)


