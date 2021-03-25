
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_stories, name='view_stories')
]
