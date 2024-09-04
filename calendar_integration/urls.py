from django.urls import path
from . import views

app_name = 'calendar_integration'

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_event, name='add_event'),
]
