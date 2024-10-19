from django.shortcuts import render, redirect
from course.models import Course
from notice.models import FAQ
from notice.models import WebsiteConfig


def home(request, *args, **kwargs):
    lang = request.GET.get('lang', 'bn')
    lang = lang if lang in ('bn', 'en') else 'bn'
    request.session['lang'] = lang

    courses = Course.objects.all()

    faqs = FAQ.objects.all()

    config = WebsiteConfig.objects.all().first()

    # print(request.user in courses.first().customers.all())

    return render(
        request,
        "index.html",
        { "exams": [11,1,1,1,1,1,1],
                'courses': courses,
                'faqs': faqs ,
                'config': config
                }
        )


