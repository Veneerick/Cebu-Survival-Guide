from django.shortcuts import render


def home(request):
    """
    Home Screen (vertical slice: home).
    First screen visitors land on. Shows Login/Register in the top bar
    when logged out, or a greeting + Logout when logged in.
    """
    return render(request, 'home/home.html')
