from django.urls import path, include
from . import views
from rest_framework import routers
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path("api/login/", csrf_exempt(views.login_view)),
    path("api/signup/", csrf_exempt(views.register_view)),
    path("api/logout/", csrf_exempt(views.logout_view)),
]