from django.shortcuts import render
from rest_framework.response import Response

from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from social.models import Hashtag
from .models import GenderChoices, VividUser
from .serializers import VividUserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from django.core.files.storage import default_storage
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
import re
import base64

class CurrentUserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = VividUserSerializer(request.user)
        return Response(serializer.data)

class VividUserViewSet(viewsets.ModelViewSet):
    queryset = VividUser.objects.all()
    serializer_class = VividUserSerializer
    permission_classes = [AllowAny]

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def accept_terms_of_service(request):
    user = request.user
    user.agreed_to_terms = True
    user.save(update_fields=['agreed_to_terms'])
    return Response({"message": "Terms of service accepted"}, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def upload_profile_picture(request):
    user = request.user
    file = request.FILES.get('profile_picture')

    if not file:
        return Response({"error": "No file provided."}, status=status.HTTP_400_BAD_REQUEST)

    # Check file size (2 MB limit)
    if file.size > 2 * 1024 * 1024:  # 2 MB
        return Response({"error": "File size exceeds 2 MB."}, status=status.HTTP_400_BAD_REQUEST)
    
    file_name = default_storage.save(f'users/{user.id}/images/profile_pic/{file.name}', file)
    user.profile_picture = file_name
    user.save()
    return Response({"message": "Profile picture updated successfully.", "profile_picture_url": user.profile_picture.url}, status=status.HTTP_200_OK)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_profile_picture(request):
    user = request.user

    if user.profile_picture:
        # Delete the file from storage
        user.profile_picture.delete()
        user.profile_picture = None
        user.save()

    return Response({"message": "Profile picture deleted successfully."}, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])  # Adjust the permissions as needed
def check_username_availability(request, username):
    User = get_user_model()

    # Regex for valid usernames (letters, numbers, underscores, periods)
    if not re.match(r'^[a-zA-Z0-9._]+$', username):
        return JsonResponse({'error': 'Username contains invalid characters.'}, status=400)

    if User.objects.filter(username=username).exists():
        if request.user.username == username:
            return JsonResponse({'available': True, 'message': 'Username is available.'})
        else:
            return JsonResponse({'available': False, 'message': 'Username is already taken.'})
    else:
        return JsonResponse({'available': True, 'message': 'Username is available.'})
    

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def update_user_profile(request):
    user = request.user
    data = request.data

    # Update username
    username = data.get('username')
    if username and username != user.username:
        if not re.match(r'^[a-zA-Z0-9._]+$', username):
            return Response({"error": "Username contains invalid characters."}, status=status.HTTP_400_BAD_REQUEST)
        if VividUser.objects.exclude(pk=user.pk).filter(username=username).exists():
            return Response({"error": "Username is already taken."}, status=status.HTTP_400_BAD_REQUEST)
        user.username = username

    # Update bio
    bio = data.get('bio')
    if bio is not None:
        user.bio = bio
    else :
        return Response({"error": "User must fill the Bio"}, status=status.HTTP_400_BAD_REQUEST)

    # Update gender
    gender = data.get('gender')
    if gender in [choice[0] for choice in GenderChoices.choices]:
        user.gender = gender
    else :
        return Response({"error": "User must choose a gender"}, status=status.HTTP_400_BAD_REQUEST)

    user.profile_completed = True
    user.save()
    return Response({"message": "Profile updated successfully."}, status=status.HTTP_200_OK)
