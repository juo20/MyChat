from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from account.forms import RegistrationForm, AuthForm
from django.contrib import messages

def registration_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return redirect('/MyChat/chat/')
        else:
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'account/register.html', context)

def logout_request(request):
    logout(request)
    messages.info(request, "logged out successfully")
    return redirect("/login")

def login_request(request):
    """
    context = {}
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if not form.is_valid():
            messages.error(request, "invalid")
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, account)
            message.info(request, "logged in")
            return redirect('/MyChat/chat/')
        else:
            messages.error(request, "Error")
    else:
        messages.error(request, "fucked")
        form = AuthenticationForm(request, data=request.POST)
        context['form'] = form
    return render(request, 'account/login.html', context)
    """
    context = {}
    #user = request.user
    #if user.is_authenticated:return redirect('/MyChat/chat/')
    if request.POST:
        form = AuthForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                return redirect('/MyChat/chat/')
    else:
        form = AuthForm()
    context['form'] = form
    return render(request, 'account/login.html', context)

