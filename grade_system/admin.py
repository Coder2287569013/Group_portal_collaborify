from django.contrib import admin
from .models import Grade , Teacher, Student, User

admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Grade)
admin.site.register(User)


