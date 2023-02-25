from unittest import TestCase
import pytest
from course.models import (
    Language,
    Lecturer,
    Course
)
from user.models import User


# ALL TESTS MADE WITH 'pytest-django' LIBRARY
# ---------------------- LANGUAGE MODEL ----------------------
class LanguageModelTest:

    @pytest.mark.django_db
    def test_language_contents_name(self):
        language = Language.objects.create(title='TestLanguageTitle')

        assert language.title == 'TestLanguageTitle'

    @pytest.mark.django_db
    def test_language_return_str(self):
        language = Language.objects.create(title='TestLanguageTitle')

        assert str(language) == language.title

    @pytest.mark.django_db
    def test_language_verbose_name(self):
        language = Language.objects.create(title='TestLanguageTitle')

        verbose_name = language._meta.verbose_name
        verbose_name_plural = language._meta.verbose_name_plural

        assert verbose_name == 'Язык'
        assert verbose_name_plural == 'Языки'

    @pytest.mark.django_db
    def test_language_ordering(self):
        language0 = Language.objects.create(title='TestLanguageTitle0')
        language1 = Language.objects.create(title='TestLanguageTitle1')
        language2 = Language.objects.create(title='TestLanguageTitle2')

        languages = Language.objects.all()
        languages = list(languages)

        assert languages[0] == language0
        assert languages[1] == language1
        assert languages[2] == language2


# ---------------------- LECTURER MODEL ----------------------
class LecturerModelTest:
    @pytest.mark.django_db
    def test_lecturer_contents_name(self):
        lecturer = Lecturer.objects.create(
            first_name='TestLecturerFirstName',
            last_name='TestLecturerLastName',
            phone_number='+77083334123',
            email='test@gmail.com'
        )

        assert lecturer.first_name == 'TestLecturerFirstName'
        assert lecturer.last_name == 'TestLecturerLastName'
        assert lecturer.phone_number == '+77083334123'
        assert lecturer.email == 'test@gmail.com'

    @pytest.mark.django_db
    def test_lecturer_return_str(self):
        lecturer = Lecturer.objects.create(
            first_name='TestLecturerFirstName',
            last_name='TestLecturerLastName',
            phone_number='+77083334123',
            email='test@gmail.com'
        )

        assert str(lecturer) == f"{lecturer.last_name}/{lecturer.first_name}"

    @pytest.mark.django_db
    def test_lecturer_verbose_name(self):
        lecturer = Lecturer.objects.create(
            first_name='TestLecturerFirstName',
            last_name='TestLecturerLastName',
            phone_number='+77083334123',
            email='test@gmail.com'
        )

        verbose_name = lecturer._meta.verbose_name
        verbose_name_plural = lecturer._meta.verbose_name_plural

        assert verbose_name == 'Лектор'
        assert verbose_name_plural == 'Лекторы'

    @pytest.mark.django_db
    def test_lecturer_ordering(self):
        lecturer0 = Lecturer.objects.create(
            first_name='TestLecturerFirstName0',
            last_name='TestLecturerLastName0',
            phone_number='+77083334120',
            email='test0@gmail.com'
        )
        lecturer1 = Lecturer.objects.create(
            first_name='TestLecturerFirstName1',
            last_name='TestLecturerLastName1',
            phone_number='+77083334121',
            email='test1@gmail.com'
        )
        lecturer2 = Lecturer.objects.create(
            first_name='TestLecturerFirstName2',
            last_name='TestLecturerLastName2',
            phone_number='+77083334122',
            email='test2@gmail.com'
        )

        lecturers = Lecturer.objects.all()
        lecturers = list(lecturers)

        assert lecturers[0] == lecturer0
        assert lecturers[1] == lecturer1
        assert lecturers[2] == lecturer2


# ---------------------- COURSE MODEL ----------------------
class CourseModelTest:
    @pytest.mark.django_db
    def course_test_contents_name(self):
        language = Language.objects.create(title='TestLanguageTitle')
        lecturer = Lecturer.objects.create(
            first_name='TestLecturerFirstName',
            last_name='TestLecturerLastName',
            phone_number='+77083334123',
            email='test@gmail.com'
        )
        course = Course.objects.create(
            title='TestCourseTitle',
            partner='TestCoursePartner',
            topic='TestCourseTopic',
            has_certificate=True,
            approximate_time_to_complete=30,
            rating=4.46,
            ratings_number=6,
            language=language,
            lecturer=lecturer
        )

        assert course.title == 'TestCourseTitle'
        assert course.partner == 'TestCoursePartner'
        assert course.topic == 'TestCourseTopic'
        assert course.has_certificate is True
        assert course.approximate_time_to_complete == 30
        assert course.rating == 4.46
        assert course.ratings_number == 6
        assert course.language == language
        assert course.lecturer == lecturer

    @pytest.mark.django_db
    def course_test_return_str(self):
        language = Language.objects.create(title='TestLanguageTitle')
        lecturer = Lecturer.objects.create(
            first_name='TestLecturerFirstName',
            last_name='TestLecturerLastName',
            phone_number='+77083334123',
            email='test@gmail.com'
        )
        course = Course.objects.create(
            title='TestCourseTitle',
            partner='TestCoursePartner',
            topic='TestCourseTopic',
            has_certificate=True,
            approximate_time_to_complete=30,
            rating=4.46,
            ratings_number=6,
            language=language,
            lecturer=lecturer
        )

        assert str(course) == f"{course.title}/Partner: {course.partner}/Topic: {course.topic}"

    @pytest.mark.django_db
    def test_course_verbose_name(self):
        language = Language.objects.create(title='TestLanguageTitle')
        lecturer = Lecturer.objects.create(
            first_name='TestLecturerFirstName',
            last_name='TestLecturerLastName',
            phone_number='+77083334123',
            email='test@gmail.com'
        )
        course = Course.objects.create(
            title='TestCourseTitle',
            partner='TestCoursePartner',
            topic='TestCourseTopic',
            has_certificate=True,
            approximate_time_to_complete=30,
            rating=4.46,
            ratings_number=6,
            language=language,
            lecturer=lecturer
        )

        verbose_name = course._meta.verbose_name
        verbose_name_plural = course._meta.verbose_name_plural

        assert verbose_name == 'Курс'
        assert verbose_name_plural == 'Курсы'

    @pytest.mark.django_db
    def test_course_ordering(self):
        # LANGUAGES
        language0 = Language.objects.create(title='TestLanguageTitle0')
        language1 = Language.objects.create(title='TestLanguageTitle1')
        language2 = Language.objects.create(title='TestLanguageTitle2')

        # LECTURERS
        lecturer0 = Lecturer.objects.create(
            first_name='TestLecturerFirstName0',
            last_name='TestLecturerLastName0',
            phone_number='+77083334120',
            email='test0@gmail.com'
        )
        lecturer1 = Lecturer.objects.create(
            first_name='TestLecturerFirstName1',
            last_name='TestLecturerLastName1',
            phone_number='+77083334121',
            email='test1@gmail.com'
        )
        lecturer2 = Lecturer.objects.create(
            first_name='TestLecturerFirstName2',
            last_name='TestLecturerLastName2',
            phone_number='+77083334122',
            email='test2@gmail.com'
        )

        # COURSES
        course0 = Course.objects.create(
            title='TestCourseTitle0',
            partner='TestCoursePartner0',
            topic='TestCourseTopic0',
            has_certificate=True,
            approximate_time_to_complete=30,
            rating=4.46,
            ratings_number=6,
            language=language0,
            lecturer=lecturer0
        )
        course1 = Course.objects.create(
            title='TestCourseTitle1',
            partner='TestCoursePartner1',
            topic='TestCourseTopic1',
            has_certificate=True,
            approximate_time_to_complete=25,
            rating=4.3,
            ratings_number=7,
            language=language1,
            lecturer=lecturer1
        )
        course2 = Course.objects.create(
            title='TestCourseTitle2',
            partner='TestCoursePartner2',
            topic='TestCourseTopic2',
            has_certificate=False,
            approximate_time_to_complete=23,
            rating=4.0,
            ratings_number=10,
            language=language2,
            lecturer=lecturer2
        )

        courses = Course.objects.all()
        courses = list(courses)

        assert courses[0] == course0
        assert courses[1] == course1
        assert courses[2] == course2
