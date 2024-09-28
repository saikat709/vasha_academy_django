from django.core.exceptions import ValidationError
from django import forms

from customer.models import Customer


class LoginForm(forms.ModelForm):
    # confirm_password = forms.CharField(max_length=100)
    number = forms.CharField(max_length=15)
    class Meta:
        model = Customer
        fields = ['fullname', 'number', 'password']
        exclude = ['is_verified', ]