from django.shortcuts import render

from notice.models import Notice


# Create your views here.
def notice(request, *args, **kwargs):
    country = request.GET.get('country')
    country = country if country in ('other', 'bd') else "other"
    notices = Notice.objects.filter(country = country)

    # notices = [1,1,1,1,1,1,1,1,1,1,1]
    return render(request, 'notice.html', {
        'country' : country,
        'notices' : notices,
    })

def terms(request, *args, **kwargs):
    return render(request, "terms.html")


