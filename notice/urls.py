from django.urls import path
from rest_framework.routers import DefaultRouter

from notice.view_api import NoticeViewSets, FaqViewSets, PdfViewSets
from notice.views import notice
app_name = 'notice'


notice_api = DefaultRouter()
notice_api.register('', NoticeViewSets)
notice_api.register('faq/', FaqViewSets)
notice_api.register('pdf/', PdfViewSets)


urlpatterns = [
    path('', notice, name='notice'),
]