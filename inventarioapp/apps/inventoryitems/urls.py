from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'inventoryitems'

router = routers.DefaultRouter()
router.register('', views.InventoryItemViewSet, basename='itens-inventario')

urlpatterns = [
    path('', include(router.urls) )
]
