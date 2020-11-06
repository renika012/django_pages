# django_pages/urls.py
from django.contrib import admin
from django.urls import path, include # new

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pages/', include('pages.urls')), # new
]
