# Generated by Django 4.0.5 on 2022-06-16 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_web', '0002_completedtodo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='completedtodo',
            name='completed_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
