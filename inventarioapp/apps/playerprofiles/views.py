from django.shortcuts import render
from .models import PlayerProfile
from rest_framework import viewsets
from .serializer import PlayerProfileSerializer

class PlayerProfileViewSet(viewsets.ModelViewSet):
    queryset = PlayerProfile.objects.all()
    serializer_class = PlayerProfileSerializer
