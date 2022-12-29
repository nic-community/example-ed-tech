from django.urls import path
from .views import *

urlpatterns = [
    # ----- LANGUAGE model -----
    path('api/languages', language_list_api_view),
    path('api/languages/<int:pk>', language_detail_api_view),
    path('api/language-create', language_create_api_view),
    path('api/language-update/<int:pk>', language_update_api_view),
    path('api/language-delete/<int:pk>', language_delete_api_view),

    # ----- LECTURER model -----
    path('api/lecturers', lecturer_list_api_view),
    path('api/lecturers/<int:pk>', lecturer_detail_api_view),
    path('api/lecturers-create', lecturer_create_api_view),
    path('api/lecturers-update/<int:pk>', lecturer_update_api_view),
    path('api/lecturers-delete/<int:pk>', lecturer_delete_api_view),

    # ----- COURSE model -----
    path('api/courses', course_list_api_view),
    path('api/courses/<int:pk>', course_detail_api_view),
    path('api/courses-create', course_create_api_view),
    path('api/courses-update/<int:pk>', course_update_api_view),
    path('api/courses-delete/<int:pk>', course_delete_api_view),
]