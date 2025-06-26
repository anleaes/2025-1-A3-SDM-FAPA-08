from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'achievements'

router = routers.DefaultRouter()
router.register('', views.AchievementViewSet, basename='conquistas')

urlpatterns = [
    path('', include(router.urls) )
]
