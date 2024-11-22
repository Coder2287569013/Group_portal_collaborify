from django.shortcuts import render, redirect
from django.views.generic import TemplateView, DetailView, ListView
from default_pages.forms import NewsForm
from django.http import HttpResponse
from default_pages.models import News

# Create your views here.
class MainView(TemplateView):
    template_name = 'default_pages/main.html'

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

def add_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news-list')
    else:
        form = NewsForm()
    return render(request, 'default_pages/add_news.html', {'form': form})