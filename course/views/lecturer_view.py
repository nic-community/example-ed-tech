from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from ..serializers import *
from rest_framework import viewsets, status
from rest_framework.response import Response
from ..models import *
from django.shortcuts import get_object_or_404


class LecturerViewSet(viewsets.ViewSet):
    def list(self, request):
        lecturers = Lecturer.objects.all()
        serializer = LecturerResponseSerializer(lecturers, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        queryset = Lecturer.objects.all()
        lecturer = get_object_or_404(queryset, pk=pk)
        serializer = LecturerResponseSerializer(lecturer)
        return Response(serializer.data)

    def create(self, request):
        serializer = LecturerRequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            lecturer = Lecturer.objects.filter(pk=serializer.data["id"])
            return Response(lecturer.values()[0], status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk):
        queryset = Lecturer.objects.all()
        lecturer = get_object_or_404(queryset, pk=pk)
        serializer = LecturerRequestSerializer(lecturer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            lecturer = Lecturer.objects.filter(pk=serializer.data["id"])
            return Response(lecturer.values()[0], status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        queryset = Lecturer.objects.all()
        lecturer = get_object_or_404(queryset, pk=pk)
        lecturer.delete()
        return Response("Lecturer deleted", status=status.HTTP_204_NO_CONTENT)
