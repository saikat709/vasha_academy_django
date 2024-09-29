from django.shortcuts import render, redirect

def home(request, *args, **kwargs):
    exams = [1, 2, 3, 4]
    lang = request.GET.get('lang', 'bn')
    lang = lang if lang in ('bn', 'en') else 'bn'
    request.session['lang'] = lang
    return render(request, "index.html", {"exams": exams})


def course(request, id):
    return render(request, "course_details.html", {"exams": [1,1,1,11,1,1,1,1,1,1,1,2,2,2]})

def notice(request):
    return render(request, "notice.html")