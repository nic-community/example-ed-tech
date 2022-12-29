from django.shortcuts import render
from django.http import JsonResponse 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import *
from .serializers import *

# Homework Tasks
@api_view(('GET',))
def homework_task_list_API_view(request):
    tasks = HomeworkTaskModel.objects.all()
    serializer = HomeworkTaskSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(('GET',))
def homework_task_detail_API_view(request, pk):
    task = HomeworkTaskModel.objects.get(pk=pk)
    serializer = HomeworkTaskSerializer(task)
    return Response(serializer.data)


@api_view(('POST',))
def homework_taks_create_API_view(request):
    serializer = HomeworkTaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(('PUT',))
def homework_task_update_API_view(request, pk):
    try:
        task = HomeworkTaskModel.objects.get(pk=pk)
    except:
        return Response({"error": 'Object with id={0} not found'.format(pk)})
    serializer = HomeworkTaskSerializer(task, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(('DELETE',))
def homework_task_delete_API_view(request, pk):
    try:
        task = HomeworkTaskModel.objects.get(pk=pk)
    except:
        return Response({"error": 'Object with id={0} not found'.format(pk)})
    task.delete()
    return Response("Homework task deleted", status=status.HTTP_204_NO_CONTENT)


#Homework Answers
@api_view(('GET',))
def homework_answer_list_API_view(request):
    answers = HomeworkAnswerModel.objects.all()
    serializer = HomeworkAnswerSerializer(answers, many=True)
    return Response(serializer.data)


@api_view(('GET',))
def homework_answer_detail_API_view(request, pk):
    answer = HomeworkAnswerModel.objects.get(pk=pk)
    serializer = HomeworkAnswerSerializer(answer)
    return Response(serializer.data)


@api_view(('POST',))
def homework_answer_create_API_view(request):
    serializer = HomeworkAnswerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(('PUT',))
def homework_answer_update_API_view(request, pk):
    try:
        answer = HomeworkAnswerModel.objects.get(pk=pk)
    except:
        return Response({"error": 'Object with id={0} not found'.format(pk)})
    serializer = HomeworkAnswerSerializer(answer, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(('DELETE',))
def homework_answer_delete_API_view(request, pk):
    try:
        answer = HomeworkAnswerModel.objects.get(pk=pk)
    except:
        return Response({"error": 'Object with id={0} not found'.format(pk)})
    answer.delete()
    return Response("Homework Answer deleted", status=status.HTTP_204_NO_CONTENT)


# Grades 
@api_view(('GET',))
def homework_grade_list_API_view(request):
    grades = GradesForHomework.objects.all()
    serializer = GradesForHomeworkSerializer(grades, many=True)
    return Response(serializer.data)


@api_view(('GET',))
def homework_grade_detail_API_view(request, pk):
    grade = GradesForHomework.objects.get(pk=pk)
    serializer = GradesForHomeworkSerializer(grade)
    return Response(serializer.data)


@api_view(('POST',))
def homework_grade_create_API_view(request):
    serializer = GradesForHomeworkSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(('PUT',))
def homework_grade_update_API_view(request, pk):
    try:
        grade = GradesForHomework.objects.get(pk=pk)
    except:
        return Response({"error": 'Object with id={0} not found'.format(pk)})
    serializer = GradesForHomeworkSerializer(grade, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(('DELETE',))
def homework_grade_delete_API_view(request, pk):
    try:
        grade = GradesForHomework.objects.get(pk=pk)
    except:
        return Response({"error": 'Object with id={0} not found'.format(pk)})
    grade.delete()
    return Response("Homework Answer deleted", status=status.HTTP_204_NO_CONTENT)