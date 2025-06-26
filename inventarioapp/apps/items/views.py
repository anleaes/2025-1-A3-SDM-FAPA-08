from django.shortcuts import render
from .models import Item
from rest_framework import viewsets
from .serializer import ItemSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
