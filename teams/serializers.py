from rest_framework import serializers
from .models import Team, TeamMember, TeamRole, InvitationLink

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'

class TeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMember
        fields = '__all__'

class TeamRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamRole
        fields = '__all__'

class InvitationLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvitationLink
        fields = '__all__'
