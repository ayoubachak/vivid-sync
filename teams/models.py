from django.db import models

from django.db import models
from users.models import VividUser
from organizations.models import Organization

class Team(models.Model):
    name = models.CharField(max_length=255)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='teams')
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class TeamRole(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class TeamMember(models.Model):
    user = models.ForeignKey(VividUser, on_delete=models.CASCADE, related_name='team_memberships')
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='members')
    role = models.ForeignKey(TeamRole, on_delete=models.SET_NULL, null=True, blank=True, related_name='team_members')
    joined_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.role.name} in {self.team.name}"


class InvitationLink(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    invite_code = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()

    def __str__(self):
        return f"Invitation for {self.team.name}"
