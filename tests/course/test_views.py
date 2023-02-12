from rest_framework import status

from course.views import *
from rest_framework.test import APIRequestFactory, APITestCase
from user import *
from user.models import User
from course.models import *


# ---------------------- COURSE API ----------------------
class CourseApiTest(APITestCase):

    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(id=1, username='User', email='user@gmail.com', phone_number='+7777777777')
        language = Language.objects.create(id=1, title='TestLanguage')
        lecturer = Lecturer.objects.create(
            id=1,
            first_name='TestName',
            last_name='TestLastName'
        )
        course = Course.objects.create(
            id=1,
            title='TestCourse',
            partner='TestPartner',
            topic='TestTopic',
            has_certificate=True,
            approximate_time_to_complete=30,
            rating=4.34,
            ratings_number=156,
            language=language,
            lecturer=lecturer
        )

    def test_list_get(self):
        url = '/course/api/courses/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_detail_get(self):
        url = '/course/api/courses/1/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post(self):
        url = '/course/api/courses/'
        data = {
            'id': 2,
            'title': 'TestCourse',
            'partner': 'TestPartner',
            'topic': 'TestTopic',
            'has_certificate': 'True',
            'approximate_time_to_complete': 30,
            'rating': 4.34,
            'ratings_number': 156,
            'language': 1,
            'lecturer': 1
        }

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_put(self):
        url = '/course/api/courses/1/'
        data = {
            'title': 'TestCourse',
            'partner': 'TestPartner',
            'topic': 'TestTopic',
            'has_certificate': 'True',
            'approximate_time_to_complete': 30,
            'rating': 4.34,
            'ratings_number': 156,
            'language': 1,
            'lecturer': 1
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete(self):
        url = '/course/api/courses/1/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


# ---------------------- LANGUAGE API ----------------------
class LanguageApiTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(id=1, username='User', email='user@gmail.com', phone_number='+7777777777')
        language = Language.objects.create(
            id=1,
            title='TestLanguage'
        )

    def test_list_get(self):
        url = '/course/api/languages/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_detail_get(self):
        url = '/course/api/languages/1/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post(self):
        url = '/course/api/languages/'
        data = {
            'id': 2,
            'title': 'TestLanguage',
        }

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_put(self):
        url = '/course/api/languages/1/'
        data = {
            'title': 'TestLanguage'
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete(self):
        url = '/course/api/languages/1/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


# ---------------------- LECTURER API ----------------------
class LecturerApiTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(id=1, username='User', email='user@gmail.com', phone_number='+7777777777')
        lecturer = Lecturer.objects.create(id=1, first_name='TestName', last_name='TestLastName')

    def test_list_get(self):
        url = '/course/api/lecturers/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_detail_get(self):
        url = '/course/api/lecturers/1/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post(self):
        url = '/course/api/lecturers/'
        data = {
            'id': 2,
            'first_name': 'TestName',
            'last_name': 'TestLastName'
        }

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_put(self):
        url = '/course/api/lecturers/1/'
        data = {
            'first_name': 'TestName',
            'last_name': 'TestLastName'
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete(self):
        url = '/course/api/lecturers/1/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
