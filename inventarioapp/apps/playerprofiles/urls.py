from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'playerprofiles'

router = routers.DefaultRouter()
router.register('', views.PlayerProfileViewSet, basename='perfis-jogadores')

urlpatterns = [
    path('', include(router.urls) )
]
