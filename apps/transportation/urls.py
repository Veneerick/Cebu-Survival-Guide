from django.urls import path
from . import views

app_name = 'transportation'

urlpatterns = [
    path('', views.transportation, name='transportation'),
    path('<str:code>/', views.route_detail, name='route'),
]
