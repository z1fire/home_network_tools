# food_inventory/urls.py

from django.urls import path
from . import views

app_name = 'food_inventory'  # Register the namespace for the 'food_inventory' app

urlpatterns = [
    path('', views.home, name='home'),  # Define a home view for the app
    # Add other URL patterns for the food_inventory app here
]
