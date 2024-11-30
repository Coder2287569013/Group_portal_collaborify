from .models import Post , Comment
from django import forms


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description', 'type', 'media']
        widgets = {
            "media":forms.FileInput()
        }


class PostFilterForm(forms.Form):
    
    TYPE = [
        ('news', 'News'),
        ('update', 'Update'),
        ('event', "Event"),
        ('question','Question')
    ]
        
    type = forms.ChoiceField(choices=TYPE, required=False , label = "type")


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content','media']
        widgets = {
            "media":forms.FileInput()
        }