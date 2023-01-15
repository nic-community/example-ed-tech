from django.contrib.auth.models import AbstractUser, PermissionsMixin, UserManager
from django.db import models
from course.models import Course


# Create your models here.
class User(AbstractUser, PermissionsMixin):
    email = models.EmailField(max_length=256, unique=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Курс ученика", blank=True, null=True)
    date_of_birth = models.DateTimeField(blank=True, null=True)

    # ENUM Roles
    class Roles(models.IntegerChoices):
        STUDENT = 1
        TEACHER = 2
        ADMIN = 3

    role = models.IntegerField(choices=Roles.choices, default=Roles.STUDENT)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    # LOGIN DATA
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email