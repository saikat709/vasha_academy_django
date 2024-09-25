from django.shortcuts import render, redirect


# Create your views here.

def login(request, *args, **kwargs):
    if request.method == "POST":
        pass
    return render(request, "login.html")

def logout(request, *args, **kwargs):
    if request.method == "POST":
        # logout
        pass
    return redirect("home")
