from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (SocialMediaPlatformViewSet, SocialMediaProfileViewSet,
                    PostViewSet, CommentViewSet, ReplyViewSet)

router = DefaultRouter()
router.register(r'platforms', SocialMediaPlatformViewSet)
router.register(r'profiles', SocialMediaProfileViewSet)
router.register(r'post', PostViewSet)
router.register(r'comment', CommentViewSet)
router.register(r'reply', ReplyViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
