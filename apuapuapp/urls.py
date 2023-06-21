"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from apuapuapp import views

urlpatterns = [
    # http://127.0.0.1:8000/apu-apu/
    path('', views.index_),
    # http://127.0.0.1:8000/apu-apu/my_list/
    path('my_list/', views.my_list),
    # http://127.0.0.1:8000/apu-apu/pill_detail/
    path('pill_detail/', views.pill_detail),
    # http://127.0.0.1:8000/apu-apu/seach_list/
    path('seach_list/', views.seach_list2),
    # http://127.0.0.1:8000/apu-apu/add_pill
    path('add_pill/', views.add_pill),
    # http://127.0.0.1:8000/apu-apu/pill_orc
    path('pill_orc/', views.pill_orc),
]
