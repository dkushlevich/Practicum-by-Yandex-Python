# Generated by Django 3.2 on 2023-04-09 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_auto_20230409_0648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
