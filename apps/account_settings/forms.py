from django import forms
from django.contrib.auth.models import User


class SettingsForm(forms.ModelForm):
    """
    Settings form (vertical slice: settings).
    Lets the logged-in user update their basic account details.
    """

    class Meta:
        model = User
        fields = ['username', 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'form-input',
                'placeholder': field.label,
            })