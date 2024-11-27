from django.urls import path
from default_pages import views

urlpatterns = [
    path('', views.MainView.as_view(), name='main'),
    path('news-list/', views.NewsListView.as_view(), name='news-list'),
    path('news-detail/<int:pk>/', views.NewsDetailView.as_view(), name='news-detail'),
    path('add-news/', views.NewsCreateView.as_view(), name='add-news'),
] 