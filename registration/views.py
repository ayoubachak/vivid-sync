from django.forms import ValidationError
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView

from authentication.views import  generate_access_token, generate_refresh_token
from registration.utils import send_password_reset_email, send_verification_email
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
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes,  force_str
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode

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


    

class UpdateProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request):
        # Implement profile update logic here
        # Update user information
        return Response({...})


class PasswordResetView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = VividUser.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, VividUser.DoesNotExist):
            user = None

        if user is not None and default_token_generator.check_token(user, token):
            new_password = request.data.get('password')
            user.set_password(new_password)
            user.save()
            return Response({'message': 'Password has been reset.'})
        else:
            return Response({'error': 'Invalid token or user ID.'}, status=status.HTTP_400_BAD_REQUEST)
    

class SendPasswordResetLink(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get('email')
        try:
            user = VividUser.objects.get(email=email)
            send_password_reset_email(user, request)
            return Response({'message': 'Password reset link sent.'})
        except VividUser.DoesNotExist:
            return Response({'error': 'User with this email does not exist.'}, status=status.HTTP_404_NOT_FOUND)
        
class PasswordResetConfirmView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = VividUser.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, VividUser.DoesNotExist):
            user = None

        if user is not None and default_token_generator.check_token(user, token):
            # The token is valid, inform the frontend
            return Response({'valid': True, 'uid': uidb64, 'token': token})
        else:
            # Invalid token
            return Response({'valid': False}, status=400)
    
    def post(self, request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = VividUser.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, VividUser.DoesNotExist):
            user = None

        if user is not None and default_token_generator.check_token(user, token):
            new_password = request.data.get('password')
            user.set_password(new_password)
            user.save()
            return Response({'message': 'Password has been reset.'})
        else:
            return Response({'error': 'Invalid token or user ID.'}, status=status.HTTP_400_BAD_REQUEST)
    