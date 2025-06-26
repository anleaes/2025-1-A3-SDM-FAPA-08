from django.shortcuts import render
from .models import Inventario
from rest_framework import viewsets
from .serializer import InventarioSerializer

class InventarioViewSet(viewsets.ModelViewSet):
    queryset = Inventario.objects.all()
    serializer_class = InventarioSerializer
