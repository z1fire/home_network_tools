from django import forms
from .models import CalendarEvent

class CalendarEventForm(forms.ModelForm):
    class Meta:
        model = CalendarEvent
        fields = ['title', 'description', 'start_time', 'end_time', 'location', 'repeat', 'repeat_until', 'custom_repeat_interval', 'custom_repeat_unit']
        widgets = {
            'start_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'repeat_until': forms.DateInput(attrs={'type': 'date'}),
        }
