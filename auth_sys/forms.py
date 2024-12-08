from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.exceptions import ValidationError
from .models import CustomUser
from datetime import date

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ["email", "first_name", "last_name", 'birth_month', 'birth_day']
    
    def clean(self):
        cleaned_data = super().clean()
        month = cleaned_data.get('birth_month')
        day = cleaned_data.get('birth_day')

        if month and day:
            try:
                date(2000, month, day)
            except ValueError:
                raise ValidationError(f"Invalid day {day} for the selected month {month}")
            
        return cleaned_data


class CustomUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm.Meta):
        model = CustomUser
        fields = ["email", "first_name", "last_name", 'birth_month', 'birth_day']
    
    def clean(self):
        cleaned_data = super().clean()
        month = cleaned_data.get('birth_month')
        day = cleaned_data.get('birth_day')

        if month and day:
            try:
                date(2000, month, day)
            except ValueError:
                raise ValidationError(f"Invalid day {day} for the selected month {month}")
            
        return cleaned_data
