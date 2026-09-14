from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy


class StyledAuthenticationForm(AuthenticationForm):
    """AuthenticationForm with the shared 'form-input' CSS class applied."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'form-input',
                'placeholder': field.label,
            })


class CebuLoginView(LoginView):
    """
    Login Screen (vertical slice: login).
    Built on Django's built-in LoginView.
    """
    template_name = 'login/login.html'
    authentication_form = StyledAuthenticationForm
    redirect_authenticated_user = True


class CebuLogoutView(LogoutView):
    """Logs the user out and sends them back to the Home Screen."""
    next_page = reverse_lazy('home:home')
