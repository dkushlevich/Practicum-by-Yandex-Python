# Generated by Django 3.2 on 2023-04-18 05:00

import reviews.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0006_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='confirmation_code',
            field=models.CharField(blank=True, max_length=4, verbose_name='Код подтверждения'),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('user', 'Аутентифицированнный пользователь'), ('moderator', 'Модератор'), ('admin', 'Администратор')], default='user', max_length=33, verbose_name='Роль'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(error_messages={'unique': 'Пользователь с таким именем уже существует'}, max_length=150, unique=True, validators=[reviews.validators.username_validator], verbose_name='Имя пользователя'),
        ),
    ]
