from django.urls import path
from . import views

app_name = 'login'

urlpatterns = [
    path('', views.CebuLoginView.as_view(), name='login'),
    path('logout/', views.CebuLogoutView.as_view(), name='logout'),
]
