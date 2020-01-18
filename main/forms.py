from django import forms
from .models import *

class GenreForm(forms.ModelForm):
    name = forms.CharField(max_length=100, label='name')
    adventure = forms.BooleanField(default=False, label='adventure')
    children = forms.BooleanField(default=False, label='children')
    comedy = forms.BooleanField(default=False, label='comedy')
    thriller = forms.BooleanField(default=False, label='thriller')
    romance = forms.BooleanField(default=False, label='romance')
    action = forms.BooleanField(default=False, label='action')
    horror = forms.BooleanField(default=False, label='horror')
    animation = forms.BooleanField(default=False, label='animation')
    crime = forms.BooleanField(default=False, label='crime')
    drama = forms.BooleanField(default=False, label='drama')

    class Meta:
        model = Genre
        fields = '__all__'


