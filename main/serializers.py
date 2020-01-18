from rest_framework import serializers
from .models import *
from rest_framework import exceptions


class GenreSerailizers(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


