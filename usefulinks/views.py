from django.shortcuts import render
from .models import UsefulLink

def useful_links(request):
    links = UsefulLink.objects.all()
    return render(request, 'usefulinks/useful_links.html', {"links": links})

