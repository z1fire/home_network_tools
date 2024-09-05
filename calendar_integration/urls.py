from django.urls import path
from . import views

app_name = 'calendar_integration'

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_event, name='add_event'),
    path('edit/<int:event_id>/', views.edit_event, name='edit_event'),
    path('delete/<int:event_id>/', views.delete_event, name='delete_event'),
    path('calendar/', views.calendar_view, name='calendar_view'),  # New URL for the calendar view
]
