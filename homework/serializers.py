from rest_framework import serializers

from .models import *


class HomeworkTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeworkTaskModel
        fields = '__all__'


class HomeworkAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeworkAnswerModel
        fields = '__all__'


class GradesForHomeworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = GradesForHomework
        fields = '__all__'