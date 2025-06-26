from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'quests'

router = routers.DefaultRouter()
router.register('', views.QuestViewSet, basename='missoes')

urlpatterns = [
    path('', include(router.urls) )
]
