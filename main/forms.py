from django import forms
from .models import *
from django.contrib.auth import authenticate, get_user_model


class GenreForm(forms.ModelForm):
    name = forms.CharField(max_length=100, label='name')
    email = forms.EmailField()
    adventure = forms.BooleanField(label='adventure', required=False)
    family = forms.BooleanField(label='family', required=False)
    comedy = forms.BooleanField(label='comedy', required=False)
    thriller = forms.BooleanField(label='thriller', required=False)
    romance = forms.BooleanField(label='romance', required=False)
    action = forms.BooleanField(label='action', required=False)
    horror = forms.BooleanField(label='horror', required=False)
    animation = forms.BooleanField(label='animation', required=False)
    crime = forms.BooleanField(label='crime', required=False)
    drama = forms.BooleanField(label='drama', required=False)

    class Meta:
        model = Genre
        fields = '__all__'


class SearchForm(forms.ModelForm):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    search = forms.CharField(max_length=100)

    class Meta:
        model = Search
        fields = '__all__'

