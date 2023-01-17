from django.urls import path
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from user.views import *


router = routers.SimpleRouter()
router.register(r'api/registration', RegistrationViewSet, basename='registration')

urlpatterns = [
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/', MyTokenObtainPairView.as_view(), name='token'),
]

urlpatterns += router.urls
