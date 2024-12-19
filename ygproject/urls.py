# ygproject/urls.py
from django.contrib import admin
from django.urls import path, include  # Include the yoga URLs

urlpatterns = [
    path('admin/', admin.site.urls),        
    path('', include('yoga.urls')),          
]
