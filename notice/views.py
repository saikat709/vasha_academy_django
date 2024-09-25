from django.shortcuts import render

# Create your views here.
def notice(request, *args, **kwargs):
    type = request.GET.get('type', 'first')
    return render(request, 'notice.html')