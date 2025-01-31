from rest_framework import serializers
from .models import Chat

class GeminiInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ['prompt']

    def create(self, validated_data):
        return Chat.objects.create(**validated_data)