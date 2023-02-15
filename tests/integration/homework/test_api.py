import pytest
import json

from rest_framework import status
from django.test import Client

from user.models import User
from homework.models import *


class TestHomeworkTaskApi():

    client = Client()
    
    @pytest.mark.django_db
    def test_list_get(self):
        user = User.objects.create(username='User', email='user@gmail.com', phone_number='+7777777777')
        task = HomeworkTaskModel.objects.create(teacher=user, course='java', lesson='first lesson', title="java tests", content='java tests')

        url = '/homework/api/tasks/'
        response = self.client.get(url)

        assert response.status_code == status.HTTP_200_OK
        assert response.json()[0]["teacher"] == task.teacher.id
        assert response.json()[0]['course'] == task.course
        assert response.json()[0]['lesson'] == task.lesson
        assert response.json()[0]['title'] == task.title
        assert response.json()[0]['content'] == task.content

    @pytest.mark.django_db
    def test_detail_get(self):
        user = User.objects.create(username='User', email='user@gmail.com', phone_number='+7777777777')
        task = HomeworkTaskModel.objects.create(teacher=user, course='java', lesson='first lesson', title="java tests", content='java tests')
        
        url = '/homework/api/tasks/'+str(task.id)+'/'
        response = self.client.get(url)

        assert response.status_code == status.HTTP_200_OK 

    @pytest.mark.django_db
    def test_post(self):
        user = User.objects.create(username='User', email='user@gmail.com', phone_number='+7777777777')

        url = '/homework/api/tasks/'
        data = {'teacher':user.id, 'course': 'python', 'lesson': '1 lesson', 'title': 'django tests', 'content': 'django tests'}
        response = self.client.post(url, data)

        assert response.status_code == status.HTTP_201_CREATED
        assert response.json()["teacher_id"] == data['teacher']
        assert response.json()['course'] == data['course']
        assert response.json()['lesson'] == data['lesson']
        assert response.json()['title'] == data['title']
        assert response.json()['content'] == data['content']

    @pytest.mark.django_db
    def test_put(self):
        user = User.objects.create(username='User', email='user@gmail.com', phone_number='+7777777777')
        task = HomeworkTaskModel.objects.create(teacher=user, course='java', lesson='first lesson', title="java tests", content='java tests')
        
        url = '/homework/api/tasks/'+str(task.id)+'/'
        data = {'teacher':user.id, 'course': 'python', 'lesson': '1 lesson', 'title': 'django tests', 'content': 'django tests'}
        response = self.client.put(url, json.dumps(data), content_type='application/json')
     
        assert response.status_code == status.HTTP_201_CREATED

    @pytest.mark.django_db
    def test_delete(self):
        user = User.objects.create(username='User', email='user@gmail.com', phone_number='+7777777777')
        task = HomeworkTaskModel.objects.create(teacher=user, course='java', lesson='first lesson', title="java tests", content='java tests')
        
        url = '/homework/api/tasks/'+str(task.id)+'/'
        response = self.client.delete(url)
        assert response.status_code == status.HTTP_204_NO_CONTENT


class TestHomeworkAnswerApi():

    client = Client()

    @pytest.mark.django_db
    def test_list_get(self):
        user = User.objects.create(username='User', email='user@gmail.com', phone_number='+7777777777')
        task = HomeworkTaskModel.objects.create(teacher=user, course='java', lesson='first lesson', title="java tests", content='java tests')
        answer = HomeworkAnswerModel.objects.create(student=user, task=task, content="java answer content")

        url = '/homework/api/answers/'
        response = self.client.get(url)

        assert response.status_code == status.HTTP_200_OK
        assert response.json()[0]["student"] == answer.student.id
        assert response.json()[0]['task'] == answer.task.id
        assert response.json()[0]['content'] == answer.content

    @pytest.mark.django_db
    def test_detail_get(self):
        user = User.objects.create(username='User', email='user@gmail.com', phone_number='+7777777777')
        task = HomeworkTaskModel.objects.create(teacher=user, course='java', lesson='first lesson', title="java tests", content='java tests')
        answer = HomeworkAnswerModel.objects.create(student=user, task=task, content="java answer content", files="file.docx")

        url = '/homework/api/answers/'+str(answer.id)+'/'
        response = self.client.get(url)

        assert response.status_code == status.HTTP_200_OK 

    @pytest.mark.django_db
    def test_post(self):
        user = User.objects.create(username='User', email='user@gmail.com', phone_number='+7777777777')
        task = HomeworkTaskModel.objects.create(teacher=user, course='java', lesson='first lesson', title="java tests", content='java tests')
        answer = HomeworkAnswerModel.objects.create(student=user, task=task, content="java answer content", files="file.docx")

        url = '/homework/api/answers/'
        data = {'student':user.id, 'task': task.id, 'content': 'task content 2'}
        response = self.client.post(url, data)

        assert response.status_code == status.HTTP_201_CREATED
        assert response.json()["student_id"] == data['student']
        assert response.json()['task_id'] == data['task']
        assert response.json()['content'] == data['content']
  
    @pytest.mark.django_db
    def test_put(self):
        user = User.objects.create(username='User', email='user@gmail.com', phone_number='+7777777777')
        task = HomeworkTaskModel.objects.create(teacher=user, course='java', lesson='first lesson', title="java tests", content='java tests')
        answer = HomeworkAnswerModel.objects.create(student=user, task=task, content="java answer content", files="file.docx")

        url = '/homework/api/answers/'+str(answer.id)+"/"
        data = {'student':user.id, 'task': task.id, 'content': 'task content 3'}
        response = self.client.put(url, json.dumps(data), content_type='application/json')
        
        assert response.status_code == status.HTTP_201_CREATED
        assert response.json()["content"] == data["content"]


    @pytest.mark.django_db
    def test_delete(self):
        user = User.objects.create(username='User', email='user@gmail.com', phone_number='+7777777777')
        task = HomeworkTaskModel.objects.create(teacher=user, course='java', lesson='first lesson', title="java tests", content='java tests')
        answer = HomeworkAnswerModel.objects.create(student=user, task=task, content="java answer content", files="file.docx")

        url = '/homework/api/answers/'+str(answer.id)+"/"
        response = self.client.delete(url)
        assert response.status_code == status.HTTP_204_NO_CONTENT


class TestHomeworkGradeApi():

    client = Client()

    @pytest.mark.django_db
    def test_list_get(self):
        user = User.objects.create(username='User', email='user@gmail.com', phone_number='+7777777777')
        task = HomeworkTaskModel.objects.create(teacher=user, course='java', lesson='first lesson', title="java tests", content='java tests')
        answer = HomeworkAnswerModel.objects.create(student=user, task=task, content="java answer content")
        grade = GradesForHomework.objects.create(homework=answer, comments="thats good tests", grade=95)

        url = '/homework/api/grades/'
        response = self.client.get(url)

        assert response.status_code == status.HTTP_200_OK
        assert response.json()[0]['homework'] == grade.homework.id
        assert response.json()[0]['comments'] == grade.comments
        assert response.json()[0]['grade'] == grade.grade

    @pytest.mark.django_db
    def test_detail_get(self):
        user = User.objects.create(username='User', email='user@gmail.com', phone_number='+7777777777')
        task = HomeworkTaskModel.objects.create(teacher=user, course='java', lesson='first lesson', title="java tests", content='java tests')
        answer = HomeworkAnswerModel.objects.create(student=user, task=task, content="java answer content")
        grade = GradesForHomework.objects.create(homework=answer, comments="thats good tests", grade=95)

        url = '/homework/api/grades/'+str(grade.id)+'/'
        response = self.client.get(url)

        assert response.status_code == status.HTTP_200_OK 

    @pytest.mark.django_db
    def test_post(self):
        user = User.objects.create(username='User', email='user@gmail.com', phone_number='+7777777777')
        task = HomeworkTaskModel.objects.create(teacher=user, course='java', lesson='first lesson', title="java tests", content='java tests')
        answer = HomeworkAnswerModel.objects.create(student=user, task=task, content="java answer content")
        grade = GradesForHomework.objects.create(homework=answer, comments="thats good tests", grade=95)

        url = '/homework/api/grades/'
        data = {'homework':answer.id, 'comments': 'test comment 2', 'grade': 90.5}
        response = self.client.post(url, data)

        assert response.status_code == status.HTTP_201_CREATED
        assert response.json()['homework_id'] == data['homework']
        assert response.json()['comments'] == data['comments']
        assert response.json()['grade'] == data['grade']
    
    @pytest.mark.django_db
    def test_put(self):
        user = User.objects.create(username='User', email='user@gmail.com', phone_number='+7777777777')
        task = HomeworkTaskModel.objects.create(teacher=user, course='java', lesson='first lesson', title="java tests", content='java tests')
        answer = HomeworkAnswerModel.objects.create(student=user, task=task, content="java answer content")
        grade = GradesForHomework.objects.create(homework=answer, comments="thats good tests", grade=95)

        url = '/homework/api/grades/'+str(grade.id)+'/'
        data = {'homework':answer.id, 'comments': 'test comment 2', 'grade': 90.5}
        response = self.client.put(url, json.dumps(data), content_type='application/json')

        assert response.status_code == status.HTTP_201_CREATED
        assert response.json()['comments'] == data['comments']
        assert response.json()['grade'] == data['grade']

    @pytest.mark.django_db
    def test_delete(self):
        user = User.objects.create(username='User', email='user@gmail.com', phone_number='+7777777777')
        task = HomeworkTaskModel.objects.create(teacher=user, course='java', lesson='first lesson', title="java tests", content='java tests')
        answer = HomeworkAnswerModel.objects.create(student=user, task=task, content="java answer content")
        grade = GradesForHomework.objects.create(homework=answer, comments="thats good tests", grade=95)

        url = '/homework/api/grades/'+str(grade.id)+'/'
        response = self.client.delete(url)
        assert response.status_code == status.HTTP_204_NO_CONTENT

