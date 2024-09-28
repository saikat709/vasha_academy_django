from re import fullmatch

from django.shortcuts import render, redirect
from customer.models import Profile, Customer
from vashaacademy.utils import send_twilio_code
from .forms import LoginForm
from .serializers import ExamineeSerializer
from rest_framework import viewsets,status
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from .import serializers
from rest_framework.authtoken.models import Token
# from rest_framework.decorators import lo
from django.contrib.auth import authenticate, login, logout
from rest_framework.decorators import  api_view

# Create your views here
def login_view(request):
    form = LoginForm(request.POST or None)
    error = ""
    print("LOGIN######33")
    print(request.method)
    print(form.is_valid())
    print(form.errors)

    if request.method == "POST" and form.is_valid():
        fullname = form.cleaned_data['fullname']
        number = form.cleaned_data['number']
        password = form.cleaned_data['password']

        customer = Customer.objects.filter(number=number).first()

        if customer:
            customer_auth = password == customer.password
            print(customer_auth)
            if customer_auth:
                login(request, customer)
                return redirect("home")
            else:
                error = "Wrong Password"
        else:
            code = send_twilio_code()

            request.session.code = code
            request.session.number = number
            request.session.password = password
            request.session.fullname = fullname
            #return render(request, "login.html", {'form': form, 'error': error})

            return redirect('verification')
    # if form.has_error:
    #     error = form.errors[0]
    return render(request, "login.html", {'form':form, "error": error})



def verification(request):
    if request.method == "POST":
        code = request.POST['otp']
        if code == request.session.code:
            Customer.objects.create(
                fullname= request.session.fullname,
                number= request.session.number,
                password= request.session.number,
                is_verified=True,
            )
            login(request)
            return redirect("home")
    return render(request, "verification.html")

def logout_view(request):
    logout(request)
    return redirect("home")