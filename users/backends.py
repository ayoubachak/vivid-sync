import jwt
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.backends import BaseBackend

class JWTAuthenticationBackend(BaseBackend):
    def authenticate(self, request, token=None):
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            user = User.objects.get(id=payload['user_id'])
            return user
        except (jwt.DecodeError, User.DoesNotExist):
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
