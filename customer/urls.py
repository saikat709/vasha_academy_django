from django.urls import path
from rest_framework.routers import DefaultRouter
from . import api_view, views

app_name = 'customer'

customer_api = DefaultRouter()
customer_api.register('profile', api_view.ExamViewset)

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('verification/', views.verification, name='verification'),
]