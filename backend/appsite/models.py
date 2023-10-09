from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    surname = models.CharField(max_length=30, null=True, verbose_name='Отчество')
    phone_number = models.CharField(max_length=30, null=True, verbose_name='Номер телефона')

    def __str__(self):
        return self.username


class Project(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя')
    description = models.TextField(max_length=1000, verbose_name='Описание')
    resource = models.CharField(max_length=200, verbose_name='Ресурсы')
    photo = models.ImageField(upload_to="photo/%Y/%m/%d/", verbose_name='Фото')

    def __str__(self):
        return self.name


class OrderStatus(models.TextChoices):
    CREATED = 'Создан'
    IN_PROGRESS = 'В работе'
    COMPLETED = 'Завершен'


class Order(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, verbose_name='Проект')
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders', verbose_name='Клиент')
    name = models.CharField(max_length=50, verbose_name='Название заказа')
    description = models.TextField(max_length=1000, verbose_name='Описание')
    status = models.CharField(max_length=30, choices=OrderStatus.choices, default=OrderStatus.CREATED, verbose_name='Статус')
    file = models.FileField(upload_to="file/%Y/%m/%d/", null=True, verbose_name='Договор')
