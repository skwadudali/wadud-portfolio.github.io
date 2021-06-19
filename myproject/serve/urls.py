from django.contrib import admin
from django.urls import path,include
from serve import views


urlpatterns = [
    path('', views.services, name='services'),
]