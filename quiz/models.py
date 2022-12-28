from django.db import models


# Create your models here.
class Quiz(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='Quiz id')
    course_id = models.IntegerField(verbose_name='Course id')  # зависит от course_id model
    module_id = models.IntegerField(verbose_name='Module id')  # id того урока/дз/модуля, к которому применяется
    language = models.CharField(max_length=5,
                                verbose_name='Language in shortened format')  # окращенный вариантб например каз, рус, англ
    mark = models.FloatField()

    def __str__(self):
        return f'{self.id} - quiz id'


class Question(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='Question id')
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, verbose_name='Quiz id')  # quiz, к которому применяется
    question = models.CharField(max_length=100, verbose_name='Question text')  # текст вопроса
    correct_answer = models.IntegerField(verbose_name='Correct answer id')  # id правильного ответа
    question_mark = models.FloatField(verbose_name='Mark for question')  # кол-во баллов за правильный ответ на вопрос

    def __str__(self):
        return f'{self.id} - question id'


class Answer(models.Model):
    id = models.IntegerField(primary_key=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)  # id того вопроса, к которому применяется
    answer = models.CharField(max_length=100)  # сам ответ

    def __str__(self):
        return f'{self.id} - answer id'
