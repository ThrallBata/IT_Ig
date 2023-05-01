from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    surname = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=30)


class Chat(models.Model):
    members = models.ManyToManyField(User, verbose_name="Участники")
    # staff_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Работник')
    # client_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Клиент')


class Message(models.Model):
    chat_id = models.ForeignKey(Chat, on_delete=models.CASCADE, verbose_name='Чат')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    content = models.TextField(max_length=1000)
    file = models.FileField(upload_to="file/%Y/%m/%d/")


class Project(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)
    resource = models.CharField(max_length=200)
    photo = models.ImageField(upload_to="photo/%Y/%m/%d/")


class Order(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)
    status = models.BooleanField()
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name='Чат')
    client_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Клиент')


