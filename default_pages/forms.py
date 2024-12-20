# Here will be the forms for News, Calendar, Events and so on...
from django import forms
from default_pages.models import News, Event

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content', 'editor']


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'date']