from django import forms
from .models import Grade, News

class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ['grade']


class GradeFilterForm(forms.Form):
    TYPE_GRADE=[
        ("H","H"),
        ("H/O","H/O")
    ]

    for a in range(12):
        TYPE_GRADE.append((f"{a+1}",f"{a+1}"))

    student_grade = forms.ChoiceField(choices=TYPE_GRADE,required=False , label = "student_grade")

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content', 'author', 'editor', 'is_published']