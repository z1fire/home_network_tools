from django.shortcuts import render, redirect
from .models import CalendarEvent
from .forms import CalendarEventForm

def home(request):
    events = CalendarEvent.objects.all()
    return render(request, 'calendar_integration/home.html', {'events': events})

def add_event(request):
    if request.method == 'POST':
        form = CalendarEventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('calendar_integration:home')
    else:
        form = CalendarEventForm()
    return render(request, 'calendar_integration/add_event.html', {'form': form})
