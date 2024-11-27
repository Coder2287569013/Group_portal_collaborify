from django.db.models.signals import post_save
from django.dispatch import receiver
from auth_sys.models import CustomUser
from django.contrib.auth.models import Group
from .models import Student, Teacher

@receiver(post_save, sender=CustomUser)
def create_related_profile(sender, instance, created, **kwargs):
    if created:
        group_id = instance.role_id
        group = Group.objects.get(id=group_id)
        if group.name == "Student":
            Student.objects.create(user=instance)
        elif group.name == "Administrator":
            Teacher.objects.create(user=instance)
