from django.shortcuts import render
# Create your views here.

from rest_framework.response import Response
from rest_framework import viewsets
from django.shortcuts import get_object_or_404

from ..models import FinalQuiz
from quiz.serializers import FinalQuizRequestSerializer, FinalQuizResponseSerializer

from rest_framework import status


class FinalQuizViewSet(viewsets.ViewSet):
    """
    Example empty viewset demonstrating the standard
    actions that will be handled by a router class.

    If you're using format suffixes, make sure to also include
    the format=None keyword argument for each action.
    """

    def list(self, request):
        final_quiz = FinalQuiz.objects.all()
        serializer = FinalQuizResponseSerializer(final_quiz, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = FinalQuizRequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            final_quiz = FinalQuiz.objects.filter(pk=serializer.data["id"])
            return Response(final_quiz.values()[0], status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        queryset = FinalQuiz.objects.all()
        final_quiz = get_object_or_404(queryset, pk=pk)
        serializer = FinalQuizResponseSerializer(final_quiz)
        return Response(serializer.data)

    def update(self, request, pk=None):
        queryset = FinalQuiz.objects.all()
        final_quiz = get_object_or_404(queryset, pk=pk)
        serializer = FinalQuizRequestSerializer(final_quiz, data=request.data)
        if serializer.is_valid():
            serializer.save()
            final_quiz = FinalQuiz.objects.filter(pk=serializer.data["id"])
            return Response(final_quiz.values()[0], status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        queryset = FinalQuiz.objects.all()
        final_quiz = get_object_or_404(queryset, pk=pk)
        final_quiz.delete()
        return Response("Final Quiz deleted", status=status.HTTP_204_NO_CONTENT)

