import pytest

from django.core.exceptions import ValidationError

from homework.models import *

# class LanguageModelTest():
#     @pytest.mark.django_db
#     def test_language_title(self):
#         language = Language.objects.create(title="TestLanguage")
#         assert language.title == "TestLanguage"

#     @pytest.mark.django_db
#     def test_language_title_max_length(self):
#         language = Language.objects.create(title="English" * 20)
#         assert len(language.title) <= 100


class TestHomeworkTaskModel:

    @pytest.mark.django_db
    def test_homework_task_contents_name(self):
        user = User.objects.create(username='User', email='user@gmail.com', phone_number='+7777777777')
        task = HomeworkTaskModel.objects.create(teacher=user, course='java', lesson='first lesson', title="java tests", content='java tests')
        
        assert task.teacher == user
        assert task.course == "java"
        assert task.lesson == "first lesson"
        assert task.title == "java tests"
        assert task.content == "java tests"

    @pytest.mark.django_db
    def test_homework_task_course_max_length(self):
        user = User.objects.create(username='User', email='user@gmail.com', phone_number='+7777777777')
        task = HomeworkTaskModel.objects.create(teacher=user, course='java', lesson='first lesson', title="java tests", content='java tests')
        max_length = task._meta.get_field('course').max_length
        
        assert max_length == 150

    @pytest.mark.django_db
    def test_homework_task_lesson_max_length(self):
        user = User.objects.create(username='User', email='user@gmail.com', phone_number='+7777777777')
        task = HomeworkTaskModel.objects.create(teacher=user, course='java', lesson='first lesson', title="java tests", content='java tests')
        max_length = task._meta.get_field('lesson').max_length
        
        assert max_length == 150

    @pytest.mark.django_db
    def test_homework_task_title_max_length(self):
        user = User.objects.create(username='User', email='user@gmail.com', phone_number='+7777777777')
        task = HomeworkTaskModel.objects.create(teacher=user, course='java', lesson='first lesson', title="java tests", content='java tests')
        max_length = task._meta.get_field('title').max_length
        
        assert max_length == 255

    @pytest.mark.django_db
    def test_homework_task_return_str(self):
        user = User.objects.create(username='User', email='user@gmail.com', phone_number='+7777777777')
        task = HomeworkTaskModel.objects.create(teacher=user, course='java', lesson='first lesson', title="java tests", content='java tests')
        
        assert str(task) == "java tests"
        
    @pytest.mark.django_db
    def test_homework_task_verbose_name(self):
        user = User.objects.create(username='User', email='user@gmail.com', phone_number='+7777777777')
        task = HomeworkTaskModel.objects.create(teacher=user, course='java', lesson='first lesson', title="java tests", content='java tests')
        
        verbose_name = task._meta.verbose_name
        verbose_name_plural = task._meta.verbose_name_plural
        
        assert verbose_name == "Домашнее задание"
        assert verbose_name_plural == "Домашние задания"

    @pytest.mark.django_db
    def test_homework_task_ordering(self):
        user = User.objects.create(username='User', email='user@gmail.com', phone_number='+7777777777')
        
        task1 = HomeworkTaskModel.objects.create(teacher=user, course='java', lesson='first lesson', title="java tests", content='java tests')
        task2 = HomeworkTaskModel.objects.create(teacher=user, course='python', lesson='second lesson', title="python tests", content='python tests')
        task3 = HomeworkTaskModel.objects.create(teacher=user, course='java', lesson='third lesson', title="java tests2", content='java tests2')
        tasks = HomeworkTaskModel.objects.all()
        
        assert list(tasks)[0] == task1
        assert list(tasks)[1] == task2
        assert list(tasks)[2] == task3


class TestHomeworkAnswerModel:

    @pytest.mark.django_db
    def test_homework_answer_contents_name(self):
        user = User.objects.create(username='User', email='user@gmail.com', phone_number='+7777777777')
        task = HomeworkTaskModel.objects.create(teacher=user, course='java', lesson='first lesson', title="java tests", content='java tests')
        answer = HomeworkAnswerModel.objects.create(student=user, task=task, content="java answer content", files="file.docx")
    
        assert answer.student == user
        assert answer.task == task
        assert answer.content == "java answer content"
        assert answer.files == "file.docx"

    @pytest.mark.django_db
    def test_homework_answer_return_str(self):
        user = User.objects.create(username='User', email='user@gmail.com', phone_number='+7777777777')
        task = HomeworkTaskModel.objects.create(teacher=user, course='java', lesson='first lesson', title="java tests", content='java tests')
        answer = HomeworkAnswerModel.objects.create(student=user, task=task, content="java answer content", files="file.docx")
    
        assert str(answer) == '{0}/{1}'.format(answer.task, answer.student)

    @pytest.mark.django_db
    def test_homework_answer_verbose_name(self):
        user = User.objects.create(username='User', email='user@gmail.com', phone_number='+7777777777')
        task = HomeworkTaskModel.objects.create(teacher=user, course='java', lesson='first lesson', title="java tests", content='java tests')
        answer = HomeworkAnswerModel.objects.create(student=user, task=task, content="java answer content", files="file.docx")
    
        verbose_name = answer._meta.verbose_name
        verbose_name_plural = answer._meta.verbose_name_plural

        assert verbose_name == "Домашняя работа"
        assert verbose_name_plural == "Домашние работы"

    @pytest.mark.django_db
    def test_homework_answer_ordering(self):
        user = User.objects.create(username='User', email='user@gmail.com', phone_number='+7777777777')
        task = HomeworkTaskModel.objects.create(teacher=user, course='java', lesson='first lesson', title="java tests", content='java tests')
        
        answer1 = HomeworkAnswerModel.objects.create(student=user, task=task, content="java answer content 1", files="file1.docx")
        answer2 = HomeworkAnswerModel.objects.create(student=user, task=task, content="java answer content 2", files="file2.docx")
        answer3 = HomeworkAnswerModel.objects.create(student=user, task=task, content="java answer content 3", files="file3.docx")
        answers = HomeworkAnswerModel.objects.all()

        assert list(answers)[0] == answer1
        assert list(answers)[1] == answer2
        assert list(answers)[2] == answer3


class TestGradesForHomeworkModel:

    @pytest.mark.django_db
    def test_homework_grade_fields_name(self):
        user = User.objects.create(username='User', email='user@gmail.com', phone_number='+7777777777')
        task = HomeworkTaskModel.objects.create(teacher=user, course='java', lesson='first lesson', title="java tests", content='java tests')
        answer = HomeworkAnswerModel.objects.create(student=user, task=task, content="java answer content", files="file.docx")
        grade = GradesForHomework(homework=answer, comments="thats good tests", grade=95)

        assert grade.homework == answer
        assert grade.comments == "thats good tests"
        assert grade.grade == 95

    @pytest.mark.django_db
    def test_homework_grade_return_str(self):
        user = User.objects.create(username='User', email='user@gmail.com', phone_number='+7777777777')
        task = HomeworkTaskModel.objects.create(teacher=user, course='java', lesson='first lesson', title="java tests", content='java tests')
        answer = HomeworkAnswerModel.objects.create(student=user, task=task, content="java answer content", files="file.docx")
        grade = GradesForHomework(homework=answer, comments="thats good tests", grade=95)

        assert str(grade) == 'Оценка за "{}"'.format(grade.homework)

    @pytest.mark.django_db
    def test_homework_grade_verbose_name(self):
        user = User.objects.create(username='User', email='user@gmail.com', phone_number='+7777777777')
        task = HomeworkTaskModel.objects.create(teacher=user, course='java', lesson='first lesson', title="java tests", content='java tests')
        answer = HomeworkAnswerModel.objects.create(student=user, task=task, content="java answer content", files="file.docx")
        grade = GradesForHomework(homework=answer, comments="thats good tests", grade=95)

        verbose_name = grade._meta.verbose_name
        verbose_name_plural = grade._meta.verbose_name_plural

        assert verbose_name == "Оценка за дз"
        assert verbose_name_plural == "Оценки за дз"