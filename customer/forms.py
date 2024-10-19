from django import forms
from customer.models import Customer


class LoginForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ["name", "username", "password"]


class UpdateForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ["name", "username", "picture"]

class PasswordResetForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)

