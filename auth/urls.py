from django.urls import path

from auth.views import login, logout

urlpatterns = [
    path('/login', login),
    path('/logout', logout)
]