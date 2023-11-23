from rest_framework import serializers
from .models import Content, ContentPlatformStatus

class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = '__all__'

class ContentPlatformStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentPlatformStatus
        fields = '__all__'
