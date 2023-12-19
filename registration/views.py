from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from .serializers import UserRegistrationSerializer


class RegisterUserView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserRegistrationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            # Send email verification here (if applicable)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
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
