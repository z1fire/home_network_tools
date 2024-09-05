# food_inventory/views.py

from django.shortcuts import render

def home(request):
    return render(request, 'todo/home.html')  # Make sure the correct template is used
