from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, DetailView, ListView, CreateView
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin
)
from default_pages.forms import NewsForm
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
    
class NewsCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = News
    form_class = NewsForm
    template_name = 'default_pages/add_news.html'
    permission_required = 'default_pages.can_post_news'
    success_url = reverse_lazy('news-list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
# def add_news(request):
#     if request.method == 'POST':
#         form = NewsForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('news-list')
#     else:
#         form = NewsForm()
#     return render(request, 'default_pages/add_news.html', {'form': form})