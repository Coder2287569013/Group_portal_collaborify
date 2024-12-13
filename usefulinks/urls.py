from django.urls import path
from . import views

urlpatterns = [
    path('useful-links/', views.useful_links, name='useful_links'),
]
