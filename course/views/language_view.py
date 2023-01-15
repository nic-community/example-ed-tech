from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from ..serializers import *
from rest_framework import viewsets, status
from rest_framework.response import Response
from ..models import *
from django.shortcuts import get_object_or_404


class LanguageViewSet(viewsets.ViewSet):
    def list(self, request):
        languages = Language.objects.all()
        serializer = LanguageResponseSerializer(languages, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        queryset = Language.objects.all()
        language = get_object_or_404(queryset, pk=pk)
        serializer = LanguageResponseSerializer(language)
        return Response(serializer.data)

    def create(self, request):
        serializer = LanguageRequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            language = Language.objects.filter(pk=serializer.data["id"])
            return Response(language.values()[0], status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk):
        queryset = Language.objects.all()
        language = get_object_or_404(queryset, pk=pk)
        serializer = LanguageRequestSerializer(language, data=request.data)
        if serializer.is_valid():
            serializer.save()
            language = Language.objects.filter(pk=serializer.data["id"])
            return Response(language.values()[0], status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        queryset = Language.objects.all()
        language = get_object_or_404(queryset, pk=pk)
        language.delete()
        return Response("Language deleted", status=status.HTTP_204_NO_CONTENT)
