from django.urls import path
from rest_framework.routers import DefaultRouter
from . import view_api, views

app_name = 'customer'

customer_api = DefaultRouter()
customer_api.register('', view_api.CustomerViewset)

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('update/', views.update, name='update'),
    path('logout/', views.logout_view, name='logout'),
    path('reset/', views.reset_password, name='reset'),
    path('verification/<int:id>', views.verification, name='verification'),
]