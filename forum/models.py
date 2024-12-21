from django.db import models
from auth_sys.models import CustomUser
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        permissions = [('category_create', 'Can create category')]

class Post(models.Model):

    TYPE = [
        ('news', 'News'),
        ('update', 'Update'),
        ('event', "Event"),
        ('question','Question')
    ]

    FORUM_TYPE = [
        ('close', 'Close'),
        ('open', 'Open')
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    media = models.FileField(upload_to="post_media",blank=True,null=True)
    type = models.CharField(max_length=20,choices=TYPE)
    priority = models.CharField(max_length=20, choices=FORUM_TYPE, default='open')
    created_at = models.DateTimeField(auto_now_add=True)
    creater = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, related_name='posts')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="category")
    

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs = {'pk': self.pk})

class Comment(models.Model):
    psot_id = models.ForeignKey(Post, on_delete= models.CASCADE,related_name='comments')
    author = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING,related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    media = models.FileField(upload_to="comments_media",blank=True,null=True)

    def get_absolute_url(self):
        return self.psot_id.get_absolute_url()


class Like(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='liked_comments')
    comment = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user','comment')


class Dislike(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='disliked_comments')
    comment = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='dislikes')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user','comment')