import jwt
from django.conf import settings
from users.models import VividUser  # Import your custom user model
from django.contrib.auth.backends import BaseBackend

class JWTAuthenticationBackend(BaseBackend):
    def authenticate(self, request, token=None):
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            user = VividUser.objects.get(id=payload['user_id'])  # Use VividUser
            return user
        except (jwt.DecodeError, VividUser.DoesNotExist):  # Catch VividUser.DoesNotExist
            return None

    def get_user(self, user_id):
        try:
            return VividUser.objects.get(pk=user_id)  # Use VividUser
        except VividUser.DoesNotExist:  # Catch VividUser.DoesNotExist
            return None
