from django import forms
from .models import CalendarEvent
from bootstrap_datepicker_plus.widgets import DateTimePickerInput, DatePickerInput

class CalendarEventForm(forms.ModelForm):
    class Meta:
        model = CalendarEvent
        fields = ['title', 'description', 'start_time', 'end_time', 'location', 'repeat', 'repeat_until', 'custom_repeat_interval', 'custom_repeat_unit']
        widgets = {
            'start_time': DateTimePickerInput(),  # Use DateTimePickerInput for start time
            'end_time': DateTimePickerInput(),    # Use DateTimePickerInput for end time
            'repeat_until': DatePickerInput(),    # Use DatePickerInput for repeat until
        }
