from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (SocialMediaPlatformViewSet, SocialMediaProfileViewSet,
                    PostViewSet, CommentViewSet, ReplyViewSet, HashtagViewSet)
from .views import update_social_links, get_social_links_by_user

router = DefaultRouter()
router.register(r'platforms', SocialMediaPlatformViewSet)
router.register(r'profiles', SocialMediaProfileViewSet)
router.register(r'post', PostViewSet)
router.register(r'comment', CommentViewSet)
router.register(r'reply', ReplyViewSet)
router.register(r'hashtag', HashtagViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('social-links/update/', update_social_links, name='update-social-links'),
    path('social-links/get/', get_social_links_by_user,name='get-social-links'),
]
