from rest_framework import serializers

from users.models import VividUser


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = VividUser
        fields = ['first_name', 'last_name', 'email', 'password']

    def create(self, validated_data):
        user = VividUser.objects.create(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            username=validated_data['email']  # Assuming username is the email
        )
        user.set_password(validated_data['password'])
        user.save()
        return user