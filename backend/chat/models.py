from django.db import models

from appsite.models import User


class Chat(models.Model):
    staff = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chats', default=1, verbose_name='Работник')
    client = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Клиент')
    status_view = models.BooleanField(default=False)


class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, null=True, related_name='messages', verbose_name='Чат')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name='Пользователь')
    content = models.TextField(max_length=1000, verbose_name='Контент')
    file = models.FileField(upload_to="file/%Y/%m/%d/", null=True, verbose_name='Файл')
