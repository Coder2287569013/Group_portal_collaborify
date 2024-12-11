from django.db import models
from auth_sys.models import CustomUser

class Voting(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='Название'
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    creator = models.ForeignKey(
        CustomUser, 
        on_delete=models.CASCADE,
        related_name='created_votings'
    )
    is_active = models.BooleanField(
        default=True
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Голосование'
        verbose_name_plural = 'Голосования'

class Choice(models.Model):
    voting = models.ForeignKey(
        Voting,
        on_delete=models.CASCADE, 
        related_name='choices'
    )
    text = models.CharField(
        max_length=200,
        verbose_name='Вариант ответа'
    )

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Вариант ответа'
        verbose_name_plural = 'Варианты ответов'

class Vote(models.Model):
    voting = models.ForeignKey(
        Voting,
        on_delete=models.CASCADE,
        related_name='votes'
    )
    choice = models.ForeignKey(
        Choice,
        on_delete=models.CASCADE,
        related_name='votes'
    )
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='user_votes'
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        verbose_name = 'Голос'
        verbose_name_plural = 'Голоса'
        unique_together = ['user', 'voting']
