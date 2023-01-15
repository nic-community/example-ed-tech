from django.shortcuts import render
# Create your views here.

from rest_framework.response import Response
from rest_framework import viewsets
from django.shortcuts import get_object_or_404

from ..models import FinalQuizAnswer

from quiz.serializers import FinalQuizAnswerRequestSerializer, FinalQuizAnswerResponseSerializer

from rest_framework import status


class FinalQuizAnswerViewSet(viewsets.ViewSet):
    """
    Example empty viewset demonstrating the standard
    actions that will be handled by a router class.

    If you're using format suffixes, make sure to also include
    the format=None keyword argument for each action.
    """

    def list(self, request):
        answer = FinalQuizAnswer.objects.all()
        serializer = FinalQuizAnswerResponseSerializer(answer, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = FinalQuizAnswerRequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            answer = FinalQuizAnswer.objects.filter(pk=serializer.data["id"])
            return Response(answer.values()[0], status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        queryset = FinalQuizAnswer.objects.all()
        answer = get_object_or_404(queryset, pk=pk)
        serializer = FinalQuizAnswerResponseSerializer(answer)
        return Response(serializer.data)

    def update(self, request, pk=None):
        queryset = FinalQuizAnswer.objects.all()
        answer = get_object_or_404(queryset, pk=pk)
        serializer = FinalQuizAnswerRequestSerializer(answer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            answer = FinalQuizAnswer.objects.filter(pk=serializer.data["id"])
            return Response(answer.values()[0], status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        queryset = FinalQuizAnswer.objects.all()
        answer = get_object_or_404(queryset, pk=pk)
        answer.delete()
        return Response("Final Quiz Answer deleted", status=status.HTTP_204_NO_CONTENT)
