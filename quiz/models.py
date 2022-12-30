from django.db import models
from course.models import Course
from course.models import Language
# from lesson.models import Lesson


# Create your models here.
class FinalQuiz(models.Model):
    course = models.OneToOneField(to=Course, on_delete=models.CASCADE,
                                  verbose_name='Course id')  # зависит от course_id model
    language = models.OneToOneField(to=Language, on_delete=models.CASCADE,
                                    verbose_name='Language')  # язык курса совпадает с языком теста
    total_mark = models.FloatField()

    def __str__(self):
        return f'Final mark for Quiz to Course {self.course.name} - {self.mark}'


class LessonQuiz(models.Model):
    # т. к. зависит от модели Lesson,то пока комментарием
    # lesson = models.OneToOneField(to=Lesson, on_delete=models.CASCADE,
                                  # verbose_name='Lesson id')  # зависит от Lesson model
    language = models.OneToOneField(to=Language, on_delete=models.CASCADE,
                                    verbose_name='Language')  # язык курса совпадает с языком теста
    total_mark = models.FloatField()

    def __str__(self):
        return f'Final mark for Quiz to Course {self.lesson.name} - {self.mark}'


class FinalQuizQuestion(models.Model):
    related_quiz = models.OneToOneField(FinalQuiz, on_delete=models.CASCADE,
                                verbose_name='Quiz id')  # quiz, к которому применяется
    text = models.CharField(max_length=100, verbose_name='Question text')  # текст вопроса
    mark = models.FloatField(verbose_name='Mark for question')  # кол-во баллов за правильный ответ на вопрос

    def __str__(self):
        return f'{self.question} - question'


class LessonQuizQuestion(models.Model):
    related_quiz = models.OneToOneField(LessonQuiz, on_delete=models.CASCADE,
                                verbose_name='Quiz id')  # quiz, к которому применяется
    text = models.CharField(max_length=100, verbose_name='Question text')  # текст вопроса
    mark = models.FloatField(verbose_name='Mark for question')  # кол-во баллов за правильный ответ на вопрос

    def __str__(self):
        return f'{self.question} - question'


class FinalQuizAnswer(models.Model):
    related_question = models.OneToOneField(FinalQuizQuestion,
                                    on_delete=models.CASCADE)  # id того вопроса, к которому применяется
    content = models.CharField(max_length=100)  # сам ответ

    def __str__(self):
        return f'{self.answer} - answer'


class LessonQuizAnswer(models.Model):
    related_question = models.OneToOneField(LessonQuizQuestion,
                                    on_delete=models.CASCADE)  # id того вопроса, к которому применяется
    content = models.CharField(max_length=100)  # сам ответ

    def __str__(self):
        return f'{self.answer} - answer'
