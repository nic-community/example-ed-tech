from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *


# ---- LANGUAGE model -----
# Multiple language objects
@api_view(('GET',))
def language_list_view(request):
    languages = Language.objects.all()
    serializer = LanguageResponseSerializer(languages, many=True)
    return Response(serializer.data)


# Single language object
@api_view(('GET',))
def language_detail_view(request, pk):
    language = Language.objects.get(pk=pk)
    serializer = LanguageResponseSerializer(language)
    return Response(serializer.data)


@api_view(('POST',))
def language_create_view(request):
    serializer = LanguageRequestSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(('PATCH',))
def language_update_view(request, pk):
    try:
        task = Language.objects.get(pk=pk)
    except:
        return Response({"error": 'Object with id={0} not found'.format(pk)})
    serializer = LanguageRequestSerializer(task, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(('DELETE',))
def language_delete_view(request, pk):
    try:
        task = Language.objects.get(pk=pk)
    except:
        return Response({"error": 'Object with id={0} not found'.format(pk)})
    task.delete()
    return Response("Language deleted", status=status.HTTP_204_NO_CONTENT)


# ---- LECTURER model -----
# Multiple language objects
@api_view(('GET',))
def lecturer_list_view(request):
    lecturers = Lecturer.objects.all()
    serializer = LecturerResponseSerializer(lecturers, many=True)
    return Response(serializer.data)


@api_view(('GET',))
def lecturer_detail_view(request, pk):
    lecturer = Lecturer.objects.get(pk=pk)
    serializer = LecturerResponseSerializer(lecturer)
    return Response(serializer.data)


@api_view(('POST',))
def lecturer_create_view(request):
    serializer = LecturerRequestSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(('PATCH',))
def lecturer_update_view(request, pk):
    try:
        task = Lecturer.objects.get(pk=pk)
    except:
        return Response({"error": 'Object with id={0} not found'.format(pk)})
    serializer = LecturerRequestSerializer(task, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(('DELETE',))
def lecturer_delete_view(request, pk):
    try:
        task = Lecturer.objects.get(pk=pk)
    except:
        return Response({"error": 'Object with id={0} not found'.format(pk)})
    task.delete()
    return Response("Lecturer deleted", status=status.HTTP_204_NO_CONTENT)


# ---- COURSE model -----
@api_view(('GET',))
def course_list_view(request):
    courses = Course.objects.all()
    serializer = CourseResponseSerializer(courses, many=True)
    return Response(serializer.data)


@api_view(('GET',))
def course_detail_view(request, pk):
    course = Course.objects.get(pk=pk)
    serializer = CourseResponseSerializer(course)
    return Response(serializer.data)


@api_view(('POST',))
def course_create_view(request):
    serializer = CourseRequestSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(('PATCH',))
def course_update_view(request, pk):
    try:
        task = Course.objects.get(pk=pk)
    except:
        return Response({"error": 'Object with id={0} not found'.format(pk)})
    serializer = CourseRequestSerializer(task, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(('DELETE',))
def course_delete_view(request, pk):
    try:
        task = Course.objects.get(pk=pk)
    except:
        return Response({"error": 'Object with id={0} not found'.format(pk)})
    task.delete()
    return Response("Course deleted", status=status.HTTP_204_NO_CONTENT)
