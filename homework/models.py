import os
import uuid
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from user.models import User


class HomeworkTaskModel(models.Model):
    """Модель для домашнего задания"""

    teacher = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Учитель") #ForeignKey(Teacher)
    course = models.CharField(max_length=150, verbose_name="Курс") #ForeignKey(Course)
    lesson = models.CharField(max_length=150, verbose_name="Урок") #ForeignKey(Lesson)
    title = models.CharField(max_length=255, verbose_name="Название")
    content = models.TextField(verbose_name="Котент") #ckeditor.fields.RichTextField
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Домашнее задание"
        verbose_name_plural = "Домашние задания"
        ordering = ['created_at']


def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('uploads/homework', filename)


class HomeworkAnswerModel(models.Model):

    """Модель для домашней работы от ученика"""

    student = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Студент")
    task = models.ForeignKey(HomeworkTaskModel, on_delete=models.CASCADE, verbose_name="Задание")
    content = models.TextField(verbose_name="Котент", blank=True)
    files = models.FileField(upload_to=get_file_path, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{0}/{1}'.format(self.task, self.student)

    class Meta:
        verbose_name = "Домашняя работа"
        verbose_name_plural = "Домашние работы"
        ordering = ['created_at']


class GradesForHomework(models.Model):
    """Модель оценок и обратной связи для домашней работы"""

    homework = models.ForeignKey(HomeworkAnswerModel, on_delete=models.CASCADE, verbose_name="Домашняя работа")
    comments = models.TextField(verbose_name="Комментарии", blank=True)
    grade = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(100.0)], verbose_name="Оценка")

    def __str__(self):
        return 'Оценка за "{}"'.format(self.homework)

    class Meta:
        verbose_name = "Оценка за дз"
        verbose_name_plural = "Оценки за дз" 