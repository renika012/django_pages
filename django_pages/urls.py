# django_pages/urls.py
from django.contrib import admin
from django.urls import path, include # new

urlpatterns = [
    path('admin/', http://admin.site.urls),
    path('pages/', include('pages.urls')), # new
]
