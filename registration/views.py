from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView

from authentication.views import  generate_access_token, generate_refresh_token
from .serializers import UserRegistrationSerializer
from users.models import VividUser
from django.utils import timezone
from datetime import datetime, timedelta
from django.contrib.auth import authenticate, login
from django.db import IntegrityError


class RegisterUserView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserRegistrationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            try :
                user : VividUser= serializer.save()
                access_token = generate_access_token(user)
                refresh_token = generate_refresh_token(user)
                access_token_exp = timezone.now() + timedelta(days=7) # session will last as much as the refresh token 
                request.session.set_expiry(access_token_exp)
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                login(request, user, backend='authentication.backends.JWTAuthenticationBackend')

                return Response({
                    "data" : serializer.data, 
                    "user":user.info(),
                    "access_token" : access_token,
                    "refresh_token": refresh_token
                    }, status=status.HTTP_201_CREATED)
            except IntegrityError as e:
                    # Here you handle the IntegrityError
                    return Response({"error": "This Email is already in use"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VerifyEmailView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        # Implement email verification logic here
        # This usually involves checking a token sent to the email
        return Response({...})

class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Implement password change logic here
        # Validate old password and set new password
        return Response({...})
    

class UpdateProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request):
        # Implement profile update logic here
        # Update user information
        return Response({...})
