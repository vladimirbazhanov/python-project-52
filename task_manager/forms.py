from django.contrib.auth.forms import AuthenticationForm
from django import forms


class UserAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={"autofocus": True, "class": 'form-control'}
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": 'form-control'}
        )
    )
