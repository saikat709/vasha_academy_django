from django.shortcuts import render, redirect
from course.models import Course
from notice.models import FAQ
from notice.models import WebsiteConfig

def home(request, *args, **kwargs):
    lang = request.GET.get('lang', 'bn')
    lang = lang if lang in ('bn', 'en') else 'bn'
    request.session['lang'] = lang

    all_courses = Course.objects.all()
    faqs = FAQ.objects.all()
    config = WebsiteConfig.objects.all().first()

    courses = []
    for course in all_courses:
        single_course = {}
        for en in course.enrollments.all():
            if en.customer.id == request.user.id and en.has_validity:
                single_course['enrolled'] = True
        single_course['course'] = course
        if course.discount >0:
            single_course["discounted_price"] = int(course.price*(1-course.discount/100))
        courses.append(single_course)
    # print(request.user in courses.first().customers.all())

    # print(courses)
    return render(
        request,
        "index.html",
        {
                'courses': courses,
                'faqs': faqs ,
                'config': config
                }
        )