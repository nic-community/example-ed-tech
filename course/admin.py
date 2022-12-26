from django.contrib import admin

# Register your models here.
from .models import *


@admin.register(Language)
class Language(admin.ModelAdmin):
    list_display = ['title', 'description', 'updated_at', 'created_at']


@admin.register(Lecturer)
class Lecturer(admin.ModelAdmin):
    list_display = [
        'first_name',
        'last_name',
        'phone_number',
        'email',
        'description',
        'updated_at',
        'created_at'
    ]


@admin.register(Course)
class Course(admin.ModelAdmin):
    list_display = [
        'title',
        'partner',
        'topic',
        'has_certificate',
        'approximate_time_to_complete',
        'rating', 'ratings_number',
        'language',
        'lecturer',
        'description',
        'updated_at',
        'created_at'
    ]
