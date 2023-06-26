# Generated by Django 4.1.7 on 2023-06-26 09:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appsite', '0002_chat_status_view_order_file_alter_chat_staff_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='staff',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='staff', to=settings.AUTH_USER_MODEL, verbose_name='Работник'),
        ),
    ]
