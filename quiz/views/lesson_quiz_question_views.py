from django.shortcuts import render
# Create your views here.

from rest_framework.response import Response
from rest_framework import viewsets
from django.shortcuts import get_object_or_404

from ..models import LessonQuizQuestion
from quiz.serializers import LessonQuizQuestionRequestSerializer, LessonQuizQuestionResponseSerializer

from rest_framework import status

class LessonQuizQuestionViewSet(viewsets.ViewSet):
    """
    Example empty viewset demonstrating the standard
    actions that will be handled by a router class.

    If you're using format suffixes, make sure to also include
    the format=None keyword argument for each action.
    """

    def list(self, request):
        question = LessonQuizQuestion.objects.all()
        serializer = LessonQuizQuestionResponseSerializer(question, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = LessonQuizQuestionRequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            question = LessonQuizQuestion.objects.filter(pk=serializer.data["id"])
            return Response(question.values()[0], status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        queryset = LessonQuizQuestion.objects.all()
        question = get_object_or_404(queryset, pk=pk)
        serializer = LessonQuizQuestionResponseSerializer(question)
        return Response(serializer.data)

    def update(self, request, pk=None):
        queryset = LessonQuizQuestion.objects.all()
        question = get_object_or_404(queryset, pk=pk)
        serializer = LessonQuizQuestionRequestSerializer(question, data=request.data)
        if serializer.is_valid():
            serializer.save()
            question = LessonQuizQuestion.objects.filter(pk=serializer.data["id"])
            return Response(question.values()[0], status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        queryset = LessonQuizQuestion.objects.all()
        question = get_object_or_404(queryset, pk=pk)
        question.delete()
        return Response("Lesson Quiz Question deleted", status=status.HTTP_204_NO_CONTENT)
