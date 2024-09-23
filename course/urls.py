from django.contrib import admin
from django.urls import path,include
from .import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('adminplan',views.CourseViewSets)
router.register('trialattend',views.AttendenceViewset)



urlpatterns = [
    path("",include(router.urls)),
]