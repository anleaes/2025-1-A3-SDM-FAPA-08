from django.shortcuts import render
from .models import Quest
from rest_framework import viewsets
from .serializer import QuestSerializer

class QuestViewSet(viewsets.ModelViewSet):
    queryset = Quest.objects.all()
    serializer_class = QuestSerializer
