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

        # bad scenarios
        url = '/api/v1/homework/tasks-bad-url/'
        response = client.get(url)
        assert response.status_code == status.HTTP_404_NOT_FOUND


    @pytest.mark.django_db
    def test_detail_get(self, init_objects, client):
        task = init_objects[1]
        
        url = '/api/v1/homework/tasks/'+str(task.id)+'/'
        response = client.get(url)

        assert response.status_code == status.HTTP_200_OK 

        # bad scenarios
        url = '/api/v1/homework/tasks/'+'bad-url/'
        with pytest.raises(ValueError) as e:
            response = client.get(url)
        assert str(e.value) == "Field 'id' expected a number but got 'bad-url'."

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

        # bad scenarios
        data = {}
        response = client.post(url, data)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.json()["teacher"] == ['This field is required.']
        assert response.json()['course'] == ['This field is required.']
        assert response.json()['lesson'] == ['This field is required.']
        assert response.json()['title'] == ['This field is required.']
        assert response.json()['content'] == ['This field is required.']

    @pytest.mark.django_db
    def test_put(self, init_objects, client):
        user, task = init_objects[0:2]

        url = '/api/v1/homework/tasks/'+str(task.id)+'/'
        data = {'teacher':user.id, 'course': 'python', 'lesson': '1 lesson', 'title': 'django tests', 'content': 'django tests'}
        response = client.put(url, json.dumps(data), content_type='application/json')
     
        assert response.status_code == status.HTTP_201_CREATED

        # bad scenarios    
        url = '/api/v1/homework/tasks/'+str(task.id+1)+'/'
        data = {}
        response = client.put(url, json.dumps(data), content_type='application/json')
        assert response.status_code == status.HTTP_404_NOT_FOUND

        url = '/api/v1/homework/tasks/'
        data = {}
        response = client.put(url, json.dumps(data), content_type='application/json')
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

        url = '/api/v1/homework/tasks/'+str(task.id)+'/'
        data = {}
        response = client.put(url, json.dumps(data), content_type='application/json')
     
        assert response.status_code == status.HTTP_400_BAD_REQUEST


    @pytest.mark.django_db
    def test_delete(self, init_objects, client):
        task = init_objects[1]

        url = '/api/v1/homework/tasks/'+str(task.id)+'/'
        response = client.delete(url)
        assert response.status_code == status.HTTP_204_NO_CONTENT

        # bad scenarios
        url = '/api/v1/homework/tasks/'+str(task.id)+'/'
        response = client.delete(url)
        assert response.status_code == status.HTTP_404_NOT_FOUND

        url = '/api/v1/homework/tasks/'
        response = client.delete(url)
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED


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

        # bad scenarios
        url = '/api/v1/homework/answers-bad-url/'
        response = client.get(url)
        assert response.status_code == status.HTTP_404_NOT_FOUND

    @pytest.mark.django_db
    def test_detail_get(self, init_objects, client):
        answer = init_objects[2]

        url = '/api/v1/homework/answers/'+str(answer.id)+'/'
        response = client.get(url)

        assert response.status_code == status.HTTP_200_OK 

        # bad scenarios
        url = '/api/v1/homework/answers/'+'bad-url/'
        with pytest.raises(ValueError) as e:
            response = client.get(url)
        assert str(e.value) == "Field 'id' expected a number but got 'bad-url'."


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

        # bad scenarios
        data = {}
        response = client.post(url, data)
        print(response.json())
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.json()["student"] == ['This field is required.']
        assert response.json()['task'] == ['This field is required.']
  
    @pytest.mark.django_db
    def test_put(self, init_objects, client):
        user, task, answer = init_objects[0:3]
        
        url = '/api/v1/homework/answers/'+str(answer.id)+"/"
        data = {'student':user.id, 'task': task.id, 'content': 'task content 3'}
        response = client.put(url, json.dumps(data), content_type='application/json')
        
        assert response.status_code == status.HTTP_201_CREATED
        assert response.json()["content"] == data["content"]

        # bad scenarios    
        url = '/api/v1/homework/answers/'+str(answer.id+1)+'/'
        data = {}
        response = client.put(url, json.dumps(data), content_type='application/json')
        assert response.status_code == status.HTTP_404_NOT_FOUND

        url = '/api/v1/homework/answers/'
        data = {}
        response = client.put(url, json.dumps(data), content_type='application/json')
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

        url = '/api/v1/homework/answers/'+str(answer.id)+'/'
        data = {}
        response = client.put(url, json.dumps(data), content_type='application/json')
     
        assert response.status_code == status.HTTP_400_BAD_REQUEST


    @pytest.mark.django_db
    def test_delete(self, init_objects, client):
        answer = init_objects[2]

        url = '/api/v1/homework/answers/'+str(answer.id)+"/"
        response = client.delete(url)
        assert response.status_code == status.HTTP_204_NO_CONTENT

        # bad scenarios
        url = '/api/v1/homework/answers/'+str(answer.id)+'/'
        response = client.delete(url)
        assert response.status_code == status.HTTP_404_NOT_FOUND

        url = '/api/v1/homework/answers/'
        response = client.delete(url)
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED



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

        # bad scenarios
        url = '/api/v1/homework/grades-bad-url/'
        response = client.get(url)
        assert response.status_code == status.HTTP_404_NOT_FOUND

    @pytest.mark.django_db
    def test_detail_get(self, init_objects, client):
        grade = init_objects[3]

        url = '/api/v1/homework/grades/'+str(grade.id)+'/'
        response = client.get(url)

        assert response.status_code == status.HTTP_200_OK 

        # bad scenarios
        url = '/api/v1/homework/grades/'+'bad-url/'
        with pytest.raises(ValueError) as e:
            response = client.get(url)
        assert str(e.value) == "Field 'id' expected a number but got 'bad-url'."


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

        # bad scenarios
        data = {}
        response = client.post(url, data)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.json()["homework"] == ['This field is required.']
        assert response.json()['grade'] == ['This field is required.']
    
    @pytest.mark.django_db
    def test_put(self, init_objects, client):
        answer, grade = init_objects[2:4]

        url = '/api/v1/homework/grades/'+str(grade.id)+'/'
        data = {'homework':answer.id, 'comments': 'test comment 2', 'grade': 90.5}
        response = client.put(url, json.dumps(data), content_type='application/json')

        assert response.status_code == status.HTTP_201_CREATED
        assert response.json()['comments'] == data['comments']
        assert response.json()['grade'] == data['grade']

        # bad scenarios    
        url = '/api/v1/homework/grades/'+str(grade.id+1)+'/'
        data = {}
        response = client.put(url, json.dumps(data), content_type='application/json')
        assert response.status_code == status.HTTP_404_NOT_FOUND

        url = '/api/v1/homework/grades/'
        data = {}
        response = client.put(url, json.dumps(data), content_type='application/json')
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

        url = '/api/v1/homework/grades/'+str(grade.id)+'/'
        data = {}
        response = client.put(url, json.dumps(data), content_type='application/json')
     
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    @pytest.mark.django_db
    def test_delete(self, init_objects, client):
        grade = init_objects[3]

        url = '/api/v1/homework/grades/'+str(grade.id)+'/'
        response = client.delete(url)
        assert response.status_code == status.HTTP_204_NO_CONTENT

        # bad scenarios
        url = '/api/v1/homework/grades/'+str(grade.id)+'/'
        response = client.delete(url)
        assert response.status_code == status.HTTP_404_NOT_FOUND

        url = '/api/v1/homework/grades/'
        response = client.delete(url)
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

