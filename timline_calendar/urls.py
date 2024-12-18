from django.urls import path
from timline_calendar import views

urlpatterns = [
    path('', views.timeline_calendar, name='timeline-calendar'),
    path('add_event/', views.add_event, name='add-event'),
]