from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from course.models import *
from course.serializers import *


# ---- LANGUAGE model -----
@api_view(('GET',))
def language_list_api_view(request):
    languages = Language.objects.all()
    serializer = LanguageSerializer(languages, many=True)
    return Response(serializer.data)


@api_view(('GET',))
def language_detail_api_view(request, pk):
    language = Language.objects.get(pk=pk)
    serializer = LanguageSerializer(language)
    return Response(serializer.data)


@api_view(('POST',))
def language_create_api_view(request):
    serializer = LanguageSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(('PUT',))
def language_update_api_view(request, pk):
    try:
        task = Language.objects.get(pk=pk)
    except:
        return Response({"error": 'Object with id={0} not found'.format(pk)})
    serializer = LanguageSerializer(task, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(('DELETE',))
def language_delete_api_view(request, pk):
    try:
        task = Language.objects.get(pk=pk)
    except:
        return Response({"error": 'Object with id={0} not found'.format(pk)})
    task.delete()
    return Response("Language deleted", status=status.HTTP_204_NO_CONTENT)


# ---- LECTURER model -----
@api_view(('GET',))
def lecturer_list_api_view(request):
    lecturers = Lecturer.objects.all()
    serializer = LecturerSerializer(lecturers, many=True)
    return Response(serializer.data)


@api_view(('GET',))
def lecturer_detail_api_view(request, pk):
    lecturer = Lecturer.objects.get(pk=pk)
    serializer = LecturerSerializer(lecturer)
    return Response(serializer.data)


@api_view(('POST',))
def lecturer_create_api_view(request):
    serializer = LecturerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(('PUT',))
def lecturer_update_api_view(request, pk):
    try:
        task = Lecturer.objects.get(pk=pk)
    except:
        return Response({"error": 'Object with id={0} not found'.format(pk)})
    serializer = LecturerSerializer(task, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(('DELETE',))
def lecturer_delete_api_view(request, pk):
    try:
        task = Lecturer.objects.get(pk=pk)
    except:
        return Response({"error": 'Object with id={0} not found'.format(pk)})
    task.delete()
    return Response("Lecturer deleted", status=status.HTTP_204_NO_CONTENT)


# ---- COURSE model -----
@api_view(('GET',))
def course_list_api_view(request):
    courses = Course.objects.all()
    serializer = CourseSerializer(courses, many=True)
    return Response(serializer.data)


@api_view(('GET',))
def course_detail_api_view(request, pk):
    course = Course.objects.get(pk=pk)
    serializer = CourseSerializer(course)
    return Response(serializer.data)


@api_view(('POST',))
def course_create_api_view(request):
    serializer = CourseSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(('PUT',))
def course_update_api_view(request, pk):
    try:
        task = Course.objects.get(pk=pk)
    except:
        return Response({"error": 'Object with id={0} not found'.format(pk)})
    serializer = CourseSerializer(task, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(('DELETE',))
def course_delete_api_view(request, pk):
    try:
        task = Course.objects.get(pk=pk)
    except:
        return Response({"error": 'Object with id={0} not found'.format(pk)})
    task.delete()
    return Response("Course deleted", status=status.HTTP_204_NO_CONTENT)
