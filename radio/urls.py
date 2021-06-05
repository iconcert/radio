"""radio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from flash import views

urlpatterns = [
    path('', views.index),
    path('home/', views.index),
    path('information/', views.information),
    path('menu/', views.menu),
    path('registration/', views.registration),
    path('autorization/', views.autorization),
    path('police/', views.police),
    path('regulations/', views.regulations),
    path('services/', views.services),
    path('sitemap/', views.sitemap),
    path('admin/', admin.site.urls),
]