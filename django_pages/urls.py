# django_pages/urls.py
from django.conf.urls import include
from django.contrib import admin
from django.urls import path # new

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pages/', include('pages.urls')), # new
]
