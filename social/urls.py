from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (SocialMediaPlatformViewSet, SocialMediaProfileViewSet,
                    PostViewSet, CommentViewSet, ReplyViewSet)

router = DefaultRouter()
router.register(r'social/platforms', SocialMediaPlatformViewSet)
router.register(r'social/profiles', SocialMediaProfileViewSet)
router.register(r'social/post', PostViewSet)
router.register(r'social/comment', CommentViewSet)
router.register(r'social/reply', ReplyViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
