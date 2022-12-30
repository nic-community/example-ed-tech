from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.LessonQuiz)
admin.site.register(models.FinalQuiz)
admin.site.register(models.FinalQuizQuestion)
admin.site.register(models.LessonQuizQuestion)
admin.site.register(models.FinalQuizAnswer)
admin.site.register(models.LessonQuizAnswer)
