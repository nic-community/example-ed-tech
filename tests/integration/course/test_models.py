import pytest

from django.test import TestCase
from course.models import *

# ---------------------- LANGUAGE MODEL ----------------------
class LanguageModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        language = Language.objects.create(title='TestTitle')

    # title
    @pytest.mark.django_db
    def test_title_label(self):
        language = Language.objects.get(id=1)
        field_label = language._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'title')

    @pytest.mark.django_db
    def test_title_max_length(self):
        language = Language.objects.get(id=1)
        max_length = language._meta.get_field('title').max_length
        self.assertEquals(max_length, 100)

    # str method
    @pytest.mark.django_db
    def test_language_str_method(self):
        language = Language.objects.get(id=1)
        self.assertEquals(language.__str__(), 'TestTitle')


# ---------------------- LECTURER MODEL ----------------------
class LecturerModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        lecturer = Lecturer.objects.create(first_name='TestName', last_name='TestLastName')

    # first_name
    def test_first_name_label(self):
        lecturer = Lecturer.objects.get(id=1)
        field_label = lecturer._meta.get_field('first_name').verbose_name
        self.assertEquals(field_label, 'first name')

    def test_first_name_max_length(self):
        lecturer = Lecturer.objects.get(id=1)
        max_length = lecturer._meta.get_field('first_name').max_length
        self.assertEquals(max_length, 50)

    # last_name
    def test_last_name_label(self):
        lecturer = Lecturer.objects.get(id=1)
        field_label = lecturer._meta.get_field('last_name').verbose_name
        self.assertEquals(field_label, 'last name')

    def test_last_name_max_length(self):
        lecturer = Lecturer.objects.get(id=1)
        max_length = lecturer._meta.get_field('last_name').max_length
        self.assertEquals(max_length, 50)

    # str method
    def test_lecturer_str_method(self):
        lecturer = Lecturer.objects.get(id=1)
        self.assertEquals(lecturer.__str__(), 'Full name: TestLastName TestName')


# ---------------------- COURSE MODEL ----------------------
class CourseModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
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

    # title
    def test_title_label(self):
        course = Course.objects.get(id=1)
        field_label = course._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'title')

    # partner
    def test_partner_label(self):
        course = Course.objects.get(id=1)
        field_label = course._meta.get_field('partner').verbose_name
        self.assertEquals(field_label, 'partner')

    def test_partner_max_length(self):
        course = Course.objects.get(id=1)
        max_length = course._meta.get_field('partner').max_length
        self.assertEquals(max_length, 200)

    # topic
    def test_topic_label(self):
        course = Course.objects.get(id=1)
        field_label = course._meta.get_field('topic').verbose_name
        self.assertEquals(field_label, 'topic')

    def test_topic_max_length(self):
        course = Course.objects.get(id=1)
        max_length = course._meta.get_field('topic').max_length
        self.assertEquals(max_length, 100)

    # has_certificate
    def test_has_certificate_label(self):
        course = Course.objects.get(id=1)
        field_label = course._meta.get_field('has_certificate').verbose_name
        self.assertEquals(field_label, 'has certificate')

    # approximate_time_to_complete
    def test_approximate_time_to_complete_label(self):
        course = Course.objects.get(id=1)
        field_label = course._meta.get_field('approximate_time_to_complete').verbose_name
        self.assertEquals(field_label, 'approximate time to complete')

    # rating
    def test_rating_label(self):
        course = Course.objects.get(id=1)
        field_label = course._meta.get_field('rating').verbose_name
        self.assertEquals(field_label, 'rating')

    # ratings_number
    def test_ratings_number_label(self):
        course = Course.objects.get(id=1)
        field_label = course._meta.get_field('ratings_number').verbose_name
        self.assertEquals(field_label, 'ratings number')

    # language (FOREIGN KEY)
    def test_language_foreign_key_label(self):
        course = Course.objects.get(id=1)
        field_label = course._meta.get_field('language').verbose_name
        self.assertEquals(field_label, 'Язык курса')

    # lecturer (FOREIGN KEY)
    def test_lecturer_foreign_key_label(self):
        course = Course.objects.get(id=1)
        field_label = course._meta.get_field('lecturer').verbose_name
        self.assertEquals(field_label, 'Лектор')
