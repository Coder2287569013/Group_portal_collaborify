from django.urls import path
from grade_system import views
from .views import NewsListView, NewsDetailView, add_news

urlpatterns = [
    path('student-list/', views.StudentListView.as_view(), name='student-list'),
    path('student-detail/<int:pk>', views.StudentDetailView.as_view(), name='student-detail'),
    path('news-list/', NewsListView.as_view(), name='news-list'),
    path('news-detail/<int:pk>/', NewsDetailView.as_view(), name='news-detail'),
    path('add-news/', add_news, name='add-news'),
]
