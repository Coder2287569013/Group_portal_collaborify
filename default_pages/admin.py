from django.contrib import admin
from default_pages.models import News, Event

# Register your models here.
admin.site.register(News)
admin.site.register(Event)