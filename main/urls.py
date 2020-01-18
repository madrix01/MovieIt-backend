from django.urls import path, include
from . import views
from rest_framework import routers
from django.views.decorators.csrf import csrf_exempt

router = routers.DefaultRouter()
router.register('genre', views.GenreView)

urlpatterns = [
    path('', include(router.urls)),
    path('api/search/', csrf_exempt(views.user_form)),
]
