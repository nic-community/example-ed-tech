from django.urls import path
from rest_framework import routers

from .models import *
from .serializers import *
from .views.task_views import *
from .views.answer_views import *
from .views.grade_views import *


router = routers.SimpleRouter()
router.register(r'api/tasks', TaskViewSet, basename="tasksviewset")
router.register(r'api/answers', AnswerViewSet, basename="answersviewset")
router.register(r'api/grades', GradeViewSet, basename="gradesviewset")


urlpatterns = [

]

urlpatterns += router.urls