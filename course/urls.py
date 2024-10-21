from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .view_api import CourseViewSets, ExamViewSets, ResultViewSets
from .views import course, exam, result, payment_success, payment_failed, initiate_payment

course_api = DefaultRouter()
course_api.register('', CourseViewSets)
#course_api.register('trialattend', views.AttendenceViewset)

exam_api = DefaultRouter()
exam_api.register('', ExamViewSets)

result_api = DefaultRouter()
result_api.register('', ResultViewSets)

app_name = 'course'
urlpatterns = [
    path("<int:id>/", course, name='course'),
    path("result/<int:id>", result, name='result'),
    path("exam/<int:id>/", exam, name='exam'),
    path("initiate-payment/<int:course_id>", initiate_payment, name='initiate_payment'),
    path("payment-successful/<int:user_id>/<int:course_id>", payment_success, name='payment_successful'),
    path("payment-failed", payment_failed, name='payment_failed'),
]