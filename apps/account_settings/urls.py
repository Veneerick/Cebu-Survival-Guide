from django.urls import path
from . import views

app_name = 'account_settings'

urlpatterns = [
    path('', views.settings, name='settings'),
]