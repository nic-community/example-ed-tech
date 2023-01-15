from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from ..serializers import *
from ..models import *


class GradeViewSet(viewsets.ViewSet):
    
    def list(self, request):
        grades = GradesForHomework.objects.all()
        serializer = HomeworkGradeResponseSerializer(grades, many=True)
        return Response(serializer.data)
       

    def create(self, request):
        serializer = HomeworkGradeRequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            grade = GradesForHomework.objects.filter(pk=serializer.data["id"])
            return Response(grade.values()[0], status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        queryset = GradesForHomework.objects.all()
        grade = get_object_or_404(queryset, pk=pk)
        serializer = HomeworkGradeResponseSerializer(grade)
        return Response(serializer.data)

    def update(self, request, pk=None):
        queryset = GradesForHomework.objects.all()
        grade = get_object_or_404(queryset, pk=pk)
        serializer = HomeworkGradeRequestSerializer(grade, data=request.data)
        if serializer.is_valid():
            serializer.save()
            grade = GradesForHomework.objects.filter(pk=serializer.data["id"])
            return Response(grade.values()[0], status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        queryset = GradesForHomework.objects.all()
        grade = get_object_or_404(queryset, pk=pk)
        grade.delete()
        return Response("Homework grade deleted", status=status.HTTP_204_NO_CONTENT)