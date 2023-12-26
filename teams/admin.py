from django.contrib import admin
from .models import Team, TeamRole, TeamMember, InvitationLink  # Adjust the import path according to your project structure


# Register your models here.
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'organization', 'created_at', 'updated_at')
    search_fields = ('name', 'organization__name')
    list_filter = ('organization',)
    ordering = ('name',)

admin.site.register(Team, TeamAdmin)
admin.site.register(TeamRole)

class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('user', 'team', 'role', 'joined_at')
    search_fields = ('user__username', 'team__name', 'role__name')
    list_filter = ('team', 'role')
    raw_id_fields = ('user', 'team', 'role')
    ordering = ('team', 'user')

admin.site.register(TeamMember, TeamMemberAdmin)

class InvitationLinkAdmin(admin.ModelAdmin):
    list_display = ('team', 'invite_code', 'created_at', 'expires_at')
    search_fields = ('team__name', 'invite_code')
    list_filter = ('team',)
    ordering = ('-created_at',)

admin.site.register(InvitationLink, InvitationLinkAdmin)
