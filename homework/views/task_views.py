from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from ..serializers import *
from ..models import *
from ..repositories import HomeworkTaskRepository


class TaskViewSet(viewsets.ViewSet):
    
    def list(self, request):
        tasks = HomeworkTaskRepository.get_all()
        serializer = HomeworkTaskResponseSerializer(tasks, many=True)
        return Response(serializer.data)
       

    def create(self, request):
        serializer = HomeworkTaskRequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            task = HomeworkTaskRepository.filter(pk=serializer.data["id"])
            return Response(task.values()[0], status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        queryset = HomeworkTaskRepository.get_all()
        task = get_object_or_404(queryset, pk=pk)
        serializer = HomeworkTaskResponseSerializer(task)
        return Response(serializer.data)

    def update(self, request, pk=None):
        queryset = HomeworkTaskRepository.get_all()
        task = get_object_or_404(queryset, pk=pk)
        serializer = HomeworkTaskRequestSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            task = HomeworkTaskRepository.filter(pk=serializer.data["id"])
            return Response(task.values()[0], status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        queryset = HomeworkTaskRepository.get_all()
        task = get_object_or_404(queryset, pk=pk)
        task.delete()
        return Response("Homework task deleted", status=status.HTTP_204_NO_CONTENT)