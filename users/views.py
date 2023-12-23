from django.shortcuts import render
from rest_framework.response import Response

from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import VividUser
from .serializers import VividUserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status

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