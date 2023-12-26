from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import SocialLink, SocialMediaPlatform, SocialMediaProfile, Post, Comment, Reply, Hashtag
from .serializers import (SocialMediaPlatformSerializer, SocialMediaProfileSerializer, 
                          PostSerializer, CommentSerializer, ReplySerializer, HashtagSerializer)
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.decorators import api_view, permission_classes


class SocialMediaPlatformViewSet(viewsets.ModelViewSet):
    queryset = SocialMediaPlatform.objects.all()
    serializer_class = SocialMediaPlatformSerializer
    permission_classes = [AllowAny]

class SocialMediaProfileViewSet(viewsets.ModelViewSet):
    queryset = SocialMediaProfile.objects.all()
    serializer_class = SocialMediaProfileSerializer
    permission_classes = [AllowAny]

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [AllowAny]

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [AllowAny]

class ReplyViewSet(viewsets.ModelViewSet):
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer
    permission_classes = [AllowAny]

class HashtagViewSet(viewsets.ModelViewSet):
    queryset = Hashtag.objects.all()
    serializer_class = HashtagSerializer
    permission_classes = [IsAuthenticated]
    
    
    @swagger_auto_schema(method='get', manual_parameters=[
        openapi.Parameter('tag', 
                          openapi.IN_QUERY, 
                          description="Tag to search for", 
                          type=openapi.TYPE_STRING
                          )
    ])
    @action(detail=False, methods=['GET'])
    def suggest_hashtags(self, request):
        tag = request.query_params.get('tag', '')
        hashtags = self.queryset.filter(name__istartswith=tag)
        serializer = self.get_serializer(hashtags, many=True)
        return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def update_social_links(request):
    user = request.user
    data = request.data.get('links', [])
    
    for link in data:
        link_type = link.get('type')
        url = link.get('url')
        # Update the website directly on the user model
        if link_type == 'website':
            user.website_link = url
            user.save()
        else:
            # Check if the social link already exists
            social_link, created = SocialLink.objects.get_or_create(
                user=user,
                platform=str(link_type).capitalize(),
                defaults={'url': url}
            )
            # If it wasn't just created, it means it already existed, and we need to update it
            if not created:
                social_link.url = url
                social_link.save()

    return Response({"message": "Social links updated successfully."}, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_social_links_by_user(request):
    # Get the current authenticated user
    user = request.user
    print(user.username)
    # Retrieve all social links for the user
    social_links = SocialLink.objects.filter(user=user)

    # Serialize the data to send as a response
    links_data = {
        "website": user.website_link,
        "instagram": "",
        "facebook": "",
        "youtube": "",
        "twitter": "",
        "linkedin": "",
    }

    # Map the social links to their respective platforms
    print("list(social_links)=",list(social_links))
    for link in social_links:
        print("link=",link)
        if link.platform == 'Instagram':
            links_data["instagram"] = link.url
        elif link.platform == 'Facebook':
            links_data["facebook"] = link.url
        elif link.platform == 'YouTube':
            links_data["youtube"] = link.url
        elif link.platform == 'Twitter':
            links_data["twitter"] = link.url
        elif link.platform == 'LinkedIn':
            links_data["linkedin"] = link.url
        # Add more platforms as needed

    return Response(links_data)