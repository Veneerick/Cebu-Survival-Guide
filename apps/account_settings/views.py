from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import SettingsForm


@login_required
def settings(request):
    """
    Settings Screen (vertical slice: account_settings).
    Lets the logged-in user update their account settings.
    """
    if request.method == 'POST':
        form = SettingsForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your settings have been updated.')
            return redirect('account_settings:settings')
    else:
        form = SettingsForm(instance=request.user)

    return render(request, 'account_settings/settings.html', {'form': form})