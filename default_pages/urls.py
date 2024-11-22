from django.urls import path
from default_pages import views

urlpatterns = [
    path('', views.MainView.as_view(), name='main')
] 