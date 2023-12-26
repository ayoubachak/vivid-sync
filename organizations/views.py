from django.shortcuts import render
from rest_framework import viewsets
from .models import Organization, Industry
from .serializers import OrganizationSerializer, IndustrySerializer

# Create your views here.
class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer

class IndustryViewSet(viewsets.ModelViewSet):
    queryset = Industry.objects.all()
    serializer_class = IndustrySerializer

