from django.contrib import admin
from django.urls import path,include
from .import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('make',views.QuestionViewset)
router.register('answer',views.UserAnswerViewset)



urlpatterns = [
    path("",include(router.urls)),
]