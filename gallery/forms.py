from django import forms
from .models import Photo


class PhotoForms(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['image']
        widgets = {
            "image":forms.FileInput()
        }
