from django.db import models
from auth_sys.models import CustomUser

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="authored_news"
    )
    editor = models.ForeignKey(
        CustomUser,
        on_delete=models.SET_NULL,
        related_name="edited_news",
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title