from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import viewsets, permissions
from .models import * 
from .serializers import *
from .forms import *
from django.db.models import Q

class GenreView(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerailizers
    permission_class = (permissions.IsAuthenticatedOrReadOnly)


def home(request):
    return JsonResponse("{'page':'home'}", safe=False)


def user_form(request):
    if request.method == 'POST':
        form = GenreForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            adventure = form.cleaned_data['adventure']
            horror = form.cleaned_data['horror']
            crime = form.cleaned_data['crime']
            romance = form.cleaned_data['romance']
            children = form.cleaned_data['children']
            fantasy = form.cleaned_data['fantasy']
            comedy = form.cleaned_data['comedy']
            thriller = form.cleaned_data['thriller']
            action = form.cleaned_data['action']
            drama = form.cleaned_data['drama']
            animation = form.cleaned_data['animation']
            x = [("adventure", adventure), ("horror", horror), ("crime", crime), ("romance", romance), ("children", children), ("fantasy", fantasy), ("comedy", comedy), ("thriller", thriller), ("action", action), ("drama", drama), ("animation", animation)]
            #z = [("adventure", True), ("horror", False), ("crime", True), ("romance", False), ("children", True), ("fantasy", False), ("comedy", True), ("thriller", True), ("action", False), ("drama", False), ("animation", True)]
            u = Genre(name=name, adventure=adventure, horror=horror, crime=crime, romance=romance, children=children, fantasy=fantasy, comedy=comedy, thriller=thriller, action=action, drama=drama, animation=animation)
            y = []
            for i in range(len(x)):
                if x[i][1] == True: 
                    y.append(x[i][0])
            print(y)
            u.save()
            print('save')
    else:
        form = GenreForm()
    return render(request, 'main/form.html' ,{
        'form':form
    })#JsonResponse("{'page': 'form'}", safe=False)
