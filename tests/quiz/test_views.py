from rest_framework import status
from rest_framework.test import APIRequestFactory, APITestCase

from user import models as user_models
from course import models as course_models
from quiz import models


#  --- FinalQuiz Test Api ---
class FinalQuizApiTest(APITestCase):

    @classmethod
    def setUpTestData(cls):
        user = user_models.User.objects.create(id=1, username='test_user1',
                                               email='user@user.email.com',
                                               phone_number='+7894561234')
        language = course_models.Language.objects.create(id=1, title='TestLanguage')
        lecturer = course_models.Lecturer.objects.create(first_name='A',
                                                         last_name='B',
                                                         phone_number='+72225554432',
                                                         email='teacher@teacher.edu')

        course = course_models.Course.objects.create(title="Django Python 3",
                                                     partner='IITU',
                                                     topic="Python",
                                                     has_certificate=True,
                                                     approximate_time_to_complete=40,
                                                     rating=4.9, ratings_number=10,
                                                     language=language,
                                                     lecturer=lecturer)

        final_quiz = models.FinalQuiz.objects.create(student=user, course=course,
                                                     language=language, total_mark=85.6)

    def test_list_get(self):
        url = '/quiz/api/final-quiz/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post(self):
        url = '/quiz/api/final-quiz/'
        data = {
            'id': 1,
            'student': 1,
            'course': 1,
            'total_mark': 85.6,
            'language': 1
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_detail_get(self):
        url = '/quiz/api/final-quiz/1'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_put(self):
        url = '/quiz/api/final-quiz/1'
        data = {
            'id': 1,
            'student': 1,
            'course': 1,
            'total_mark': 99.9,
            'language': 1,
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete(self):
        url = '/quiz/api/final-quiz/1'

        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


#  --- FinalQuizQuestion Test Api ---
class FinalQuizQuestionApiTest(APITestCase):

    @classmethod
    def setUpTestData(cls):
        user = user_models.User.objects.create(id=1, username='test_user1',
                                               email='user@user.email.com',
                                               phone_number='+7894561234')
        language = course_models.Language.objects.create(id=1, title='TestLanguage')
        lecturer = course_models.Lecturer.objects.create(first_name='A',
                                                         last_name='B',
                                                         phone_number='+72225554432',
                                                         email='teacher@teacher.edu')

        course = course_models.Course.objects.create(title="Django Python 3",
                                                     partner='IITU',
                                                     topic="Python",
                                                     has_certificate=True,
                                                     approximate_time_to_complete=40,
                                                     rating=4.9, ratings_number=10,
                                                     language=language,
                                                     lecturer=lecturer)

        final_quiz = models.FinalQuiz.objects.create(student=user, course=course,
                                                     language=language, total_mark=85.6)
        final_quiz_question = models.FinalQuizQuestion.objects.create( related_quiz=final_quiz,
                                                                       text = 'Write "Hello World" in Python',
                                                                       mark=5)

    def test_list_get(self):
        url = '/quiz/api/final-quiz-question/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post(self):
        url = '/quiz/api/final-quiz-question/'
        data = {
            'id': 1,
            'related_quiz': 1,
            'text': 'Write "Hello World" in Python',
            'mark': 5
        }

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_detail_get(self):
        url = '/quiz/api/final-quiz-question/1'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_put(self):
        url = '/quiz/api/final-quiz-question/1'
        data = {
            'id': 1,
            'related_quiz': 1,
            'text': 'Write "Hello World" in Python',
            'mark': 10
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete(self):
        url = '/quiz/api/final-quiz/1'

        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


#  --- FinalQuizAnswer Test Api ---
class FinalQuizAnswerApiTest(APITestCase):

    @classmethod
    def setUpTestData(cls):
        user = user_models.User.objects.create(id=1, username='test_user1',
                                               email='user@user.email.com',
                                               phone_number='+7894561234')
        language = course_models.Language.objects.create(id=1, title='TestLanguage')
        lecturer = course_models.Lecturer.objects.create(first_name='A',
                                                         last_name='B',
                                                         phone_number='+72225554432',
                                                         email='teacher@teacher.edu')

        course = course_models.Course.objects.create(title="Django Python 3",
                                                     partner='IITU',
                                                     topic="Python",
                                                     has_certificate=True,
                                                     approximate_time_to_complete=40,
                                                     rating=4.9, ratings_number=10,
                                                     language=language,
                                                     lecturer=lecturer)

        final_quiz = models.FinalQuiz.objects.create(student=user, course=course,
                                                     language=language, total_mark=85.6)

    def test_list_get(self):
        url = '/quiz/api/final-quiz/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post(self):
        url = '/quiz/api/final-quiz/'
        data = {
            'id': 1,
            'student': 1,
            'course': 1,
            'total_mark': 85.6,
            'language': 1,
            'lecturer': 1
        }

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_detail_get(self):
        url = '/quiz/api/final-quiz/1'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_put(self):
        url = '/quiz/api/final-quiz/1'
        data = {
            'id': 1,
            'student': 1,
            'course': 1,
            'total_mark': 99.9,
            'language': 1,
            'lecturer': 1
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete(self):
        url = '/quiz/api/final-quiz/1'

        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


#  --- LessonQuiz Test Api ---

class LessonQuizApiTest(APITestCase):

    @classmethod
    def setUpTestData(cls):
        user = user_models.User.objects.create(id=1, username='test_user1',
                                               email='user@user.email.com',
                                               phone_number='+7894561234')
        language = course_models.Language.objects.create(id=1, title='TestLanguage')
        lecturer = course_models.Lecturer.objects.create(first_name='A',
                                                         last_name='B',
                                                         phone_number='+72225554432',
                                                         email='teacher@teacher.edu')

        course = course_models.Course.objects.create(title="Django Python 3",
                                                     partner='IITU',
                                                     topic="Python",
                                                     has_certificate=True,
                                                     approximate_time_to_complete=40,
                                                     rating=4.9, ratings_number=10,
                                                     language=language,
                                                     lecturer=lecturer)

        final_quiz = models.FinalQuiz.objects.create(student=user, course=course,
                                                     language=language, total_mark=85.6)

    def test_list_get(self):
        url = '/quiz/api/final-quiz/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post(self):
        url = '/quiz/api/final-quiz/'
        data = {
            'id': 1,
            'student': 1,
            'course': 1,
            'total_mark': 85.6,
            'language': 1,
            'lecturer': 1
        }

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_detail_get(self):
        url = '/quiz/api/final-quiz/1'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_put(self):
        url = '/quiz/api/final-quiz/1'
        data = {
            'id': 1,
            'student': 1,
            'course': 1,
            'total_mark': 99.9,
            'language': 1,
            'lecturer': 1
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete(self):
        url = '/quiz/api/final-quiz/1'

        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


#  --- LessonQuizQuestion Test Api ---
class LessonQuizQuestionApiTest(APITestCase):

    @classmethod
    def setUpTestData(cls):
        user = user_models.User.objects.create(id=1, username='test_user1',
                                               email='user@user.email.com',
                                               phone_number='+7894561234')
        language = course_models.Language.objects.create(id=1, title='TestLanguage')
        lecturer = course_models.Lecturer.objects.create(first_name='A',
                                                         last_name='B',
                                                         phone_number='+72225554432',
                                                         email='teacher@teacher.edu')

        course = course_models.Course.objects.create(title="Django Python 3",
                                                     partner='IITU',
                                                     topic="Python",
                                                     has_certificate=True,
                                                     approximate_time_to_complete=40,
                                                     rating=4.9, ratings_number=10,
                                                     language=language,
                                                     lecturer=lecturer)

        final_quiz = models.FinalQuiz.objects.create(student=user, course=course,
                                                     language=language, total_mark=85.6)

    def test_list_get(self):
        url = '/quiz/api/final-quiz/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post(self):
        url = '/quiz/api/final-quiz/'
        data = {
            'id': 1,
            'student': 1,
            'course': 1,
            'total_mark': 85.6,
            'language': 1,
            'lecturer': 1
        }

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_detail_get(self):
        url = '/quiz/api/final-quiz/1'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_put(self):
        url = '/quiz/api/final-quiz/1'
        data = {
            'id': 1,
            'student': 1,
            'course': 1,
            'total_mark': 99.9,
            'language': 1,
            'lecturer': 1
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete(self):
        url = '/quiz/api/final-quiz/1'

        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


#  --- LessonQuizAnswer Test Api ---
class LessonQuizAnswerApiTest(APITestCase):

    @classmethod
    def setUpTestData(cls):
        user = user_models.User.objects.create(id=1, username='test_user1',
                                               email='user@user.email.com',
                                               phone_number='+7894561234')
        language = course_models.Language.objects.create(id=1, title='TestLanguage')
        lecturer = course_models.Lecturer.objects.create(first_name='A',
                                                         last_name='B',
                                                         phone_number='+72225554432',
                                                         email='teacher@teacher.edu')

        course = course_models.Course.objects.create(title="Django Python 3",
                                                     partner='IITU',
                                                     topic="Python",
                                                     has_certificate=True,
                                                     approximate_time_to_complete=40,
                                                     rating=4.9, ratings_number=10,
                                                     language=language,
                                                     lecturer=lecturer)

        final_quiz = models.FinalQuiz.objects.create(student=user, course=course,
                                                     language=language, total_mark=85.6)

    def test_list_get(self):
        url = '/quiz/api/final-quiz/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post(self):
        url = '/quiz/api/final-quiz/'
        data = {
            'id': 1,
            'student': 1,
            'course': 1,
            'total_mark': 85.6,
            'language': 1,
            'lecturer': 1
        }

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_detail_get(self):
        url = '/quiz/api/final-quiz/1'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_put(self):
        url = '/quiz/api/final-quiz/1'
        data = {
            'id': 1,
            'student': 1,
            'course': 1,
            'total_mark': 99.9,
            'language': 1,
            'lecturer': 1
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete(self):
        url = '/quiz/api/final-quiz/1'

        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
