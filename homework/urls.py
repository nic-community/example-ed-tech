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
    # Homework Tasks
    # path('api/tasks', homework_task_list_api_view),
    # path('api/tasks/<int:pk>', homework_task_detail_api_view),
    # path('api/tasks', homework_taks_create_api_view),
    # path('api/tasks-update/<int:pk>', homework_task_update_api_view),
    # path('api/tasks-delete/<int:pk>', homework_task_delete_api_view),

]

urlpatterns += router.urls