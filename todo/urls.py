# todo/urls.py

from django.urls import path
from . import views

app_name = 'todo'  # Register the namespace for the 'todo' app

urlpatterns = [
    path('', views.home, name='home'),
    # Add other URL patterns for the todo app here
]
