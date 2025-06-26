from .models import CompletedQuest
from rest_framework import serializers

class CompletedQuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompletedQuest
        fields = '__all__'
