from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import SocialMediaPlatform, SocialMediaProfile, Post, Comment, Reply
from .serializers import (SocialMediaPlatformSerializer, SocialMediaProfileSerializer, 
                          PostSerializer, CommentSerializer, ReplySerializer)

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

