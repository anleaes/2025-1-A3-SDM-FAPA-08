from django.shortcuts import render
from .models import Achievement
from rest_framework import viewsets
from .serializer import AchievementSerializer

class AchievementViewSet(viewsets.ModelViewSet):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer
