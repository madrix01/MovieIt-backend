from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import viewsets, permissions
from .models import * 
from .serializers import *
from .forms import *

class GenreView(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerailizers
    permission_class = (permissions.IsAuthenticatedOrReadOnly)


def home(request):
    return JsonResponse("{'page':'home'}", safe=False)


def user_form(request):
    if request.method == 'POST':
        form = GenreForm(request.POST):
        if form.is_valid():
            name = form.cleaned_data['name']
            adventure = form.cleaned_data['adventure']
            horror = form.cleaned_data['horror']
            crime = form.cleaned_data['crime']
            romance = form.cleaned_data['romance']
            children = form.cleaned_data['children']
            fantasy = form.cleaned_data['fantasy']
            command = form.cleaned_data['command']
            thriller = form.cleaned_data['thriller']
            action = form.cleaned_data['action']
            drama = form.cleaned_data['drama']
            animation = form.cleaned_data['animation']
            x = list[adventure, horror, crime, romance, children, fantasy, command, thriller, action, drama, animation]
            for i in range(11):
                if list[i] == 'True':
                    print(list[i])
                    