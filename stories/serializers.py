from rest_framework import serializers
from .models import Story

class StorySerializer(serializers.ModelSerializer):
    """Serializer for AI-generated stories"""

    class Meta:
        model = Story
        fields = ['id', 'title', 'content', 'author', 'created_at']
        read_only_fields = ['author', 'created_at']
