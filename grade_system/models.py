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
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Grade: {self.grade} for {self.student.user.username} by {self.teacher.user.username}"


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="authored_news"
    )
    editor = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name="edited_news",
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title