from django.shortcuts import render, redirect
from vashaacademy.utils import send_otp_code
from .forms import LoginForm, PasswordResetForm, UpdateForm
from django.contrib.auth import login, logout, authenticate

from .models import Customer, LoginInfo

def first_form_error(form):
    for field, errors in form.errors.items():
        if errors:
            return errors[0]

# Create your views here
def login_view(request):
    form = LoginForm()
    error = ""
    is_email = request.GET.get('is_email')
    is_email = is_email.upper() == "TRUE" if is_email is not None else False
    print(is_email)
    if request.method == "POST":
        form = LoginForm(request.POST)
        print(form.changed_data)
        username = request.POST.get('username')
        username = "+880" + username if not is_email else username
        password = request.POST.get('password')
        name = request.POST.get('name')

        if form.errors != {}:
            # error = first_form_error(form)
            error = str(form.errors)

        customer = Customer.objects.filter(username=username).first()
        if customer:
            customer_auth = authenticate(username=username, password=password) # customer.password == password
            if customer_auth:
                print("Found user....")
                if customer.is_verified:
                    info = LoginInfo(user=customer, using_app=False)
                    info.save()
                    login(request, customer)
                    return redirect("home")
                else:
                    print("sending code.")
                    print(is_email)
                    code = send_otp_code(username, is_email)
                    request.session['code'] = code
                    return redirect('customer:verification', id = customer.id)
            else:
                error = "Wrong Password"
        else:
            print("Did not found user....")
            print("sending code.")
            code = send_otp_code(sent_to=username, is_email=is_email)
            print("sending code done.")
            request.session['code'] = code
            user = Customer.objects.create_user(
                username=username,
                name = name,
                password=password,
                is_email = is_email
            )
            user.save()
            return redirect('customer:verification', id=user.id)
    return render(request, "login.html", {'form':form, "error": error, 'is_email': is_email})


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
    is_email = request.GET.get('is_email')
    is_email = is_email.upper() == "TRUE" if is_email is not None else False
    error = None
    if form.is_valid():
        username = form.cleaned_data['username']
        customer = Customer.objects.filter(username = username ).first()
        if customer is not None:
            request.session['code'] = send_otp_code(sent_to=username, is_email=customer.is_email)
            request.session['password']  = form.cleaned_data['password']
            return redirect('customer:verification', id=customer.id)
        else:
            error = "No user found with that number"
    elif form.errors != {}:
        error = str(form.errors)
    return render(request, 'reset.html', {'form': form, 'error':error, 'is_email':is_email})


def update(request):
    if request.method == "POST":
        form = UpdateForm(request.POST or None, request.FILES, instance=request.user)
        print(form.errors)
        if form.is_valid(): form.save()
        pass
    return redirect("home")

def logout_view(request):
    logout(request)
    return redirect("home")
