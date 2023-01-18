from django.contrib import admin
from user.models import *


# Register your models here.
@admin.register(User)
class User(admin.ModelAdmin):
    list_display = ['email']
