from django import forms
from .models import *

class GenreForm(forms.ModelForm):
    name = forms.CharField(max_length=100, label='name')
    adventure = forms.BooleanField(label='adventure', required=False)
    children = forms.BooleanField(label='children', required=False)
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


