from django.urls import path
from rest_framework import routers
from .views import *
from course.views.language_view import *
from .views.lecturer_view import LecturerViewSet
from .views.language_view import LanguageViewSet
from .views.course_view import CourseViewSet

router = routers.SimpleRouter()
router.register(r'languages', LanguageViewSet, basename='languages-view')
router.register(r'lecturers', LecturerViewSet, basename='lecturers-view')
router.register(r'courses', CourseViewSet, basename='courses-view')


urlpatterns = [

]

urlpatterns += router.urls