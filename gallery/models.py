from django.db import models
from auth_sys.models import CustomUser
from django.urls import reverse

class Photo(models.Model):
    class Meta:
        ordering = ['-id']

    image = models.FileField(upload_to="gallery",blank=True,null=True)
    creater = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, related_name='galaries')
    creat_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.creater
    

def get_absolute_url(self):
        return reverse('post-detail', kwargs = {'pk': self.pk})