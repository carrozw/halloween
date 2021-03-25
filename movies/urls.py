
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_movies, name='view_movies')
]
