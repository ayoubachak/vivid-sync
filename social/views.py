from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import SocialMediaPlatform, SocialMediaProfile, Post, Comment, Reply, Hashtag
from .serializers import (SocialMediaPlatformSerializer, SocialMediaProfileSerializer, 
                          PostSerializer, CommentSerializer, ReplySerializer, HashtagSerializer)
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

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
