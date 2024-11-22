from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse

# Create your views here.
class MainView(TemplateView):
    template_name = 'default_pages/main.html'