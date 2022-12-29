from django.urls import path
from .views import *

urlpatterns = [
    # Homework Tasks
    path('api/homework-tasks', homework_task_list_API_view),
    path('api/homework-tasks/<int:pk>', homework_task_detail_API_view),
    path('api/homework-tasks-create', homework_taks_create_API_view),
    path('api/homework-tasks-update/<int:pk>', homework_task_update_API_view),
    path('api/homework-tasks-delete/<int:pk>', homework_task_delete_API_view),

    # Homework Answers
    path('api/homework-answers', homework_answer_list_API_view),
    path('api/homework-answers/<int:pk>', homework_answer_detail_API_view),
    path('api/homework-answers-create', homework_answer_create_API_view),
    path('api/homework-answers-update/<int:pk>', homework_answer_update_API_view),
    path('api/homework-answers-delete/<int:pk>', homework_answer_delete_API_view),

    # Grades
    path('api/homework-grades', homework_grade_list_API_view),
    path('api/homework-grades/<int:pk>', homework_grade_detail_API_view),
    path('api/homework-grades-create', homework_grade_create_API_view),
    path('api/homework-grades-update/<int:pk>', homework_grade_update_API_view),
    path('api/homework-grades-delete/<int:pk>', homework_grade_delete_API_view),
]
