from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from django.conf import settings

from course.urls import course_api, exam_api, result_api
from customer.urls import customer_api
from .views import home, course, notice

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('customer/', include('customer.urls')),

    path('course/<int:id>', course),
    path('notice/', notice),

    # api routes
    path('api/question/',include('question.urls')),
    path('api/customer/',include(customer_api.urls)),
    path('api/course/',include(course_api.urls)),
    path('api/exam/',include(exam_api.urls)),
    path('api/result/',include(result_api.urls)),
]

# if settings.DEBUG:
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
