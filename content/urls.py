from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ContentViewSet, ContentPlatformStatusViewSet

router = DefaultRouter()
router.register(r'content/content', ContentViewSet)
router.register(r'content/content-status', ContentPlatformStatusViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
