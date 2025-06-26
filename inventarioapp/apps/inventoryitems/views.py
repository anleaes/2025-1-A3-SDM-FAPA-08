from django.shortcuts import render
from .models import InventoryItem
from rest_framework import viewsets
from .serializer import InventoryItemSerializer

class InventoryItemViewSet(viewsets.ModelViewSet):
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer
