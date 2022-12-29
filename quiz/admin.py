from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(LessonQuiz)
admin.site.register(FinalQuiz)
admin.site.register(QuestionsForFinalQuiz)
admin.site.register(QuestionsForLessonQuiz)
admin.site.register(AnswerForFinalQuizQuestion)
admin.site.register(AnswerForLessonQuizQuestion)
