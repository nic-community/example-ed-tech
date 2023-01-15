from django.db import models
from course.models import Course
from course.models import Language


from user.models import User


# from lesson.models import Lesson


# Create your models here.
class FinalQuiz(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Student") # студент к которому  привязывается конкретная оценка

    course = models.OneToOneField(to=Course,on_delete=models.CASCADE,  verbose_name='Course id')  # зависит от course_id model
    language = models.ForeignKey(to=Language, on_delete=models.CASCADE, verbose_name='Language')  # язык курса совпадает с языком теста
    total_mark = models.FloatField() #оценка за тест для студента, а не в целом максимальная за тест

    def __str__(self):
        return f'Final mark for Quiz to Course {self.course.title} - {self.total_mark}'


class LessonQuiz(models.Model):
    # т. к. зависит от модели Lesson,то пока комментарием
    # lesson = models.OneToOneField(to=Lesson, on_delete=models.CASCADE,
    #                               verbose_name='Lesson id')  # зависит от Lesson model

    language = models.ForeignKey(to=Language, on_delete=models.CASCADE, verbose_name='Language')  # язык курса совпадает с языком теста

    student = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Student") # студент, к которому привязывается конкретная оценка

    total_mark = models.FloatField()

    def __str__(self):
        return f'Final mark for Quiz to Lesson {self.lesson.name} - {self.total_mark}'


class FinalQuizQuestion(models.Model):
    related_quiz = models.OneToOneField(FinalQuiz, on_delete=models.CASCADE,
                                        verbose_name='Quiz id')  # quiz, к которому применяется
    text = models.CharField(max_length=100, verbose_name='Question text')  # текст вопроса
    mark = models.FloatField(verbose_name='Mark for question')  # кол-во баллов за правильный ответ на вопрос

    def __str__(self):
        return f'{self.text} - question'


class LessonQuizQuestion(models.Model):
    related_quiz = models.OneToOneField(LessonQuiz, on_delete=models.CASCADE,
                                        verbose_name='Quiz id')  # quiz, к которому применяется
    text = models.CharField(max_length=100, verbose_name='Question text')  # текст вопроса
    mark = models.FloatField(verbose_name='Mark for question')  # кол-во баллов за правильный ответ на вопрос

    def __str__(self):
        return f'{self.text} - question'


class FinalQuizAnswer(models.Model):
    related_question = models.OneToOneField(FinalQuizQuestion,
                                            on_delete=models.CASCADE)  # id того вопроса, к которому применяется
    content = models.CharField(max_length=100)  # сам ответ

    def __str__(self):
        return f'{self.content} - answer'


class LessonQuizAnswer(models.Model):
    related_question = models.OneToOneField(LessonQuizQuestion,
                                            on_delete=models.CASCADE)  # id того вопроса, к которому применяется
    content = models.CharField(max_length=100)  # сам ответ

    def __str__(self):
        return f'{self.content} - answer'
