from django.shortcuts import render, redirect
from course.models import Course
from notice.models import FAQ

def home(request, *args, **kwargs):
    lang = request.GET.get('lang', 'bn')
    lang = lang if lang in ('bn', 'en') else 'bn'
    request.session['lang'] = lang

    courses = Course.objects.all()
    # print(courses.first().customers)

    faqs = FAQ.objects.all()

    print(request.user in courses.first().customers.all())

    return render(request, "index.html",
                  { "exams": [11,1,1,1,1,1,1], 'courses': courses, 'faqs': faqs })

