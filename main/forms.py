from django import forms
from .models import *
from django.contrib.auth import authenticate, get_user_model

User = get_user_model()

class GenreForm(forms.ModelForm):
    name = forms.CharField(max_length=100, label='name', required=False)
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
    search = forms.CharField(max_length=100)
    class Meta:
        model = Search
        fields = '__all__'


class UserLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(email=email, password=password)
            if not user:
                raise forms.ValidationError('This user does not exist')
            if not user.check_password(password):
                raise forms.ValidationError('Incorrect password')
            if not user.is_active:
                raise forms.ValidationError('This user is not active')
        return super(UserLoginForm, self).clean(*args, **kwargs)


class UserRegisterForm(forms.ModelForm):
    email = forms.EmailField(label='Email address')
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password'
        ]

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError(
                "This email has already been registered")
        return super(UserRegisterForm, self).clean(*args, **kwargs)

