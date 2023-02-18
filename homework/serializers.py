from rest_framework import serializers
from django.contrib.auth.models import User

from .models import *
from .repositories import *


class HomeworkTaskRequestSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    teacher = serializers.CharField()
    course = serializers.CharField(max_length=150)
    lesson = serializers.CharField(max_length=150)
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()

    def create(self, validated_data):
        validated_data["teacher"] = User.objects.get(pk=validated_data["teacher"])
        return HomeworkTaskRepository.create(**validated_data)

    def update(self, instance, validated_data):
        validated_data["teacher"] = User.objects.get(pk=validated_data["teacher"])
        instance.teacher = validated_data.get('teacher', instance.teacher)
        instance.lesson = validated_data.get('lesson', instance.lesson)
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.save()
        return instance

    class Meta: 
        model = HomeworkTaskModel
        fields = ['id', 'teacher', 'course', 'lesson', 'title', 'content']


class HomeworkTaskResponseSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    teacher = serializers.IntegerField(source='teacher.id')
    course = serializers.CharField(max_length=150)
    lesson = serializers.CharField(max_length=150)
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta: 
        model = HomeworkTaskModel
        fields = ['id', 'teacher', 'course', 'lesson', 'title', 'content', 'created_at', 'updated_at']
        # fields = '__all__'


class HomeworkAnswerRequestSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    student = serializers.CharField()
    task = serializers.CharField()
    content = serializers.CharField(allow_blank=True, required=False)
    files = serializers.FileField(required=False)

    def create(self, validated_data):
        validated_data["student"] = User.objects.get(pk=validated_data["student"])
        validated_data["task"] = HomeworkTaskRepository.get_by_id(id=validated_data["task"])
        return HomeworkAnswerRepository.create(**validated_data)
    
    def update(self, instance, validated_data):
        validated_data["student"] = User.objects.get(pk=validated_data["student"])
        validated_data["task"] = HomeworkTaskModel.objects.get(pk=validated_data["task"])
        instance.student = validated_data.get('student', instance.student)
        instance.task = validated_data.get('task', instance.task)
        instance.content = validated_data.get('content', instance.content)
        instance.files = validated_data.get('files', instance.files)
        instance.save()
        return instance

    class Meta:
        model = HomeworkAnswerModel
        fields = ['id', 'student', 'task', 'content', 'files']


class HomeworkAnswerResponseSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    student = serializers.IntegerField(source='student.id')
    task = serializers.IntegerField(source='task.id')
    content = serializers.CharField(allow_blank=True)
    files = serializers.FileField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        model = HomeworkAnswerModel
        fields = ['id', 'student', 'task', 'content', 'files', 'created_at', 'updated_at']


class HomeworkGradeRequestSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    homework = serializers.CharField()
    comments = serializers.CharField(allow_blank=True, required=False)
    grade = serializers.FloatField(max_value=100.0, min_value=0.0)

    def create(self, validated_data):
        validated_data["homework"] = HomeworkAnswerRepository.get_by_id(id=validated_data["homework"])
        return HomeworkGradeRepository.create(**validated_data)

    def update(self, instance, validated_data):
        validated_data["homework"] = HomeworkAnswerModel.objects.get(pk=validated_data["homework"])
        instance.homework = validated_data.get('homework', instance.homework)
        instance.comments = validated_data.get('comments', instance.comments)
        instance.grade = validated_data.get('grade', instance.grade)
        instance.save()
        return instance

    class Meta:
        model = GradesForHomework
        fields = ['id', 'homework', 'comments', 'grade']


class HomeworkGradeResponseSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    homework = serializers.IntegerField(source='homework.id')
    comments = serializers.CharField(allow_blank=True)
    grade = serializers.FloatField()

    class Meta:
        model = GradesForHomework
        fields = ['id', 'homework', 'comments', 'grade']