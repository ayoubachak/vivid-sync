from rest_framework import serializers
from .models import VividUser

class VividUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = VividUser
        fields = '__all__'  # Specify fields you want to include
