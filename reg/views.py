from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)
from .forms import UserLoginForm, UserRegisterForm


def login_view(request):
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = authenticate(email=email, password=password)
        login(request, user)
        if login:
            return JsonResponse("{'message' : 'login successful'}", safe=False, status=200)
        else:
            return JsonResponse("{'message' : 'invalid credentials'}", safe=False, status=400)
    return JsonResponse("{'message' : 'login'}", safe=False)


def register_view(request):
    next = request.GET.get('next')
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        return JsonResponse("{'message' : 'signup success'}", safe=False)
    return JsonResponse("{'message' : 'signup'}", safe=False)



def logout_view(request):
    logout(request)
    return JsonResponse({'message':'Logout'}, safe=False, status=200)

