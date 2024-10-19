from tkinter.font import names

from django.urls import path
from rest_framework.routers import DefaultRouter

from notice.view_api import NoticeViewSets, FaqViewSets, PdfViewSets
from notice.views import notice, terms

app_name = 'notice'


notice_api = DefaultRouter()
notice_api.register('notice', NoticeViewSets)
notice_api.register('faq', FaqViewSets)
notice_api.register('pdf', PdfViewSets)


urlpatterns = [
    path('', notice, name='notice'),
    path('terms/', terms, name='terms')
]