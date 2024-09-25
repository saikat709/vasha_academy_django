from django.http import HttpResponse
from django.shortcuts import render


def home(request, *args, **kwargs):
    exams = [1, 2, 3, 4]
    return render(request, "index.html", {"exams": exams})

def login(request):
    return render(request, "login.html")

def verification(request):
    return render(request, "verification.html")