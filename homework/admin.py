from django.contrib import admin

from .models import *


@admin.register(HwTaskModel)
class HwTaskAdmin(admin.ModelAdmin):
    list_display = ['course', 'lesson', 'teacher', 'title', 'created']


@admin.register(HwAnswerModel)
class HwAnswerModel(admin.ModelAdmin):
    list_display = ['task', 'student', 'created']


@admin.register(GradesForHw)
class GradesForHwAdmin(admin.ModelAdmin):
    list_display = ['homework', 'grade']

