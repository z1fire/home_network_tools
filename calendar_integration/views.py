import calendar  # Import the Python calendar module
from django.shortcuts import render, get_object_or_404, redirect
from .models import CalendarEvent
from .forms import CalendarEventForm
from datetime import datetime, timedelta



def calendar_view(request):
    # Get the current date
    today = datetime.today()
    month = request.GET.get('month', today.month)
    year = request.GET.get('year', today.year)

    # Convert month and year to integers
    month = int(month)
    year = int(year)

    # Generate the month calendar
    cal = calendar.Calendar()
    month_days = cal.monthdayscalendar(year, month)
    month_name = calendar.month_name[month]

    # Get all events for the selected month
    events = CalendarEvent.objects.filter(
        start_time__year=year,
        start_time__month=month
    )

    # Prepare a dictionary to hold events by day
    events_by_day = {}
    for event in events:
        day = event.start_time.day
        if day not in events_by_day:
            events_by_day[day] = []
        events_by_day[day].append(event)

    context = {
        'month_days': month_days,
        'month_name': month_name,
        'year': year,
        'events_by_day': events_by_day,
    }

    return render(request, 'calendar_integration/calendar.html', context)
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

def edit_event(request, event_id):
    event = get_object_or_404(CalendarEvent, id=event_id)
    if request.method == 'POST':
        form = CalendarEventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('calendar_integration:home')
    else:
        form = CalendarEventForm(instance=event)
    return render(request, 'calendar_integration/edit_event.html', {'form': form, 'event': event})

def delete_event(request, event_id):
    event = get_object_or_404(CalendarEvent, id=event_id)
    if request.method == 'POST':
        event.delete()
        return redirect('calendar_integration:home')
    return render(request, 'calendar_integration/delete_event.html', {'event': event})
