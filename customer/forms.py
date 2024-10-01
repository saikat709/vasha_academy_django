from django import forms
from django.core.exceptions import ValidationError
from phonenumber_field.formfields import PhoneNumberField, SplitPhoneNumberField


class LoginForm(forms.Form):
    fullname = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)
    number = SplitPhoneNumberField()

class PasswordResetForm(forms.Form):
    number = SplitPhoneNumberField()
    password = forms.CharField(max_length=100)

