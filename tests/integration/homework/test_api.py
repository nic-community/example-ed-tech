import pytest
import json

from rest_framework import status
from django.test import Client

from user.models import User
from homework.models import *


@pytest.fixture
def init_objects():
    user = User.objects.create(username='User', email='user@gmail.com', phone_number='+7777777777')
    task = HomeworkTaskModel.objects.create(teacher=user, course='java', lesson='first lesson', title="java tests", content='java tests')
    answer = HomeworkAnswerModel.objects.create(student=user, task=task, content="java answer content")
    grade = GradesForHomework.objects.create(homework=answer, comments="thats good tests", grade=95)

    return user, task, answer, grade


@pytest.fixture
def client():
    return Client()

class TestHomeworkTaskApi():
    
    @pytest.mark.django_db
    def test_list_get(self, init_objects, client):
        task = init_objects[1]

        url = '/api/v1/homework/tasks/'
        response = client.get(url)

        assert response.status_code == status.HTTP_200_OK
        assert response.json()[0]["teacher"] == task.teacher.id
        assert response.json()[0]['course'] == task.course
        assert response.json()[0]['lesson'] == task.lesson
        assert response.json()[0]['title'] == task.title
        assert response.json()[0]['content'] == task.content

    @pytest.mark.django_db
    def test_detail_get(self, init_objects, client):
        task = init_objects[1]
        
        url = '/api/v1/homework/tasks/'+str(task.id)+'/'
        response = client.get(url)

        assert response.status_code == status.HTTP_200_OK 

    @pytest.mark.django_db
    def test_post(self, init_objects, client):
        user = init_objects[0]

        url = '/api/v1/homework/tasks/'
        data = {'teacher':user.id, 'course': 'python', 'lesson': '1 lesson', 'title': 'django tests', 'content': 'django tests'}
        response = client.post(url, data)

        assert response.status_code == status.HTTP_201_CREATED
        assert response.json()["teacher_id"] == data['teacher']
        assert response.json()['course'] == data['course']
        assert response.json()['lesson'] == data['lesson']
        assert response.json()['title'] == data['title']
        assert response.json()['content'] == data['content']

    @pytest.mark.django_db
    def test_put(self, init_objects, client):
        user, task = init_objects[0:2]

        url = '/api/v1/homework/tasks/'+str(task.id)+'/'
        data = {'teacher':user.id, 'course': 'python', 'lesson': '1 lesson', 'title': 'django tests', 'content': 'django tests'}
        response = client.put(url, json.dumps(data), content_type='application/json')
     
        assert response.status_code == status.HTTP_201_CREATED

    @pytest.mark.django_db
    def test_delete(self, init_objects, client):
        task = init_objects[1]

        url = '/api/v1/homework/tasks/'+str(task.id)+'/'
        response = client.delete(url)
        assert response.status_code == status.HTTP_204_NO_CONTENT


class TestHomeworkAnswerApi():

    @pytest.mark.django_db
    def test_list_get(self, init_objects, client):
        answer = init_objects[2]

        url = '/api/v1/homework/answers/'
        response = client.get(url)

        assert response.status_code == status.HTTP_200_OK
        assert response.json()[0]["student"] == answer.student.id
        assert response.json()[0]['task'] == answer.task.id
        assert response.json()[0]['content'] == answer.content

    @pytest.mark.django_db
    def test_detail_get(self, init_objects, client):
        answer = init_objects[2]

        url = '/api/v1/homework/answers/'+str(answer.id)+'/'
        response = client.get(url)

        assert response.status_code == status.HTTP_200_OK 

    @pytest.mark.django_db
    def test_post(self, init_objects, client):
        user, task = init_objects[0:2]

        url = '/api/v1/homework/answers/'
        data = {'student':user.id, 'task': task.id, 'content': 'task content 2'}
        response = client.post(url, data)

        assert response.status_code == status.HTTP_201_CREATED
        assert response.json()["student_id"] == data['student']
        assert response.json()['task_id'] == data['task']
        assert response.json()['content'] == data['content']
  
    @pytest.mark.django_db
    def test_put(self, init_objects, client):
        user, task, answer = init_objects[0:3]
        
        url = '/api/v1/homework/answers/'+str(answer.id)+"/"
        data = {'student':user.id, 'task': task.id, 'content': 'task content 3'}
        response = client.put(url, json.dumps(data), content_type='application/json')
        
        assert response.status_code == status.HTTP_201_CREATED
        assert response.json()["content"] == data["content"]


    @pytest.mark.django_db
    def test_delete(self, init_objects, client):
        answer = init_objects[2]

        url = '/api/v1/homework/answers/'+str(answer.id)+"/"
        response = client.delete(url)
        assert response.status_code == status.HTTP_204_NO_CONTENT


class TestHomeworkGradeApi():

    @pytest.mark.django_db
    def test_list_get(self, init_objects, client):
        grade = init_objects[3]

        url = '/api/v1/homework/grades/'
        response = client.get(url)

        assert response.status_code == status.HTTP_200_OK
        assert response.json()[0]['homework'] == grade.homework.id
        assert response.json()[0]['comments'] == grade.comments
        assert response.json()[0]['grade'] == grade.grade

    @pytest.mark.django_db
    def test_detail_get(self, init_objects, client):
        grade = init_objects[3]

        url = '/api/v1/homework/grades/'+str(grade.id)+'/'
        response = client.get(url)

        assert response.status_code == status.HTTP_200_OK 

    @pytest.mark.django_db
    def test_post(self, init_objects, client):
        answer = init_objects[2]

        url = '/api/v1/homework/grades/'
        data = {'homework':answer.id, 'comments': 'test comment 2', 'grade': 90.5}
        response = client.post(url, data)

        assert response.status_code == status.HTTP_201_CREATED
        assert response.json()['homework_id'] == data['homework']
        assert response.json()['comments'] == data['comments']
        assert response.json()['grade'] == data['grade']
    
    @pytest.mark.django_db
    def test_put(self, init_objects, client):
        answer, grade = init_objects[2:4]

        url = '/api/v1/homework/grades/'+str(grade.id)+'/'
        data = {'homework':answer.id, 'comments': 'test comment 2', 'grade': 90.5}
        response = client.put(url, json.dumps(data), content_type='application/json')

        assert response.status_code == status.HTTP_201_CREATED
        assert response.json()['comments'] == data['comments']
        assert response.json()['grade'] == data['grade']

    @pytest.mark.django_db
    def test_delete(self, init_objects, client):
        grade = init_objects[3]

        url = '/api/v1/homework/grades/'+str(grade.id)+'/'
        response = client.delete(url)
        assert response.status_code == status.HTTP_204_NO_CONTENT

