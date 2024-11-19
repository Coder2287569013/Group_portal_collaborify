from django.db import models
from auth_sys.models import CustomUser


class Teacher(models.Model):
    user = models.OneToOneField(
        CustomUser, 
        on_delete=models.CASCADE,
        related_name='teacher_profile',  
        limit_choices_to={'role': 'teacher'}  
    )

    def __str__(self):
        return f"Teacher: {self.user.username}"


class Student(models.Model):
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='student_profile',
        limit_choices_to={'role': 'student'}
    )

    def __str__(self):
        return f"Student: {self.user.username}"


class Grade(models.Model):
    TYPE_GRADE = [
        ("H", "H"),
        ("H/O", "H/O"),
    ] + [(str(i), str(i)) for i in range(1, 13)]

    student = models.ForeignKey(Student,on_delete=models.CASCADE,related_name='grades')
    teacher = models.ForeignKey(Teacher,on_delete=models.DO_NOTHING,related_name='grades')
    grade = models.CharField(max_length=20,choices=TYPE_GRADE)

    def __str__(self):
        return f"Grade: {self.grade} for {self.student.user.username} by {self.teacher.user.username}"
