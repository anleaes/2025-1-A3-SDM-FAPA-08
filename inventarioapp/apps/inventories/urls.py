from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'inventories'

router = routers.DefaultRouter()
router.register('', views.InventarioViewSet, basename='inventarios')

urlpatterns = [
    path('', include(router.urls) )
]
