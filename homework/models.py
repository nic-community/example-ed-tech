import uuid
from django.db import models
from django.contrib.auth.models import User


class HwTaskModel(models.Model):
    """Модель для домашнего задания"""

    teacher = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Учитель") #ForeignKey(Teacher)
    course = models.CharField(max_length=150, verbose_name="Курс") #ForeignKey(Course)
    lesson = models.CharField(max_length=150, verbose_name="Урок") #ForeignKey(Lesson)
    title = models.CharField(max_length=255, verbose_name="Название")
    content = models.TextField(verbose_name="Котент") #ckeditor.fields.RichTextField
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Домашнее задание"
        verbose_name_plural = "Домашние задания"
        ordering = ['created']


class HwAnswerModel(models.Model):
    """Модель для домашней работы от ученика"""

    student = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Студент")
    task = models.ForeignKey(HwTaskModel, on_delete=models.CASCADE, verbose_name="Задание")
    content = models.TextField(verbose_name="Котент", blank=True)
    files = models.FileField(upload_to='uploads/homework/{0}'.format(uuid.uuid4()), blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{0}/{1}'.format(self.task, self.student)

    class Meta:
        verbose_name = "Домашняя работа"
        verbose_name_plural = "Домашние работы"
        ordering = ['created']


class GradesForHw(models.Model):
    """Модель оценок и обратной связи для домашней работы"""

    homework = models.ForeignKey(HwAnswerModel, on_delete=models.CASCADE, verbose_name="Домашняя работа")
    comments = models.TextField(verbose_name="Комментарии", blank=True)
    # Добавить Курс
    grade = models.FloatField(verbose_name="Оценка")

    def __str__(self):
        return 'Оценка за "{}"'.format(self.homework)

    class Meta:
        verbose_name = "Оценка за дз"
        verbose_name_plural = "Оценки за дз" 