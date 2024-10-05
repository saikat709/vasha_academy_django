from django.shortcuts import render

from notice.models import Notice


# Create your views here.
def notice(request, *args, **kwargs):
    country = request.GET.get('country', 'others')
    notices = Notice.objects.filter(country = country)
    print(notices)

    # notices = [1,1,1,1,1,1,1,1,1,1,1]
    return render(request, 'notice.html', {
        'country' : country,
        'notices' : notices,
    })


