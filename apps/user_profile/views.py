from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def profile(request):
    """
    Profile Screen (vertical slice: user_profile).
    Displays the logged-in user's account details.
    """
    return render(request, 'user_profile/profile.html', {'user': request.user})