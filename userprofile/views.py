from django.contrib.auth import authenticate, login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from userprofile.forms import CustomUserCreationForm, LoginForm


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Authenticate and login
            login(request, user)
            return redirect('userprofile:login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'userprofile/signup.html', {'form': form})


def custom_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('userprofile:dashboard')
    else:
        form = LoginForm()
    return render(request, 'userprofile/login.html', {'form': form})


@login_required
def dashboard(request):
    return render(request, 'dashboard.html')


@login_required
def logout(request):
    auth_logout(request)
    return redirect('userprofile:login')
