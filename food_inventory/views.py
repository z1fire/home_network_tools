# food_inventory/views.py

from django.shortcuts import render

def home(request):
    return render(request, 'food_inventory/home.html')  # Make sure the correct template is used
