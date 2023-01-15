from django.shortcuts import render
# Create your views here.

from rest_framework.response import Response
from rest_framework import viewsets
from django.shortcuts import get_object_or_404

from ..models import FinalQuizQuestion
from quiz.serializers import FinalQuizQuestionRequestSerializer, FinalQuizQuestionResponseSerializer

from rest_framework import status

class FinalQuizQuestionViewSet(viewsets.ViewSet):
    """
    Example empty viewset demonstrating the standard
    actions that will be handled by a router class.

    If you're using format suffixes, make sure to also include
    the format=None keyword argument for each action.
    """

    def list(self, request):
        question = FinalQuizQuestion.objects.all()
        serializer = FinalQuizQuestionResponseSerializer(question, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = FinalQuizQuestionRequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            question = FinalQuizQuestion.objects.filter(pk=serializer.data["id"])
            return Response(question.values()[0], status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        queryset = FinalQuizQuestion.objects.all()
        question = get_object_or_404(queryset, pk=pk)
        serializer = FinalQuizQuestionResponseSerializer(question)
        return Response(serializer.data)

    def update(self, request, pk=None):
        queryset = FinalQuizQuestion.objects.all()
        question = get_object_or_404(queryset, pk=pk)
        serializer = FinalQuizQuestionRequestSerializer(question, data=request.data)
        if serializer.is_valid():
            serializer.save()
            question = FinalQuizQuestion.objects.filter(pk=serializer.data["id"])
            return Response(question.values()[0], status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        queryset = FinalQuizQuestion.objects.all()
        question = get_object_or_404(queryset, pk=pk)
        question.delete()
        return Response("Final Quiz Question deleted", status=status.HTTP_204_NO_CONTENT)
