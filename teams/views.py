from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Team, TeamMember, TeamRole, InvitationLink
from .serializers import TeamSerializer, TeamMemberSerializer, TeamRoleSerializer, InvitationLinkSerializer

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class TeamMemberViewSet(viewsets.ModelViewSet):
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer

class TeamRoleViewSet(viewsets.ModelViewSet):
    queryset = TeamRole.objects.all()
    serializer_class = TeamRoleSerializer

class InvitationLinkViewSet(viewsets.ModelViewSet):
    queryset = InvitationLink.objects.all()
    serializer_class = InvitationLinkSerializer
