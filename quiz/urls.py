from django.urls import path
from rest_framework import routers
from .views.final_quiz_views import FinalQuizViewSet
from .views.final_quiz_question_views import FinalQuizQuestionViewSet
from .views.final_quiz_answer_views import FinalQuizAnswerViewSet
from .views.lesson_quiz_views import LessonQuizViewSet
from .views.lesson_quiz_question_views import LessonQuizQuestionViewSet
from .views.lesson_quiz_answer_views import LessonQuizAnswerViewSet

urlpatterns = []

router = routers.SimpleRouter()
router.register(r'final-quiz', FinalQuizViewSet, basename='final-quiz-view')
router.register(r'final-quiz-question', FinalQuizQuestionViewSet, basename='final-quiz-question-view')
router.register(r'final-quiz-answer', FinalQuizAnswerViewSet, basename='final-quiz-answer-view')
router.register(r'lesson-quiz', LessonQuizViewSet, basename='lesson-quiz-view')
router.register(r'lesson-quiz-question', LessonQuizQuestionViewSet, basename='lesson-quiz-question-view')
router.register(r'lesson-quiz-answer', LessonQuizAnswerViewSet, basename='lesson-quiz-answer-view')

urlpatterns += router.urls
