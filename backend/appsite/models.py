from django.db import models
from django.contrib.auth.models import AbstractUser

from django.conf import settings


class User(AbstractUser):
    surname = models.CharField(max_length=30, verbose_name='Клиент')
    phone_number = models.CharField(max_length=30, verbose_name='Клиент')

    def __str__(self):
        return self.username


class Chat(models.Model):
    staff_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='staff', verbose_name='Работник')
    client_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Клиент')


class Message(models.Model):
    chat_id = models.ForeignKey('Chat', on_delete=models.CASCADE, verbose_name='Чат')
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь')
    content = models.TextField(max_length=1000, verbose_name='Клиент')
    file = models.FileField(upload_to="file/%Y/%m/%d/", verbose_name='Клиент')# необязательно


class Project(models.Model):
    name = models.CharField(max_length=50, verbose_name='Клиент')
    description = models.TextField(max_length=1000, verbose_name='Клиент')
    resource = models.CharField(max_length=200, verbose_name='Клиент')
    photo = models.ImageField(upload_to="photo/%Y/%m/%d/", verbose_name='Клиент')


class Order(models.Model):
    name = models.CharField(max_length=50, verbose_name='Клиент')
    description = models.TextField(max_length=1000, verbose_name='Клиент')
    status = models.BooleanField()
    project_id = models.ForeignKey('Project', on_delete=models.CASCADE, verbose_name='Проект')
    client_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Клиент')


