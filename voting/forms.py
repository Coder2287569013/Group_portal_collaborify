from django import forms
from django.forms import inlineformset_factory
from .models import Voting, Choice

class VotingForm(forms.ModelForm):
    class Meta:
        model = Voting
        fields = ['title', 'description']

ChoiceFormSet = inlineformset_factory(
    Voting, 
    Choice,
    fields=['text'],
    extra=4,
    min_num=4,
    validate_min=True
) 