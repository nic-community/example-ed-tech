# Generated by Django 4.1.4 on 2023-01-15 11:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('homework', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='homeworktaskmodel',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Учитель'),
        ),
        migrations.AddField(
            model_name='homeworkanswermodel',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Студент'),
        ),
        migrations.AddField(
            model_name='homeworkanswermodel',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homework.homeworktaskmodel', verbose_name='Задание'),
        ),
        migrations.AddField(
            model_name='gradesforhomework',
            name='homework',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homework.homeworkanswermodel', verbose_name='Домашняя работа'),
        ),
    ]
