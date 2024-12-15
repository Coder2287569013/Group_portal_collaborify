from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, ListView, DetailView
from auth_sys.models import CustomUser
from django.urls import reverse_lazy
from .models import Grade, Student, Teacher
from .forms import GradeForm

class StudentListView(ListView):
    model = CustomUser
    context_object_name = 'students'

    def get_queryset(self):
        students = CustomUser.objects.filter(role__name='Student')
        return students


class StudentDetailView(DetailView):
    model = CustomUser
    context_object_name = 'student'
    template_name = 'grade_system/student_detail.html'  

    def get_queryset(self):
        return CustomUser.objects.filter(role__name='Student')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['grade_form'] = GradeForm()
        return context
    
    def post(self, request, *args, **kwargs):
        student = self.get_object()
        grade_form = GradeForm(request.POST)

        if grade_form.is_valid():
            grade = grade_form.save(commit=False)
            grade.teacher = Teacher.objects.get(user = request.user)  # Прив'язуємо вчителя
            grade.student = Student.objects.get(user = student)  # Прив'язуємо студента
            grade.save()
            return redirect('student-detail', pk=student.id)

        return render(request, self.template_name, {
            'student': student,
            'grade_form': grade_form,
        })

