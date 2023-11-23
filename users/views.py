from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import VividUser
from .serializers import VividUserSerializer

class VividUserViewSet(viewsets.ModelViewSet):
    queryset = VividUser.objects.all()
    serializer_class = VividUserSerializer
    permission_classes = [AllowAny]
