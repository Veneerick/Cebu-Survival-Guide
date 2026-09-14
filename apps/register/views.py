from django.contrib.auth import login as auth_login
from django.contrib import messages
from django.shortcuts import render, redirect

from .forms import RegisterForm


def register(request):
    """
    Register Screen (vertical slice: register).
    On success, logs the new user in and sends them to the Home Screen.
    """
    if request.user.is_authenticated:
        return redirect('home:home')

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            messages.success(request, 'Welcome to the Cebu Survival Guide!')
            return redirect('home:home')
    else:
        form = RegisterForm()

    return render(request, 'register/register.html', {'form': form})
