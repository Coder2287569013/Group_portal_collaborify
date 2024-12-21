from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, DetailView, ListView, CreateView
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin
)
from default_pages.forms import NewsForm
from default_pages.models import News
from datetime import datetime, timedelta
from .models import CustomUser
from .models import Event
from .forms import EventForm
from datetime import datetime, timedelta

def generate_timeline_with_events(start_date, end_date):
    timeline = []
    current_date = start_date
    events = Event.objects.filter(date__range=[start_date, end_date])

    while current_date <= end_date:
        daily_events = events.filter(date=current_date)
        timeline.append({
            "day": current_date.strftime("%d"),
            "month": current_date.strftime("%b"),
            "weekday": current_date.strftime("%a"),
            "events": daily_events,
        })
        current_date += timedelta(days=1)

    return timeline

# Create your views here.
class MainView(TemplateView):
    template_name = 'default_pages/main.html'

    def get_context_data(self, **kwargs):
        today = datetime.now().date()
        thirty_days = today + timedelta(days=30)
        print(thirty_days)
        upcoming_birthdays = []
        for user in CustomUser.objects.all():
            if user.birth_month is not None and user.birth_day is not None:
                try:
                    birthday = datetime(today.year, user.birth_month, user.birth_day).date()
                except ValueError:
                    continue

                if today > birthday:
                    birthday = datetime(today.year + 1, user.birth_month, user.birth_day).date()

                if today <= birthday <= thirty_days:
                    print(thirty_days - birthday)
                    upcoming_birthdays.append(user)
        

        news = News.objects.all().order_by('-created_at')[0:3]

        start_date = datetime.now() - timedelta(days=30)
        end_date = datetime.now() + timedelta(days=30)

        Event.objects.filter(date__lt=start_date-timedelta(days=1)).delete()

        timeline = generate_timeline_with_events(start_date, end_date)

        context = super().get_context_data(**kwargs)
        context['upcoming_birthdays'] = upcoming_birthdays
        context['news'] = news
        context['timeline'] = timeline
        print(upcoming_birthdays)

        return context

class NewsListView(ListView):
    model = News
    template_name = 'default_pages/news_list.html'
    context_object_name = 'news'

    def get_queryset(self):
        return News.objects.order_by('-created_at')

class NewsDetailView(DetailView):
    model = News
    template_name = 'default_pages/news_detail.html'
    context_object_name = 'news_item'

    def get_queryset(self):
        return News.objects
    
class NewsCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = News
    form_class = NewsForm
    template_name = 'default_pages/add_news.html'
    permission_required = 'default_pages.can_post_news'
    success_url = reverse_lazy('news-list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class AboutView(TemplateView):
    template_name = "default_pages/about_page.html"
    
# def add_news(request):
#     if request.method == 'POST':
#         form = NewsForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('news-list')
#     else:
#         form = NewsForm()
#     return render(request, 'default_pages/add_news.html', {'form': form})

def useful_links(request):
    return render(request, 'default_pages/useful_links.html',)

def add_event(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        date = request.POST.get("date")

        if not title or not date:
            return render(
                request,
                "default_pages/add_event.html",
                {"error": "Title and date are required fields."}
            )

        event = Event.objects.create(
            title=title,
            description=description,
            date=date,
        )

    return render(request, "default_pages/add_event.html")