from rest_framework.test import APITestCase
from rest_framework import status

from user.models import User
from ..models import *


class HomeworkTaskApiTestCase(APITestCase):

    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(id=1, username='User', email='user@gmail.com', phone_number='+7777777777')
        HomeworkTaskModel.objects.create(id=1, teacher=user, course='java', lesson='first lesson', title="java tests", content='java tests')

    def test_list_get(self):
        url = '/homework/api/tasks/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_detail_get(self):
        url = '/homework/api/tasks/1/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post(self):
        url = '/homework/api/tasks/'
        data = {'id': 2,'teacher':1, 'course': 'python', 'lesson': '1 lesson', 'title': 'django tests', 'content': 'django tests'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_put(self):
        url = '/homework/api/tasks/1/'
        data = {'teacher':1, 'course': 'C++', 'lesson': '1 lesson', 'title': 'c++ tests', 'content': 'C++ tests'}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete(self):
        url = '/homework/api/tasks/1/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class HomeworkAnswerApiTestCase(APITestCase):

    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(id=1, username='User', email='user@gmail.com', phone_number='+7777777777')
        task = HomeworkTaskModel.objects.create(id=1, teacher=user, course='java', lesson='first lesson', title="java tests", content='java tests')
        HomeworkAnswerModel.objects.create(id=1, student=user, task=task, content='task content')

    def test_list_get(self):
        url = '/homework/api/answers/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_detail_get(self):
        url = '/homework/api/answers/1/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post(self):
        url = '/homework/api/answers/'
        data = {'id': 2, 'student':1, 'task': 1, 'content': 'task content 2'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_put(self):
        url = '/homework/api/answers/1/'
        data = {'student':1, 'task': 1, 'content': 'task content 3'}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete(self):
        url = '/homework/api/answers/1/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    
class HomeworkGradeApiTestCase(APITestCase):

    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(id=1, username='User', email='user@gmail.com', phone_number='+7777777777')
        task = HomeworkTaskModel.objects.create(id=1, teacher=user, course='java', lesson='first lesson', title="java tests", content='java tests')
        answer = HomeworkAnswerModel.objects.create(id=1, student=user, task=task, content='task content')
        GradesForHomework.objects.create(id=1, homework=answer, comments="test comment", grade="100")

    def test_list_get(self):
        url = '/homework/api/grades/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_detail_get(self):
        url = '/homework/api/grades/1/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post(self):
        url = '/homework/api/grades/'
        data = {'id': 2, 'homework':1, 'comments': 'test comment 2', 'grade': '90.5'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_put(self):
        url = '/homework/api/grades/1/'
        data = {'homework':1, 'comments': 'test comment 3',  'grade': '90'}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete(self):
        url = '/homework/api/grades/1/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)