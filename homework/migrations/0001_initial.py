# Generated by Django 4.1.4 on 2023-01-15 15:09

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import homework.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeworkTaskModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.CharField(max_length=150, verbose_name='Курс')),
                ('lesson', models.CharField(max_length=150, verbose_name='Урок')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('content', models.TextField(verbose_name='Котент')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Учитель')),
            ],
            options={
                'verbose_name': 'Домашнее задание',
                'verbose_name_plural': 'Домашние задания',
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='HomeworkAnswerModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True, verbose_name='Котент')),
                ('files', models.FileField(blank=True, upload_to=homework.models.get_file_path)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Студент')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homework.homeworktaskmodel', verbose_name='Задание')),
            ],
            options={
                'verbose_name': 'Домашняя работа',
                'verbose_name_plural': 'Домашние работы',
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='GradesForHomework',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.TextField(blank=True, verbose_name='Комментарии')),
                ('grade', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(100.0)], verbose_name='Оценка')),
                ('homework', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homework.homeworkanswermodel', verbose_name='Домашняя работа')),
            ],
            options={
                'verbose_name': 'Оценка за дз',
                'verbose_name_plural': 'Оценки за дз',
            },
        ),
    ]
