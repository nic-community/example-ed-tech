from django.http import JsonResponse
from rest_framework import serializers
from .models import *
from django.forms.models import model_to_dict
from rest_framework.renderers import JSONRenderer

# ----- LANGUAGE MODEL SERIALIZERS -----
class LanguageRequestSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=100)
    description = serializers.CharField(required=False)

    def create(self, validated_data):
        return Language.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance

    class Meta:
        model = Language
        fields = ['id', 'title', 'description']


class LanguageResponseSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=100)
    description = serializers.CharField(required=False)
    updated_at = serializers.DateTimeField()
    created_at = serializers.DateTimeField()

    class Meta:
        model = Language
        fields = ['id', 'title', 'description']


# ----- LECTURER MODEL SERIALIZERS -----
class LecturerRequestSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    phone_number = serializers.CharField(max_length=15, required=False)
    email = serializers.CharField(max_length=256, required=False)
    description = serializers.CharField(required=False)

    def create(self, validated_data):
        return Lecturer.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.description = validated_data.get('description', instance.description)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance

    class Meta:
        model = Lecturer
        fields = [
            'id',
            'first_name',
            'last_name',
            'phone_number',
            'email',
            'description',
        ]


class LecturerResponseSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    phone_number = serializers.CharField(max_length=15, required=False)
    email = serializers.CharField(max_length=256, required=False)
    description = serializers.CharField(required=False)
    updated_at = serializers.DateTimeField()
    created_at = serializers.DateTimeField()

    class Meta:
        model = Lecturer
        fields = [
            'id',
            'first_name',
            'last_name',
            'phone_number',
            'email',
            'description',
            'updated_at',
            'created_at'
        ]


# ----- COURSE MODEL SERIALIZERS -----
class CourseRequestSerializer(serializers.ModelSerializer):
    title = serializers.CharField()
    partner = serializers.CharField(max_length=200)
    topic = serializers.CharField(max_length=100)
    has_certificate = serializers.BooleanField()
    approximate_time_to_complete = models.IntegerField(default=0)
    rating = serializers.FloatField(default=0)
    ratings_number = serializers.IntegerField(default=0)
    language = serializers.CharField()
    lecturer = serializers.CharField()
    description = serializers.CharField(required=False)

    def create(self, validated_data):
        validated_data["language"] = Language.objects.get(pk=validated_data["language"])
        validated_data["lecturer"] = Lecturer.objects.get(pk=validated_data["lecturer"])
        return Course.objects.create(**validated_data)

    def update(self, instance, validated_data):
        validated_data["language"] = Language.objects.get(pk=validated_data["language"])
        validated_data["lecturer"] = Lecturer.objects.get(pk=validated_data["lecturer"])
        instance.title = validated_data.get('title', instance.title)
        instance.partner = validated_data.get('partner', instance.partner)
        instance.topic = validated_data.get('topic', instance.topic)
        instance.has_certificate = validated_data.get('has_certificate', instance.has_certificate)
        instance.approximate_time_to_complete = validated_data.get('approximate_time_to_complete', instance.approximate_time_to_complete)
        instance.rating = validated_data.get('rating', instance.rating)
        instance.ratings_number = validated_data.get('ratings_number', instance.ratings_number)
        instance.language = validated_data.get('language', instance.language)
        instance.lecturer = validated_data.get('lecturer', instance.lecturer)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance

    class Meta:
        model = Course
        fields = [
            'id',
            'title',
            'partner',
            'topic',
            'has_certificate',
            'approximate_time_to_complete',
            'rating',
            'ratings_number',
            'language',
            'lecturer',
            'description',
        ]


class CourseResponseSerializer(serializers.ModelSerializer):
    title = serializers.CharField()
    partner = serializers.CharField(max_length=200)
    topic = serializers.CharField(max_length=100)
    has_certificate = serializers.BooleanField()
    approximate_time_to_complete = models.IntegerField(default=0)
    rating = serializers.FloatField(default=0)
    ratings_number = serializers.IntegerField(default=0)
    language = serializers.IntegerField(source='language.id')
    lecturer = serializers.IntegerField(source='lecturer.id')
    description = serializers.CharField(required=False)

    class Meta:
        model = Course
        fields = [
            'id',
            'title',
            'partner',
            'topic',
            'has_certificate',
            'approximate_time_to_complete',
            'rating',
            'ratings_number',
            'language',
            'lecturer',
            'description',
            'updated_at',
            'created_at'
        ]
