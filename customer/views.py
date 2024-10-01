from dbm import error

from django.shortcuts import render, redirect
from vashaacademy.utils import send_twilio_code
from .forms import LoginForm, PasswordResetForm
from django.contrib.auth import login, logout

from .models import Customer, LoginInfo

def first_form_error(form):
    for field, errors in form.errors.items():
        if errors:
            return error[0]


# Create your views here
def login_view(request):
    form = LoginForm(request.POST or None)
    error = ""
    print("#########1")
    if request.method == "POST" and form.is_valid():
        number = form.cleaned_data['number']
        password = form.cleaned_data['password']
        fullname = form.cleaned_data['fullname']

        print("#########2")
        customer = Customer.objects.filter(number=number).first()
        if customer:
            customer_auth = customer.password == password
            if customer_auth:
                if customer.is_verified:
                    info = LoginInfo(user=customer, using_app=False)
                    info.save()
                    login(request, customer)
                    return redirect("home")
                else:
                    code = send_twilio_code()
                    request.session['code'] = code
                    return redirect('customer:verification', id = customer.id)
            else:
                error = "Wrong Password"
        else:
            code = send_twilio_code()
            request.session['code'] = code
            user = Customer.objects.create_user(
                number = number,
                fullname = fullname,
                password=password
            )
            return redirect('customer:verification', id=user.id)
    elif form.errors != {}:
        error = first_form_error(form)
    return render(request, "login.html", {'form':form, "error": error})


def verification(request, id):
    error = None
    session_code = request.session.get('code')
    if session_code is None:
        redirect('home')

    if request.method == "POST":
        code = request.POST['code']
        if session_code == code:
            customer = Customer.objects.filter(id=id).first()
            if customer:
                password = request.session.get('password')
                if password:
                    customer.password = request.session.get('password')
                    request.session['password'] = None
                else:
                    customer.is_verified = True
                customer.save()
                login(request, customer)
                request.session['code'] = None
                return redirect("home")
            else:
                error = "User not found."
        error = "Provided code does not match"
    return render(request, "verification.html", {'error': error})


def reset_password(request):
    form = PasswordResetForm(request.POST or None)
    error = None
    if form.is_valid():
        customer = Customer.objects.filter(number = form.cleaned_data['number'] ).first()
        if customer is not None:
            request.session['code'] = send_twilio_code()
            request.session['password']  = form.cleaned_data['password']
            return redirect('customer:verification', id=customer.id)
        else:
            error = "No user found with that number"
    elif form.errors != {}:
        error = first_form_error(form)
    return render(request, 'reset.html', {'form': form, 'error':error, 'hi':"Saikat"})


def logout_view(request):
    logout(request)
    return redirect("home")
