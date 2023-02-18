from django.db import models


# Create your models here.

class Language(models.Model):
    title = models.CharField(max_length=100)

    description = models.TextField(blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Язык"
        verbose_name_plural = "Языки"
        ordering = ['title']


class Lecturer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15, blank=True)
    email = models.CharField(max_length=256, blank=True)

    description = models.TextField(blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Full name: {self.last_name} {self.first_name}"

    class Meta:
        verbose_name = "Лектор"
        verbose_name_plural = "Лекторы"
        ordering = ['last_name']


class Course(models.Model):
    title = models.TextField()
    # Партнёр курса. К примеру: "University of Michigan"
    partner = models.CharField(max_length=200)
    # Затрагиваемый стек. К примеру: "Python (Django)"
    topic = models.CharField(max_length=100)
    has_certificate = models.BooleanField()
    approximate_time_to_complete = models.IntegerField(default=0)
    rating = models.FloatField(default=0)
    ratings_number = models.IntegerField(default=0)

    # ------ FOREIGN KEYS ------
    # Основной язык курса (тот, на котором говорят учителя в озвучке)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, verbose_name="Язык курса")
    lecturer = models.ForeignKey(Lecturer, on_delete=models.CASCADE, verbose_name="Лектор")

    description = models.TextField(blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Title: {self.title} | Partner: {self.partner} | Topic: {self.topic}"

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"
        ordering = ['created_at']
