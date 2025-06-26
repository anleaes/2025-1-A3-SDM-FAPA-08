from django.shortcuts import render
from .models import CompletedQuest
from rest_framework import viewsets
from .serializer import CompletedQuestSerializer

class CompletedQuestViewSet(viewsets.ModelViewSet):
    queryset = CompletedQuest.objects.all()
    serializer_class = CompletedQuestSerializer
