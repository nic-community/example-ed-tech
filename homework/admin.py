from django.contrib import admin

from .models import *


@admin.register(HomeworkTaskModel)
class HomeworkTaskAdmin(admin.ModelAdmin):
    list_display = ['course', 'lesson', 'teacher', 'title', 'created_at']


@admin.register(HomeworkAnswerModel)
class HomeworkAnswerModel(admin.ModelAdmin):
    list_display = ['task', 'student', 'created_at']


@admin.register(GradesForHomework)
class GradesForHomeworkAdmin(admin.ModelAdmin):
    list_display = ['homework', 'grade']