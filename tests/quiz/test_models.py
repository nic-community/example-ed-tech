from django.test import TestCase
# Todo Исправить иморты
import pytest
from user import models as user_models
from course import models as course_models
from quiz import models


@pytest.fixture
def test_user1():
    test_user1 = user_models.User.objects.create_user(username='testuser1', password='12345',
                                                      email="testuser1@testuser.com")
    yield test_user1
    test_user1.delete()


@pytest.fixture
def test_user2():
    test_user2 = user_models.User.objects.create_user(username='testuser2', password='12345',
                                                      email="testuser2@testuser.com")
    yield test_user2
    test_user2.delete()


@pytest.fixture
def test_langauge1():
    test_lang1 = course_models.Language.objects.create(title="eng")
    yield test_lang1
    test_lang1.delete()


@pytest.fixture
def test_lecturer():
    test_lecturer1 = course_models.Lecturer.objects.create(first_name='A', last_name='B', phone_number='+72225554432',
                                                           email='teacher@teacher.edu')
    yield test_lecturer1
    test_lecturer1.delete()


@pytest.fixture
def test_course1(test_langauge1, test_lecturer):
    course1 = course_models.Course.objects.create(title="Django Python 3", partner='IITU', topic="Python",
                                                  has_certificate=True, approximate_time_to_complete=40,
                                                  rating=4.9, ratings_number=10, language=test_langauge1,
                                                  lecturer=test_lecturer
                                                  )
    yield course1
    course1.delete()


@pytest.fixture
def test_langauge2():
    test_lang2 = course_models.Language.objects.create(title="esp")
    yield test_lang2
    test_lang2.delete()


@pytest.fixture
def test_course2(test_langauge2, test_lecturer):
    course2 = course_models.Course.objects.create(title="Java", partner='IITU', topic="Java",
                                                  has_certificate=False, approximate_time_to_complete=50,
                                                  rating=4.9, ratings_number=10, language=test_langauge2,
                                                  lecturer=test_lecturer
                                                  )
    yield course2
    course2.delete()


@pytest.fixture
def test_final_quiz1(test_user1, test_course1, test_langauge1):
    final_quiz = models.FinalQuiz.objects.create(student=test_user1, course=test_course1,
                                                 language=test_langauge1, total_mark=85.6)
    yield final_quiz
    final_quiz.delete()


@pytest.fixture
def test_final_quiz2(test_user1, test_course1, test_langauge1):
    final_quiz = models.FinalQuiz.objects.create(student=test_user2, course=test_course2, language=test_langauge2,
                                                 total_mark=89.3)
    yield final_quiz
    final_quiz.delete()


@pytest.fixture
def test_final_quiz3(test_user1, test_course1, test_langauge1):
    final_quiz = models.FinalQuiz.objects.create(student=test_user1, course=test_course2, language=test_langauge1,
                                                 total_mark=80)
    yield final_quiz
    final_quiz.delete()


@pytest.fixture
def test_final_quiz4(test_user1, test_course1, test_langauge1):
    final_quiz = models.FinalQuiz.objects.create(student=test_user2, course=test_course1, language=test_langauge2,
                                                 total_mark=98)
    yield final_quiz
    final_quiz.delete()


@pytest.fixture
def test_question1(test_final_quiz1):
    question = models.FinalQuizQuestion.objects.create(related_quiz=test_final_quiz1,
                                                       text="Write 'Hello World'",
                                                       mark=15)
    yield question
    question.delete()


@pytest.fixture
def test_answer1(test_question1):
    answer = models.FinalQuizAnswer.objects.create(related_question=test_final_quiz1,
                                                   content="print('Hello World')")
    yield answer
    answer.delete()


# ---FinalQuiz Test---
class FinalQuizModelTest():
    @pytest.mark.django_db
    def test_final_quiz_contents_name(self, test_final_quiz1):
        final_quiz = test_final_quiz1

        assert final_quiz.title == "Django Python 3"

    @pytest.mark.django_db
    def test_final_quiz_return_str(self, test_final_quiz2):
        final_quiz = test_final_quiz2

        assert str(final_quiz) == final_quiz.title

    @pytest.mark.django_db
    def test_many_final_quiz_creation(self, test_final_quiz1, test_final_quiz2, test_final_quiz3, test_final_quiz4):
        final_quiz1 = test_final_quiz1
        final_quiz2 = test_final_quiz2
        final_quiz3 = test_final_quiz3
        final_quiz4 = test_final_quiz4

        quizes_list = models.FinalQuiz.objects.all()
        quizes_list = list(quizes_list)

        assert quizes_list[0] == final_quiz1
        assert quizes_list[1] == final_quiz2
        assert quizes_list[2] == final_quiz3
        assert quizes_list[3] == final_quiz4

    @pytest.mark.django_db
    def test_mark_validity(self, test_final_quiz1):
        final_quiz1 = test_final_quiz1
        final_quiz2 = models.FinalQuiz.objects.create(student=test_user2, course=test_course2,
                                                      language=test_langauge2, total_mark=90000000)

        assert final_quiz1.total_mark <= 100
        assert final_quiz2.total_mark <= 100

    @pytest.mark.django_db
    def test_mark_correctness(self, test_final_quiz1, test_final_quiz4):
        final_quiz1 = test_final_quiz1
        final_quiz2 = test_final_quiz4

        assert final_quiz1.total_mark == 85.6
        assert final_quiz2.total_mark == 98


# ---FinalQuizQuestion Test---
class FinalQuizQuestionModelTest():
    @pytest.mark.django_db
    def test_question_text(self, test_question1):
        question = test_question1

        assert question.title == "Write 'Hello World'"

    @pytest.mark.django_db
    def test_question_return_str(self, test_question1):
        question = test_question1

        assert str(question) == "Write 'Hello World' - question"

    @pytest.mark.django_db
    def test_multiple_question_creation(self, test_question1, test_final_quiz2, test_final_quiz3):
        question1 = test_question1
        question2 = models.FinalQuizQuestion.objects.create(related_quiz=test_final_quiz1,
                                                            text="Write 'Hello World'",
                                                            mark=15)
        question3 = models.FinalQuizQuestion.objects.create(related_quiz=test_final_quiz2,
                                                            text="2 in 10th power equals to ... ",
                                                            mark=10)
        question4 = models.FinalQuizQuestion.objects.create(related_quiz=test_final_quiz3,
                                                            text="5+5 equals to ...",
                                                            mark=5)

        questions_list = models.FinalQuizQuestion.objects.all()
        questions_list = list(questions_list)

        assert questions_list[0] == question1
        assert questions_list[1] == question2
        assert questions_list[2] == question3
        assert questions_list[3] == question4

    @pytest.mark.django_db
    def test_many_to_one_relation_question_creation(self, test_question1, test_final_quiz3):
        question1 = test_question1
        question2 = models.FinalQuizQuestion.objects.create(related_quiz=test_final_quiz1,
                                                            text="5+7 equals to ...",
                                                            mark=5)
        question3 = models.FinalQuizQuestion.objects.create(related_quiz=test_final_quiz3,
                                                            text="5+5 equals to ...",
                                                            mark=5)
        question4 = models.FinalQuizQuestion.objects.create(related_quiz=test_final_quiz3,
                                                            text="15+5 equals to ...",
                                                            mark=5)

        questions_list = models.FinalQuizQuestion.objects.all()
        questions_list = list(questions_list)

        assert questions_list[0] == question1
        assert questions_list[1] == question2
        assert questions_list[2] == question3
        assert questions_list[3] == question4

    @pytest.mark.django_db
    def test_unique_question_creation(self, test_question1, test_final_quiz3):
        question1 = test_question1
        question2 = test_question1

        questions_list = models.FinalQuizQuestion.objects.all()
        questions_list = list(questions_list)

        assert questions_list[0] == question1
        assert questions_list[1] == question2

    @pytest.mark.django_db
    def test_mark_validity(self, test_question1):
        question1 = test_question1
        question2 = models.FinalQuizQuestion.objects.create(related_quiz=test_final_quiz3,
                                                            text="15+5 equals to ...",
                                                            mark=500)

        assert question1.total_mark <= 100
        assert question2.total_mark <= 100


# ---FinalQuizAnswer Test---
class FinalQuizAnswerModelTest():
    @pytest.mark.django_db
    def test_answer_text(self, test_answer1):
        answer = test_answer1

        assert answer.content == "print('Hello World')"

    @pytest.mark.django_db
    def test_answer_return_str(self, test_answer1):
        answer = test_answer1

        assert str(answer) == "print('Hello World') - answer"

    @pytest.mark.django_db
    def test_multiple_answer_creation(self, test_answer1, test_final_quiz2, test_final_quiz3, test_final_quiz4):
        answer1 = test_answer1
        answer2 = models.FinalQuizAnswer.objects.create(related_question=test_final_quiz2,
                                                        content="print('Hello World')")
        answer3 = models.FinalQuizAnswer.objects.create(related_question=test_final_quiz3,
                                                        content="print('Hello World')")
        answer4 = models.FinalQuizAnswer.objects.create(related_question=test_final_quiz4,
                                                        content="print('Hello World')")

        answers_list = models.FinalQuizAnswer.objects.all()
        answers_list = list(answers_list)

        assert answers_list[0] == answer1
        assert answers_list[1] == answer2
        assert answers_list[2] == answer3
        assert answers_list[3] == answer4

    @pytest.mark.django_db
    def test_many_answer_to_one_question_creation(self, test_answer1):
        answer1 = test_answer1
        answer2 = models.FinalQuizAnswer.objects.create(related_question=test_final_quiz4,
                                                        content="std.Out('Hello World')")
        answer3 = models.FinalQuizAnswer.objects.create(related_question=test_final_quiz4,
                                                        content="cout<< "'Hello World'"")
        answer4 = models.FinalQuizAnswer.objects.create(related_question=test_final_quiz4,
                                                        content="println('Hello World')")

        answers_list = models.FinalQuizAnswer.objects.all()
        answers_list = list(answers_list)

        assert answers_list[0] == answer1
        assert answers_list[1] == answer2
        assert answers_list[2] == answer3
        assert answers_list[3] == answer4


# ToDo: дописать модели и тесты

# ---LessonQuiz Test---
# ToDo: необходимо дописать фикстуры,так нет модели урока

class LessonQuizModelTest():
    @pytest.mark.django_db
    def test_lesson(self):
        pass


# ---LessonQuizQuestion Test---

class LessonQuizQuestionModelTest():
    @pytest.mark.django_db
    def test_lesson(self):
        pass


# ---LessonQuizAnswer Test---
class LessonQuizAnswerModelTest():
    @pytest.mark.django_db
    def test_lesson(self):
        pass
