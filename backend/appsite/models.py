from django.db import models
from django.contrib.auth.models import AbstractUser

from django.conf import settings


class User(AbstractUser):
    surname = models.CharField(max_length=30, null=True, verbose_name='Отчество')
    phone_number = models.CharField(max_length=30, null=True, verbose_name='Номер телефона')

    def __str__(self):
        return self.username


class Chat(models.Model):
    staff = models.ForeignKey(User, on_delete=models.CASCADE, related_name='staff', verbose_name='Работник')
    client = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Клиент')


class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, null=True, verbose_name='Чат')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name='Пользователь')
    content = models.TextField(max_length=1000, verbose_name='Контент')
    file = models.FileField(upload_to="file/%Y/%m/%d/", null=True, verbose_name='Файл')


class Project(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя')
    description = models.TextField(max_length=1000, verbose_name='Описание')
    resource = models.CharField(max_length=200, verbose_name='Ресурсы')
    photo = models.ImageField(upload_to="photo/%Y/%m/%d/", verbose_name='Фото')

    def __str__(self):
        return self.name


class OrderStatus(models.Model):
    status = models.CharField(max_length=50, verbose_name='Статус')

    def __str__(self):
        return self.status


class Order(models.Model):
    name = models.CharField(max_length=50, verbose_name='Клиент')
    description = models.TextField(max_length=1000, verbose_name='Описание')
    status = models.ForeignKey(OrderStatus, on_delete=models.CASCADE, default=1, verbose_name='Статус')#таблица с полем вариантами состояния и как вторичный ключ
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, verbose_name='Проект')
    client = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Клиент')


