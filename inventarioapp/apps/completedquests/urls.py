from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'completedquests'

router = routers.DefaultRouter()
router.register('', views.CompletedQuestViewSet, basename='missoes-concluidas')

urlpatterns = [
    path('', include(router.urls) )
]
