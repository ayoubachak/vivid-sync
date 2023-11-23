from django.shortcuts import render

# Create your views here.
import jwt
from django.conf import settings
from django.contrib.auth import authenticate
from django.http import JsonResponse
from datetime import datetime, timedelta
from users.models import VividUser
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import AuthTokenSerializer, VividUserSerializer

def generate_access_token(user):
    access_token_payload = {
        'user_id': user.id,
        'exp': datetime.utcnow() + timedelta(minutes=30),  # short-lived access token
        'iat': datetime.utcnow(),
    }
    return jwt.encode(access_token_payload, settings.SECRET_KEY, algorithm='HS256')

def generate_refresh_token(user):
    refresh_token_payload = {
        'user_id': user.id,
        'exp': datetime.utcnow() + timedelta(days=7),  # long-lived refresh token
        'iat': datetime.utcnow(),
    }
    return jwt.encode(refresh_token_payload, settings.SECRET_KEY, algorithm='HS256')



class ObtainJWTToken(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(request_body=AuthTokenSerializer)
    def post(self, request, *args, **kwargs):
        serializer = AuthTokenSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(**serializer.validated_data)

            if user:
                access_token = generate_access_token(user)
                refresh_token = generate_refresh_token(user)
                return Response({
                    'access_token': access_token,
                    'refresh_token': refresh_token
                })
            return Response({'error': 'Invalid Credentials'}, status=400)
        return Response(serializer.errors, status=400)

class RefreshToken(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'refresh_token': openapi.Schema(type=openapi.TYPE_STRING, description='Refresh token'),
        }
    ))
    def post(self, request, *args, **kwargs):
        refresh_token = request.data.get('refresh_token')
        try:
            payload = jwt.decode(refresh_token, settings.SECRET_KEY, algorithms=['HS256'])
            user = VividUser.objects.get(id=payload['user_id'])

            if payload['exp'] < datetime.utcnow().timestamp():
                return Response({'error': 'Refresh token expired'}, status=400)

            new_token = generate_access_token(user)
            return Response({'token': new_token})
        except jwt.ExpiredSignatureError:
            return Response({'error': 'Refresh token expired'}, status=400)
        except jwt.DecodeError:
            return Response({'error': 'Invalid token'}, status=400)
        except VividUser.DoesNotExist:
            return Response({'error': 'User not found'}, status=404)


class UserMeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Assuming the request.user is already populated by the token authentication class
        user = request.user
        serializer = VividUserSerializer(user)
        return Response(serializer.data)