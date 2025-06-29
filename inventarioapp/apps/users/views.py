from django.shortcuts import render
from .models import User
from rest_framework import viewsets
from .serializer import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer