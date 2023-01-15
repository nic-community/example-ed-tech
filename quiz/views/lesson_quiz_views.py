from django.shortcuts import render
# Create your views here.

from rest_framework.response import Response
from rest_framework import viewsets
from django.shortcuts import get_object_or_404

from ..models import LessonQuiz
from quiz.serializers import LessonQuizRequestSerializer, LessonQuizResponseSerializer

from rest_framework import status


class LessonQuizViewSet(viewsets.ViewSet):
    """
    Example empty viewset demonstrating the standard
    actions that will be handled by a router class.

    If you're using format suffixes, make sure to also include
    the format=None keyword argument for each action.
    """

    def list(self, request):
        lesson_quiz = LessonQuiz.objects.all()
        serializer = LessonQuizResponseSerializer(lesson_quiz, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = LessonQuizRequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            lesson_quiz = LessonQuiz.objects.filter(pk=serializer.data["id"])
            return Response(lesson_quiz.values()[0], status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        queryset = LessonQuiz.objects.all()
        lesson_quiz = get_object_or_404(queryset, pk=pk)
        serializer = LessonQuizResponseSerializer(lesson_quiz)
        return Response(serializer.data)

    def update(self, request, pk=None):
        queryset = LessonQuiz.objects.all()
        lesson_quiz = get_object_or_404(queryset, pk=pk)
        serializer = LessonQuizRequestSerializer(lesson_quiz, data=request.data)
        if serializer.is_valid():
            serializer.save()
            lesson_quiz = LessonQuiz.objects.filter(pk=serializer.data["id"])
            return Response(lesson_quiz.values()[0], status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        queryset = LessonQuiz.objects.all()
        lesson_quiz = get_object_or_404(queryset, pk=pk)
        lesson_quiz.delete()
        return Response("Lesson Quiz deleted", status=status.HTTP_204_NO_CONTENT)
