from rest_framework import serializers

from users.models import VividUser


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = VividUser
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = VividUser.objects.create_user(**validated_data)
        return user
