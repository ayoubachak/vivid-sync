from django.forms import ValidationError
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView

from authentication.views import  generate_access_token, generate_refresh_token
from registration.utils import send_verification_email
from .serializers import UserRegistrationSerializer
from users.models import VividUser
from django.utils import timezone
from datetime import datetime, timedelta
from django.contrib.auth import authenticate, login
from django.db import IntegrityError
from django.utils.crypto import get_random_string
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.exceptions import NotFound
from django.shortcuts import redirect


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
                # Send verification email
                user.verification_code = get_random_string(length=6, allowed_chars='1234567890')
                user.verification_token = get_random_string(length=100)
                user.save(update_fields=['verification_code', 'verification_token'])
                send_verification_email(user, request)

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

class SendEmailVerification(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Resend the verification email if needed
        user = request.user
        try:
            if not user.verification_code or not user.verification_token:
                # If not, generate them now and send a verification email
                user.verification_code = get_random_string(length=6, allowed_chars='1234567890')
                user.verification_token = get_random_string(length=100)
                user.save(update_fields=['verification_code', 'verification_token'])
            send_verification_email(user, request)
            return Response({'message': 'Verification email sent.'})
        except ObjectDoesNotExist:
            raise NotFound(detail="User with this email does not exist.")


class VerifyEmailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Resend the verification email if needed
        user = request.user
        token = request.query_params.get('token')
        print(f"{token=}") 
        print(f"{request.data=}") 
        try:
            if user.verification_token == token:
                if not user.email_verified:
                    user.email_verified = True
                    user.verification_code = ''  # Optionally clear the code
                    user.verification_token = ''  # Optionally clear the token
                    user.save()
                    return redirect('/terms-of-service/')
                    # return Response({'message': 'Email verified successfully'})
                else:
                    raise ValidationError('Email is already verified.')
            return Response({'message': 'Invalid Link'})
        except ObjectDoesNotExist:
            raise NotFound(detail="User with this email does not exist.")

    def post(self, request):
        user = request.user
        code = request.data.get('code')
        try:
            # Check if the user already has a verification token and code
            if not user.verification_code or not user.verification_token:
                # If not, generate them now and send a verification email
                user.verification_code = get_random_string(length=6, allowed_chars='1234567890')
                user.verification_token = get_random_string(length=100)
                user.save(update_fields=['verification_code', 'verification_token'])
                send_verification_email(user, request)

            # Now check if the provided token and code match
            if user.verification_code == code :
                if not user.email_verified:
                    user.email_verified = True
                    user.verification_code = ''  # Optionally clear the code
                    user.verification_token = ''  # Optionally clear the token
                    user.save()
                    return Response({'message': 'Email verified successfully'})
                else:
                    raise ValidationError('Email is already verified.')
            else:
                raise ValidationError('Verification code or token is incorrect.')

        except VividUser.DoesNotExist:
            raise ValidationError('User not found.')

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def resend_verification_email(request):
    user = request.user
    if not user.email_verified:
        if not user.verification_code or not user.verification_token:
            # If not, generate them now and send a verification email
            user.verification_code = get_random_string(length=6, allowed_chars='1234567890')
            user.verification_token = get_random_string(length=100)
            user.save(update_fields=['verification_code', 'verification_token'])
        send_verification_email(user, request)
        return Response({'message': 'Verification email sent.'})
    else:
        return Response({'message': 'Email is already verified.'}, status=status.HTTP_400_BAD_REQUEST)

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
