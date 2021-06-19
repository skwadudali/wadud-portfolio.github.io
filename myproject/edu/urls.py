
from django.urls import path,include
from edu import views


urlpatterns = [
    path('', views.skill, name='skill'),
]