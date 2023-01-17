from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import serializers

from user.models import User
from django.contrib.auth.hashers import make_password


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['role'] = user.role
        # ...

        return token


class RegistrationRequestSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=256)
    first_name = serializers.CharField(max_length=256)
    last_name = serializers.CharField(max_length=256)
    phone_number = serializers.CharField(max_length=15)
    email = serializers.EmailField(max_length=256)
    password = serializers.CharField(max_length=100)

    def create(self, validated_data):
        # Hashing
        validated_data["password"] = make_password(validated_data['password'])
        return User.objects.create(**validated_data)

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'phone_number',
            'email',
            'password',
            'username'
        ]

