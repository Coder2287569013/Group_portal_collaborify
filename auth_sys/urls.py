from django.urls import path
from auth_sys import views

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
]
