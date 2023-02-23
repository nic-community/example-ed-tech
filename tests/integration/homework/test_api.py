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
    def test_get_list_of_tasks(self, init_objects, client):
        task = init_objects[1]

        url = '/api/v1/homework/tasks/'
        response = client.get(url)
        response_data = response.json()

        assert response.status_code == status.HTTP_200_OK
        assert response_data[0]["teacher"] == task.teacher.id
        assert response_data[0]['course'] == task.course
        assert response_data[0]['lesson'] == task.lesson
        assert response_data[0]['title'] == task.title
        assert response_data[0]['content'] == task.content

    @pytest.mark.django_db
    def test_get_list_of_tasks_form_wrong_url(self, client):
        url = '/api/v1/homework/tasks-bad-url/'
    
        response = client.get(url)
        assert response.status_code == status.HTTP_404_NOT_FOUND


    @pytest.mark.django_db
    def test_get_detail_task(self, init_objects, client):
        task = init_objects[1]
        
        url = '/api/v1/homework/tasks/'+str(task.id)+'/'
        response = client.get(url)

        assert response.status_code == status.HTTP_200_OK 

    @pytest.mark.django_db
    def test_get_detail_task_from_wrong_url(self, client):
        url = '/api/v1/homework/tasks/'+'bad-url/'
        with pytest.raises(ValueError) as e:
            response = client.get(url)
        assert str(e.value) == "Field 'id' expected a number but got 'bad-url'."

    @pytest.mark.django_db
    def test_get_detail_non_existent_task(self, client):        
        url = '/api/v1/homework/tasks/1/'
        response = client.get(url)
        response_data = response.json()

        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert response_data['detail'] == 'Not found.'

    @pytest.mark.django_db
    def test_create_task(self, init_objects, client):
        user = init_objects[0]

        url = '/api/v1/homework/tasks/'
        data = {'teacher':user.id, 'course': 'python', 'lesson': '1 lesson', 'title': 'django tests', 'content': 'django tests'}
        response = client.post(url, data)
        response_data = response.json()

        assert response.status_code == status.HTTP_201_CREATED
        assert response_data["teacher_id"] == data['teacher']
        assert response_data['course'] == data['course']
        assert response_data['lesson'] == data['lesson']
        assert response_data['title'] == data['title']
        assert response_data['content'] == data['content']

    @pytest.mark.django_db
    def test_create_task_with_empty_data(self, client):
        url = '/api/v1/homework/tasks/'
        data = {}
        response = client.post(url, data)
        response_data = response.json()

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response_data["teacher"] == ['This field is required.']
        assert response_data['course'] == ['This field is required.']
        assert response_data['lesson'] == ['This field is required.']
        assert response_data['title'] == ['This field is required.']
        assert response_data['content'] == ['This field is required.']

    @pytest.mark.django_db
    def test_update_task(self, init_objects, client):
        user, task = init_objects[0:2]

        url = '/api/v1/homework/tasks/'+str(task.id)+'/'
        data = {'teacher':user.id, 'course': 'python', 'lesson': '1 lesson', 'title': 'django tests', 'content': 'django tests'}
        response = client.put(url, json.dumps(data), content_type='application/json')
     
        assert response.status_code == status.HTTP_201_CREATED

    @pytest.mark.django_db
    def test_update_non_existent_task(self, client):   
        url = '/api/v1/homework/tasks/1/'
        data = {}
        response = client.put(url, json.dumps(data), content_type='application/json')
        response_data = response.json()

        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert response_data['detail'] == 'Not found.'

    @pytest.mark.django_db
    def test_put_method_to_another_url(self, client):
        url = '/api/v1/homework/tasks/'
        data = {}
        response = client.put(url, json.dumps(data), content_type='application/json')
        response_data = response.json()

        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED
        assert response_data['detail']== 'Method "PUT" not allowed.'

    @pytest.mark.django_db
    def test_update_task_with_empty_data(self, init_objects,client):
        task = init_objects[1]

        url = '/api/v1/homework/tasks/'+str(task.id)+'/'
        data = {}
        response = client.put(url, json.dumps(data), content_type='application/json')
        response_data = response.json()

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response_data['teacher'] == ['This field is required.']
        assert response_data['course'] == ['This field is required.']
        assert response_data['lesson'] == ['This field is required.']
        assert response_data['title'] == ['This field is required.']
        assert response_data['content'] == ['This field is required.']


    @pytest.mark.django_db
    def test_delete_task(self, init_objects, client):
        task = init_objects[1]

        url = '/api/v1/homework/tasks/'+str(task.id)+'/'
        response = client.delete(url)
        assert response.status_code == status.HTTP_204_NO_CONTENT

    @pytest.mark.django_db
    def test_delete_non_existent_task(self, client):
        url = '/api/v1/homework/tasks/1/'
        response = client.delete(url)
        response_data = response.json()

        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert response_data['detail'] == 'Not found.'

    @pytest.mark.django_db
    def test_delete_method_to_another_url(self, client):
        url = '/api/v1/homework/tasks/'
        response = client.delete(url)
        response_data = response.json()

        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED
        assert response_data['detail']== 'Method "DELETE" not allowed.'


class TestHomeworkAnswerApi():

    @pytest.mark.django_db
    def test_get_list_of_answers(self, init_objects, client):
        answer = init_objects[2]

        url = '/api/v1/homework/answers/'
        response = client.get(url)
        response_data = response.json()

        assert response.status_code == status.HTTP_200_OK
        assert response_data[0]["student"] == answer.student.id
        assert response_data[0]['task'] == answer.task.id
        assert response_data[0]['content'] == answer.content

    @pytest.mark.django_db
    def test_get_list_of_answers_form_wrong_url(self, client):
        url = '/api/v1/homework/answers-bad-url/'

        response = client.get(url)
        assert response.status_code == status.HTTP_404_NOT_FOUND

    @pytest.mark.django_db
    def test_get_detail_answer(self, init_objects, client):
        answer = init_objects[2]

        url = '/api/v1/homework/answers/'+str(answer.id)+'/'
        response = client.get(url)

        assert response.status_code == status.HTTP_200_OK 

    @pytest.mark.django_db
    def test_get_detali_answer_from_wrong_url(self, client):
        url = '/api/v1/homework/answers/'+'bad-url/'
        with pytest.raises(ValueError) as e:
            response = client.get(url)
        assert str(e.value) == "Field 'id' expected a number but got 'bad-url'."

    @pytest.mark.django_db
    def test_get_detail_non_existent_answer(self, client):
        url = '/api/v1/homework/answers/1/'
        response = client.get(url)
        response_data = response.json()

        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert response_data['detail'] == 'Not found.'

    @pytest.mark.django_db
    def test_create_answer(self, init_objects, client):
        user, task = init_objects[0:2]

        url = '/api/v1/homework/answers/'
        data = {'student':user.id, 'task': task.id, 'content': 'task content 2'}
        response = client.post(url, data)
        response_data = response.json()

        assert response.status_code == status.HTTP_201_CREATED
        assert response_data["student_id"] == data['student']
        assert response_data['task_id'] == data['task']
        assert response_data['content'] == data['content']

    @pytest.mark.django_db
    def test_create_answer_with_empty_data(self, client):
        data = {}

        url = '/api/v1/homework/answers/'
        response = client.post(url, data)
        response_data = response.json()

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response_data["student"] == ['This field is required.']
        assert response_data['task'] == ['This field is required.']
  
    @pytest.mark.django_db
    def test_update_answer(self, init_objects, client):
        user, task, answer = init_objects[0:3]
        
        url = '/api/v1/homework/answers/'+str(answer.id)+"/"
        data = {'student':user.id, 'task': task.id, 'content': 'task content 3'}
        response = client.put(url, json.dumps(data), content_type='application/json')
        response_data = response.json()

        assert response.status_code == status.HTTP_201_CREATED
        assert response_data["content"] == data["content"]

    @pytest.mark.django_db
    def test_update_non_existent_answer(self, client):
        url = '/api/v1/homework/answers/1/'
        data = {}
        response = client.put(url, json.dumps(data), content_type='application/json')
        response_data = response.json()

        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert response_data['detail'] == 'Not found.'

    @pytest.mark.django_db
    def test_put_method_to_another_url(self, client):
        url = '/api/v1/homework/answers/'
        data = {}
        response = client.put(url, json.dumps(data), content_type='application/json')
        response_data = response.json()

        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED
        assert response_data['detail']== 'Method "PUT" not allowed.'

    @pytest.mark.django_db
    def test_update_answer_with_empty_data(self, init_objects, client):
        answer = init_objects[2]

        url = '/api/v1/homework/answers/'+str(answer.id)+'/'
        data = {}
        response = client.put(url, json.dumps(data), content_type='application/json')
        response_data = response.json()
        
        assert response_data["student"] == ['This field is required.']
        assert response_data['task'] == ['This field is required.']


    @pytest.mark.django_db
    def test_delete_answer(self, init_objects, client):
        answer = init_objects[2]

        url = '/api/v1/homework/answers/'+str(answer.id)+"/"
        response = client.delete(url)
        assert response.status_code == status.HTTP_204_NO_CONTENT

    @pytest.mark.django_db
    def test_delete_non_existent_answer(self, client):
        url = '/api/v1/homework/answers/1/'
        response = client.delete(url)
        response_data = response.json()

        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert response_data['detail'] == 'Not found.'

    @pytest.mark.django_db
    def test_delete_method_to_another_url(self, client):
        url = '/api/v1/homework/answers/'
        response = client.delete(url)
        response_data =response.json()

        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED
        assert response_data['detail']== 'Method "DELETE" not allowed.'


class TestHomeworkGradeApi():

    @pytest.mark.django_db
    def test_get_list_of_grades_for_answer(self, init_objects, client):
        grade = init_objects[3]

        url = '/api/v1/homework/grades/'
        response = client.get(url)
        response_data = response.json()

        assert response.status_code == status.HTTP_200_OK
        assert response_data[0]['homework'] == grade.homework.id
        assert response_data[0]['comments'] == grade.comments
        assert response_data[0]['grade'] == grade.grade

    @pytest.mark.django_db
    def test_get_list_of_grades_from_wrong_url(self, client):
        url = '/api/v1/homework/grades-bad-url/'
        response = client.get(url)

        assert response.status_code == status.HTTP_404_NOT_FOUND

    @pytest.mark.django_db
    def test_get_detail_grade_for_answer(self, init_objects, client):
        grade = init_objects[3]

        url = '/api/v1/homework/grades/'+str(grade.id)+'/'
        response = client.get(url)

        assert response.status_code == status.HTTP_200_OK 

    @pytest.mark.django_db
    def test_get_detail_grade_from_wrong_url(self, client):
        url = '/api/v1/homework/grades/'+'bad-url/'
        with pytest.raises(ValueError) as e:
            response = client.get(url)
        assert str(e.value) == "Field 'id' expected a number but got 'bad-url'."

    @pytest.mark.django_db
    def test_get_detail_non_existent_grade(self, client):
        url = '/api/v1/homework/grades/1/'
        response = client.get(url)
        response_data = response.json()

        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert response_data['detail'] == 'Not found.'


    @pytest.mark.django_db
    def test_create_grade_for_answer(self, init_objects, client):
        answer = init_objects[2]

        url = '/api/v1/homework/grades/'
        data = {'homework':answer.id, 'comments': 'test comment 2', 'grade': 90.5}
        response = client.post(url, data)
        response_data = response.json()

        assert response.status_code == status.HTTP_201_CREATED
        assert response_data['homework_id'] == data['homework']
        assert response_data['comments'] == data['comments']
        assert response_data['grade'] == data['grade']

    @pytest.mark.django_db
    def test_create_grade_for_answer_with_empty_data(self, client):
        url = '/api/v1/homework/grades/'
        data = {}
        response = client.post(url, data)
        response_data = response.json()

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response_data["homework"] == ['This field is required.']
        assert response_data['grade'] == ['This field is required.']
    
    @pytest.mark.django_db
    def test_update_grade_for_answer(self, init_objects, client):
        answer, grade = init_objects[2:4]

        url = '/api/v1/homework/grades/'+str(grade.id)+'/'
        data = {'homework':answer.id, 'comments': 'test comment 2', 'grade': 90.5}
        response = client.put(url, json.dumps(data), content_type='application/json')

        assert response.status_code == status.HTTP_201_CREATED
        assert response.json()['comments'] == data['comments']
        assert response.json()['grade'] == data['grade']

    @pytest.mark.django_db
    def test_update_non_existent_grade_for_answer(self, client):
        url = '/api/v1/homework/grades/1/'
        data = {}
        response = client.put(url, json.dumps(data), content_type='application/json')
        response_data = response.json()

        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert response_data['detail'] == 'Not found.'

    @pytest.mark.django_db
    def test_put_method_to_another_url(self, client):
        url = '/api/v1/homework/grades/'
        data = {}
        response = client.put(url, json.dumps(data), content_type='application/json')
        response_data = response.json()

        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED
        assert response_data['detail']== 'Method "PUT" not allowed.'
    
    @pytest.mark.django_db
    def test_update_grade_for_answer_with_empty_data(self, init_objects, client):
        grade = init_objects[3]

        url = '/api/v1/homework/grades/'+str(grade.id)+'/'
        data = {}
        response = client.put(url, json.dumps(data), content_type='application/json')
        response_data = response.json()

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response_data["homework"] == ['This field is required.']
        assert response_data['grade'] == ['This field is required.']

    @pytest.mark.django_db
    def test_delete_grade_for_answer(self, init_objects, client):
        grade = init_objects[3]

        url = '/api/v1/homework/grades/'+str(grade.id)+'/'
        response = client.delete(url)
        assert response.status_code == status.HTTP_204_NO_CONTENT

    @pytest.mark.django_db
    def test_delete_non_existent_grade_for_answer(self, client):
        url = '/api/v1/homework/grades/1/'
        response = client.delete(url)
        response_data = response.json()

        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert response_data['detail'] == 'Not found.'

    @pytest.mark.django_db
    def test_delete_method_to_another_url(self, client):
        url = '/api/v1/homework/grades/'
        response = client.delete(url)
        response_data = response.json()

        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED
        assert response_data['detail']== 'Method "DELETE" not allowed.'

