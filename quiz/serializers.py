from . import models
from rest_framework import serializers


# +++++ FinalQuiz model serializer +++++
class FinalQuizRequestSerializer(serializers.Serializer):
    course = serializers.IntegerField()
    language = serializers.CharField()
    total_mark = serializers.FloatField()

    def create(self, validated_data):
        models.FinalQuiz.objects.create(**validated_data)
        return models.FinalQuiz.objects.latest('id')

    def update(self, instance, validated_data):
        """
        Update and return an existing `FinalQuiz` instance, given the validated data.
        """

        instance.course = validated_data.get('course', instance.course)
        instance.total_mark = validated_data.get('total_mark', instance.total_mark)
        instance.language = validated_data.get('language', instance.language)
        instance.save()
        return instance

    class Meta:
        model = models.FinalQuiz
        fields = ['course', 'language', 'total_mark']


class FinalQuizResponseSerializer(serializers.Serializer):
    course = serializers.IntegerField()
    language = serializers.CharField()
    total_mark = serializers.FloatField()

    class Meta:
        model = models.FinalQuiz
        fields = ['course', 'language', 'total_mark']


#  FinalQuizQuestion model serializer
class FinalQuizQuestionRequestSerializer(serializers.Serializer):
    related_quiz = serializers.IntegerField()
    text = serializers.CharField()
    mark = serializers.FloatField()

    def create(self, validated_data):
        models.FinalQuizQuestion.objects.create(**validated_data)
        return models.FinalQuizQuestion.objects.latest('id')

    def update(self, instance, validated_data):
        """
        Update and return an existing `FinalQuiz` instance, given the validated data.
        """

        instance.related_quiz = validated_data.get('related_quiz', instance.related_quiz)
        instance.text = validated_data.get('text', instance.text)
        instance.mark = validated_data.get('mark', instance.mark)
        instance.save()
        return instance

    class Meta:
        model = models.FinalQuizQuestion
        fields = ['related_quiz', 'text', 'mark']


class FinalQuizQuestionResponseSerializer(serializers.Serializer):
    related_quiz = serializers.IntegerField()
    text = serializers.CharField()
    mark = serializers.FloatField()

    class Meta:
        model = models.FinalQuizQuestion
        fields = ['related_quiz', 'text', 'mark']


#  FinalQuizAnswer model serializer
class FinalQuizAnswerRequestSerializer(serializers.Serializer):
    related_question = serializers.IntegerField()
    content = serializers.CharField()

    def create(self, validated_data):
        models.FinalQuizAnswer.objects.create(**validated_data)
        return models.FinalQuizAnswer.objects.latest('id')

    def update(self, instance, validated_data):
        """
        Update and return an existing `FinalQuiz` instance, given the validated data.
        """

        instance.related_question = validated_data.get('related_question', instance.related_question)
        instance.content = validated_data.get('content', instance.content)
        instance.save()
        return instance

    class Meta:
        model = models.FinalQuizAnswer
        fields = ['related_question', 'content']


class FinalQuizAnswerResponseSerializer(serializers.Serializer):
    related_question = serializers.IntegerField()
    content = serializers.CharField()

    class Meta:
        model = models.FinalQuizAnswer
        fields = ['related_question', 'content']


# +++++  LessonQuiz model serializer +++++
class LessonQuizRequestSerializer(serializers.Serializer):
    lesson = serializers.IntegerField()
    language = serializers.IntegerField()
    total_mark = serializers.FloatField()

    def create(self, validated_data):
        models.LessonQuiz.objects.create(**validated_data)
        return models.LessonQuiz.objects.latest('id')

    def update(self, instance, validated_data):
        """
        Update and return an existing `FinalQuiz` instance, given the validated data.
        """

        instance.lesson = validated_data.get('lesson', instance.lesson)
        instance.total_mark = validated_data.get('total_mark', instance.total_mark)
        instance.language = validated_data.get('language', instance.language)
        instance.save()
        return instance

    class Meta:
        model = models.LessonQuiz
        fields = ['lesson', 'language', 'total_mark']


class LessonQuizResponseSerializer(serializers.Serializer):
    lesson = serializers.IntegerField()
    language = serializers.IntegerField()
    total_mark = serializers.FloatField()

    class Meta:
        model = models.LessonQuiz
        fields = ['lesson', 'language', 'total_mark']


#  LessonQuizQuestion model serializers

class LessonQuizQuestionRequestSerializer(serializers.Serializer):
    related_quiz = serializers.IntegerField()
    text = serializers.CharField()
    mark = serializers.FloatField()

    def create(self, validated_data):
        models.LessonQuizQuestion.objects.create(**validated_data)
        return models.LessonQuizQuestion.objects.latest('id')

    def update(self, instance, validated_data):
        """
        Update and return an existing `FinalQuiz` instance, given the validated data.
        """

        instance.related_quiz = validated_data.get('related_quiz', instance.related_quiz)
        instance.text = validated_data.get('text', instance.text)
        instance.mark = validated_data.get('mark', instance.mark)
        instance.save()
        return instance

    class Meta:
        model = models.LessonQuizQuestion
        fields = ['related_quiz', 'text', 'mark']


class LessonQuizQuestionResponseSerializer(serializers.Serializer):
    related_quiz = serializers.IntegerField()
    text = serializers.CharField()
    mark = serializers.FloatField()

    class Meta:
        model = models.LessonQuizQuestion
        fields = ['related_quiz', 'text', 'mark']


#  LessonQuizAnswer model serializer
class LessonQuizAnswerRequestSerializer(serializers.Serializer):
    related_question = serializers.IntegerField()
    content = serializers.CharField()

    def create(self, validated_data):
        models.LessonQuizAnswer.objects.create(**validated_data)
        return models.LessonQuizAnswer.objects.latest('id')

    def update(self, instance, validated_data):
        """
        Update and return an existing `FinalQuiz` instance, given the validated data.
        """

        instance.related_question = validated_data.get('related_question', instance.related_question)
        instance.content = validated_data.get('content', instance.content)
        instance.save()
        return instance

    class Meta:
        model = models.LessonQuizAnswer
        fields = ['related_question', 'content']


class LessonQuizAnswerResponseSerializer(serializers.Serializer):
    related_question = serializers.IntegerField()
    content = serializers.CharField()

    class Meta:
        model = models.LessonQuizAnswer
        fields = ['related_question', 'content']
