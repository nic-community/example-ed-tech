from . import models
from django.contrib.auth.models import User
from course.models import Course, Language
# from lesson.models import Lesson
from rest_framework import serializers


# +++++ FinalQuiz model serializer +++++
class FinalQuizRequestSerializer(serializers.Serializer):
    student = serializers.CharField()
    course = serializers.CharField()
    language = serializers.CharField()
    total_mark = serializers.FloatField()
    id = serializers.IntegerField()

    def create(self, validated_data):

        validated_data["student"] = User.objects.get(pk=validated_data["student"])
        validated_data["course"] = Course.objects.get(pk=validated_data["course"])
        validated_data["language"] = Language.objects.get(pk=validated_data["language"])
        return models.FinalQuiz.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `FinalQuiz` instance, given the validated data.
        """
        validated_data["student"] = User.objects.get(pk=validated_data["student"])
        validated_data["course"] = Course.objects.get(pk=validated_data["course"])
        validated_data["language"] = Language.objects.get(pk=validated_data["language"])

        instance.student = validated_data.get('student', instance.student)

        instance.course = validated_data.get('course', instance.course)
        instance.language = validated_data.get('language', instance.language)
        instance.total_mark = validated_data.get('total_mark', instance.total_mark)
        instance.save()

        return instance

    class Meta:
        model = models.FinalQuiz
        fields = ['id', 'student', 'course', 'language', 'total_mark']


class FinalQuizResponseSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    course = serializers.IntegerField(source="course.id")
    language = serializers.CharField(source="language.id")
    student = serializers.CharField(source="student.id")
    total_mark = serializers.FloatField()

    class Meta:
        model = models.FinalQuiz
        fields = ['id', 'student', 'course', 'language', 'total_mark']


#  FinalQuizQuestion model serializer
class FinalQuizQuestionRequestSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    related_quiz = serializers.CharField()
    text = serializers.CharField()
    mark = serializers.FloatField()

    def create(self, validated_data):
        validated_data["related_quiz"] = models.FinalQuiz.objects.get(pk=validated_data["related_quiz"])

        return models.FinalQuizQuestion.objects.create(**validated_data)


    def update(self, instance, validated_data):
        """
        Update and return an existing  instance, given the validated data.
        """

        validated_data["related_quiz"] = models.FinalQuiz.objects.get(pk=validated_data["related_quiz"])

        instance.related_quiz = validated_data.get('related_quiz', instance.related_quiz)
        instance.text = validated_data.get('text', instance.text)
        instance.mark = validated_data.get('mark', instance.mark)
        instance.save()
        return instance

    class Meta:
        model = models.FinalQuizQuestion
        fields = ['id', 'related_quiz', 'text', 'mark']


class FinalQuizQuestionResponseSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    related_quiz = serializers.IntegerField(source="related_quiz.id")
    text = serializers.CharField()
    mark = serializers.FloatField()

    class Meta:
        model = models.FinalQuizQuestion
        fields = ['id', 'related_quiz', 'text', 'mark']


#  FinalQuizAnswer model serializer
class FinalQuizAnswerRequestSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    related_question = serializers.CharField()
    content = serializers.CharField()

    def create(self, validated_data):
        validated_data["related_question"] = models.FinalQuizQuestion.objects.get(pk=validated_data["related_question"])

        return models.FinalQuizAnswer.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing instance, given the validated data.
        """
        validated_data["related_question"] = models.FinalQuizQuestion.objects.get(pk=validated_data["related_question"])

        instance.related_question = validated_data.get('related_question', instance.related_question)
        instance.content = validated_data.get('content', instance.content)
        instance.save()
        return instance

    class Meta:
        model = models.FinalQuizAnswer
        fields = ['id', 'related_question', 'content']


class FinalQuizAnswerResponseSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    related_question = serializers.CharField(source="related_question.id")
    content = serializers.CharField()

    class Meta:
        model = models.FinalQuizAnswer
        fields = ['id', 'related_question', 'content']


# +++++  LessonQuiz model serializer +++++
class LessonQuizRequestSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    student = serializers.CharField()
    lesson = serializers.CharField()
    language = serializers.CharField()
    total_mark = serializers.FloatField()

    def create(self, validated_data):
        validated_data["student"] = User.objects.get(pk=validated_data["student"])
        validated_data["lesson"] = Lesson.objects.get(pk=validated_data["lesson"])
        validated_data["language"] = Language.objects.get(pk=validated_data["language"])

        return models.LessonQuiz.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing instance, given the validated data.
        """
        validated_data["student"] = User.objects.get(pk=validated_data["student"])
        validated_data["lesson"] = Lesson.objects.get(pk=validated_data["lesson"])
        validated_data["language"] = Language.objects.get(pk=validated_data["language"])

        instance.student = validated_data.get('student', instance.student)

        instance.lesson = validated_data.get('lesson', instance.lesson)
        instance.total_mark = validated_data.get('total_mark', instance.total_mark)
        instance.language = validated_data.get('language', instance.language)
        instance.save()
        return instance

    class Meta:
        model = models.LessonQuiz
        fields = ['id', 'student', 'lesson', 'language', 'total_mark']


class LessonQuizResponseSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    student = serializers.CharField(source="student.id")
    lesson = serializers.IntegerField(source="lesson.id")
    language = serializers.CharField(source="language.id")
    total_mark = serializers.FloatField()

    class Meta:
        model = models.LessonQuiz
        fields = ['id', 'student', 'lesson', 'language', 'total_mark']


#  LessonQuizQuestion model serializers

class LessonQuizQuestionRequestSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    related_quiz = serializers.CharField()
    text = serializers.CharField()
    mark = serializers.FloatField()

    def create(self, validated_data):
        validated_data["related_quiz"] = models.LessonQuiz.objects.get(pk=validated_data["related_quiz"])

        return models.LessonQuizQuestion.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing instance, given the validated data.
        """
        validated_data["related_quiz"] = models.LessonQuiz.objects.get(pk=validated_data["related_quiz"])

        instance.related_quiz = validated_data.get('related_quiz', instance.related_quiz)
        instance.text = validated_data.get('text', instance.text)
        instance.mark = validated_data.get('mark', instance.mark)
        instance.save()
        return instance

    class Meta:
        model = models.LessonQuizQuestion
        fields = ['id', 'related_quiz', 'text', 'mark']


class LessonQuizQuestionResponseSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    related_quiz = serializers.IntegerField(source="related_quiz.id")
    text = serializers.CharField()
    mark = serializers.FloatField()

    class Meta:
        model = models.LessonQuizQuestion
        fields = ['id', 'related_quiz', 'text', 'mark']


#  LessonQuizAnswer model serializer
class LessonQuizAnswerRequestSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    related_question = serializers.CharField()
    content = serializers.CharField()

    def create(self, validated_data):
        validated_data["related_question"] = models.LessonQuizQuestion.objects.get(
            pk=validated_data["related_question"])

        return models.LessonQuizAnswer.objects.create(**validated_data)


    def update(self, instance, validated_data):
        """
        Update and return an existing instance, given the validated data.
        """

        validated_data["related_question"] = models.LessonQuizQuestion.objects.get(
            pk=validated_data["related_question"])

        instance.related_question = validated_data.get('related_question', instance.related_question)
        instance.content = validated_data.get('content', instance.content)
        instance.save()
        return instance

    class Meta:
        model = models.LessonQuizAnswer
        fields = ['id', 'related_question', 'content']


class LessonQuizAnswerResponseSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    related_question = serializers.IntegerField(source="related_question.id")
    content = serializers.CharField()

    class Meta:
        model = models.LessonQuizAnswer
        fields = ['id', 'related_question', 'content']
