from django.contrib import admin
from django.urls import path , include
from application import views  # Import the views module from your app directory
from django.contrib.auth import views as auth_views
from django.urls import re_path


urlpatterns = [

    path('', views.home, name='home'),
 
]