from django.core.exceptions import ValidationError
from django import forms

from customer.models import Customer


class LoginForm(forms.Form):
    fullname = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)
    number = forms.CharField(max_length=15, validators=[])

class PasswordResetForm(forms.Form):
    number = forms.CharField(max_length=15, validators=[])
    password = forms.CharField(max_length=100)
