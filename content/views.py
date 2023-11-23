from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import Content, ContentPlatformStatus
from .serializers import ContentSerializer, ContentPlatformStatusSerializer

class ContentViewSet(viewsets.ModelViewSet):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    permission_classes = [AllowAny]

class ContentPlatformStatusViewSet(viewsets.ModelViewSet):
    queryset = ContentPlatformStatus.objects.all()
    serializer_class = ContentPlatformStatusSerializer
    permission_classes = [AllowAny]
