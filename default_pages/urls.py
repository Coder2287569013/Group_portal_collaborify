from django.urls import path
from default_pages import views

urlpatterns = [
    path('', views.MainView.as_view(), name='main'),
    path('news-list/', views.NewsListView.as_view(), name='news-list'),
    path('news-detail/<int:pk>/', views.NewsDetailView.as_view(), name='news-detail'),
    path('add-news/', views.NewsCreateView.as_view(), name='add-news'),
    path('useful-links/', views.useful_links, name='useful-links'),
    path('add_event/', views.add_event, name='add-event'),
    path('about/', views.AboutView.as_view(), name='about'),
] 