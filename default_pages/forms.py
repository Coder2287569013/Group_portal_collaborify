# Here will be the forms for News, Calendar, Events and so on...
from django import forms
from default_pages.models import News

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content', 'author', 'editor']