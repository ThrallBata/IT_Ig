from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


class User(AbstractUser):
    surname = models.CharField(max_length=30, null=True, verbose_name='Отчество')
    phoneRegex = RegexValidator(regex=r"(^8|7|\+7)((\d{10})|(\s\(\d{3}\)\s\d{3}\s\d{2}\s\d{2}))")
    phone = models.CharField(validators=[phoneRegex], max_length=15, unique=True)

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
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders',
                               verbose_name='Клиент')
    name = models.CharField(max_length=50, verbose_name='Название заказа')
    description = models.TextField(max_length=1000, verbose_name='Описание')
    status = models.CharField(max_length=30, choices=OrderStatus.choices,
                              default=OrderStatus.CREATED, verbose_name='Статус')
    file = models.FileField(upload_to="file/%Y/%m/%d/", null=True, verbose_name='Договор')
