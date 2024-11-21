from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, ListView, DetailView
from auth_sys.models import CustomUser
from django.urls import reverse_lazy
from .models import Grade, Student, Teacher, News, User
from .forms import GradeForm, NewsForm


class StudentListView(ListView):
    model = CustomUser
    context_object_name = 'students'

    def get_queryset(self):
        return CustomUser.objects.filter(role='student')


class StudentDetailView(DetailView):
    model = CustomUser
    context_object_name = 'student'
    template_name = 'grade_system/student_detail.html'  

    def get_queryset(self):
        return CustomUser.objects.filter(role='student')

    def post(self, request, *args, **kwargs):
        student = self.get_object()
        grade_form = GradeForm(request.POST)

        if grade_form.is_valid():
            grade = grade_form.save(commit=False)
            grade.teacher = Teacher.objects.get(user = request.user)  # Прив'язуємо вчителя
            grade.student = Student.objects.get(user = student)  # Прив'язуємо студента
            grade.save()
            return redirect('student-detail', pk=student.pk)

        return render(request, self.template_name, {
            'student': student,
            'grade_form': grade_form,
        })

class NewsListView(ListView):
    model = News
    template_name = 'news/news_list.html'
    context_object_name = 'news'

    def get_queryset(self):
        return News.objects.filter(is_published=True).order_by('-created_at')

class NewsListView(ListView):
    model = News
    template_name = 'news/news_list.html'
    context_object_name = 'news'

    def get_queryset(self):
        return News.objects.filter(is_published=True).order_by('-created_at')

class NewsDetailView(DetailView):
    model = News
    template_name = 'news/news_detail.html'
    context_object_name = 'news_item'

    def get_queryset(self):
        return News.objects.filter(is_published=True)
    
def add_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news-list')
    else:
        form = NewsForm()
    return render(request, 'news/add_news.html', {'form': form})