from django.shortcuts import render
from .models import PlayerProfile
from rest_framework import viewsets
from .serializer import PlayerProfileSerializer
from django_filters.rest_framework import DjangoFilterBackend

class PlayerProfileViewSet(viewsets.ModelViewSet):
    queryset = PlayerProfile.objects.all()
    serializer_class = PlayerProfileSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['playername', 'level', 'experience']
