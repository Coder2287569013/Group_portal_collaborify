from django.shortcuts import render, redirect
from .models import Event
from .forms import EventForm
import calendar
from datetime import datetime, timedelta

# Create your views here.
def generate_timeline_with_events(start_date, end_date):
    timeline = []
    current_date = start_date
    events = Event.objects.filter(date__range=[start_date, end_date])  # Отримуємо події в діапазоні дат

    while current_date <= end_date:
        # Події для поточного дня
        daily_events = events.filter(date=current_date)
        timeline.append({
            "day": current_date.strftime("%d"),  # День місяця
            "month": current_date.strftime("%b"),  # Місяць
            "weekday": current_date.strftime("%a"),  # День тижня
            "events": daily_events,  # Події
        })
        current_date += timedelta(days=1)

    return timeline

# def generate_timeline_with_events(start_date, end_date):
#     timeline = []
#     current_date = start_date
#     events = Event.objects.filter(date__range=[start_date, end_date])

#     while current_date <= end_date:
#         daily_events = events.filter(date=current_date)
#         timeline.append({
#             "day": current_date.strftime("%d"),
#             "month": current_date.strftime("%b"),
#             "weekday": current_date.strftime("%a"),
#             "events": daily_events,
#         })
#         current_date += timedelta(days=1)

#     return timeline

# def timeline_calendar(request):
#     today = datetime.today()
#     start_date = today - timedelta(days=7)
#     end_date = today + timedelta(days=7)

#     timeline = generate_timeline_with_events(start_date, end_date)
def timeline_calendar(request):
    Event.objects.filter(date__lt= datetime.now() ).delete()

    start_date = datetime.now() - timedelta(days=30)
    end_date = datetime.now() + timedelta(days=30)

    timeline = generate_timeline_with_events(start_date, end_date)

    return render(request, "default_pages/main.html", {"timeline": timeline})

def add_event(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('timeline-calendar')
    else:
        form = EventForm()

    return render(request, "default_pages/add_event.html", {"form": form})