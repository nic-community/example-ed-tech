from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from ..serializers import *
from rest_framework import viewsets, status
from rest_framework.response import Response
from ..models import *
from django.shortcuts import get_object_or_404


class CourseViewSet(viewsets.ViewSet):
    def list(self, request):
        courses = Course.objects.all()
        serializer = CourseResponseSerializer(courses, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        queryset = Course.objects.all()
        course = get_object_or_404(queryset, pk=pk)
        serializer = CourseResponseSerializer(course)
        return Response(serializer.data)

    def create(self, request):
        serializer = CourseRequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            course = Course.objects.filter(pk=serializer.data["id"])
            return Response(course.values()[0], status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk):
        queryset = Course.objects.all()
        course = get_object_or_404(queryset, pk=pk)
        serializer = CourseRequestSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            course = Course.objects.filter(pk=serializer.data["id"])
            return Response(course.values()[0], status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        queryset = Course.objects.all()
        course = get_object_or_404(queryset, pk=pk)
        course.delete()
        return Response("Course deleted", status=status.HTTP_204_NO_CONTENT)