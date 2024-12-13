from django.db import models

class UsefulLink(models.Model):
    title = models.CharField(max_length=200, verbose_name="Назва")
    url = models.URLField(verbose_name="Ссылка")
    description = models.TextField(blank=True, verbose_name="Опис")
    image = models.ImageField(upload_to='link_images/', blank=True, null=True, verbose_name="Зображення")

    def __str__(self):
        return self.title
