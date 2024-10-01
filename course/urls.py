from django.contrib import admin
from django.urls import path,include
from .import views

from rest_framework.routers import DefaultRouter

from .view_api import CourseViewSets, ExamViewSets, ResultViewSets

course_api = DefaultRouter()
course_api.register('', CourseViewSets)
course_api.register('trialattend', views.AttendenceViewset)

exam_api = DefaultRouter()
exam_api.register('', ExamViewSets)

result_api = DefaultRouter()
result_api.register('', ResultViewSets)

urlpatterns = [
    path("", include(course_api.urls)),
]