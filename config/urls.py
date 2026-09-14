"""
URL configuration for cebu_survival_guide project.

Each screen is a self-contained vertical slice (its own Django app), so the
root urlconf just mounts each app's urls.py at its own path.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.home.urls')),                  # Home Screen slice
    path('login/', include('apps.login.urls')),            # Login slice
    path('register/', include('apps.register.urls')),      # Register slice
    path('profile/', include('apps.user_profile.urls')),   # Profile slice
    path('settings/', include('apps.account_settings.urls')),       # Settings slice
]