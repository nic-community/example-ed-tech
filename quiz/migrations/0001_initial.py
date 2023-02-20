# Generated by Django 4.1.4 on 2023-01-15 15:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('course', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FinalQuiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_mark', models.FloatField()),
                ('course', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='course.course', verbose_name='Course id')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.language', verbose_name='Language')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Student')),
            ],
        ),
        migrations.CreateModel(
            name='LessonQuiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_mark', models.FloatField()),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.language', verbose_name='Language')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Student')),
            ],
        ),
        migrations.CreateModel(
            name='LessonQuizQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100, verbose_name='Question text')),
                ('mark', models.FloatField(verbose_name='Mark for question')),
                ('related_quiz', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='quiz.lessonquiz', verbose_name='Quiz id')),
            ],
        ),
        migrations.CreateModel(
            name='LessonQuizAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=100)),
                ('related_question', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='quiz.lessonquizquestion')),
            ],
        ),
        migrations.CreateModel(
            name='FinalQuizQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100, verbose_name='Question text')),
                ('mark', models.FloatField(verbose_name='Mark for question')),
                ('related_quiz', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='quiz.finalquiz', verbose_name='Quiz id')),
            ],
        ),
        migrations.CreateModel(
            name='FinalQuizAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=100)),
                ('related_question', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='quiz.finalquizquestion')),
            ],
        ),
    ]
