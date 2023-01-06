from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from ..serializers import *
from ..models import *


class AnswerViewSet(viewsets.ViewSet):
    
    def list(self, request):
        answers = HomeworkAnswerModel.objects.all()
        serializer = HomeworkAnswerResponseSerializer(answers, many=True)
        return Response(serializer.data)
       

    def create(self, request):
        serializer = HomeworkAnswerRequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            answer = HomeworkAnswerModel.objects.filter(pk=serializer.data["id"])
            return Response(answer.values()[0], status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        queryset = HomeworkAnswerModel.objects.all()
        answer = get_object_or_404(queryset, pk=pk)
        serializer = HomeworkAnswerResponseSerializer(answer)
        return Response(serializer.data)

    def update(self, request, pk=None):
        queryset = HomeworkAnswerModel.objects.all()
        answer = get_object_or_404(queryset, pk=pk)
        serializer = HomeworkAnswerRequestSerializer(answer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            answer = HomeworkAnswerModel.objects.filter(pk=serializer.data["id"])
            return Response(answer.values()[0], status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        queryset = HomeworkAnswerModel.objects.all()
        answer = get_object_or_404(queryset, pk=pk)
        answer.delete()
        return Response("Homework answer deleted", status=status.HTTP_204_NO_CONTENT)