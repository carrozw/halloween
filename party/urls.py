
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_party, name='view_party')
]
