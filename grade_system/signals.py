from django.db.models.signals import post_save
from django.dispatch import receiver
from auth_sys.models import CustomUser
from .models import Student, Teacher

@receiver(post_save, sender=CustomUser)
def create_related_profile(sender, instance, created, **kwargs):
    if created:  # Виконується тільки при створенні нового користувача
        if instance.role__name == 'Student':
            Student.objects.create(user=instance)
        elif instance.role__name == 'Adminstrator':
            Teacher.objects.create(user=instance)
