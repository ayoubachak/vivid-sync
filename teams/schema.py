import graphene
from graphene_django import DjangoObjectType
from .models import Team, TeamRole, TeamMember, InvitationLink  # Adjust the import path according to your project structure

class TeamType(DjangoObjectType):
    class Meta:
        model = Team
        fields = "__all__"
        interfaces = (graphene.relay.Node, )

class TeamRoleType(DjangoObjectType):
    class Meta:
        model = TeamRole
        fields = "__all__"
        interfaces = (graphene.relay.Node, )

class TeamMemberType(DjangoObjectType):
    class Meta:
        model = TeamMember
        fields = "__all__"
        interfaces = (graphene.relay.Node, )

class InvitationLinkType(DjangoObjectType):
    class Meta:
        model = InvitationLink
        fields = "__all__"
        interfaces = (graphene.relay.Node, )


class Query(graphene.ObjectType):
    all_teams = graphene.List(TeamType)
    team_by_name = graphene.Field(TeamType, name=graphene.String(required=True))
    all_team_roles = graphene.List(TeamRoleType)
    team_members = graphene.List(TeamMemberType, team_id=graphene.Int())
    all_invitation_links = graphene.List(InvitationLinkType)

    def resolve_all_teams(self, info):
        return Team.objects.all()

    def resolve_team_by_name(self, info, name):
        return Team.objects.get(name=name)

    def resolve_all_team_roles(self, info):
        return TeamRole.objects.all()

    def resolve_team_members(self, info, team_id=None):
        if team_id:
            return TeamMember.objects.filter(team_id=team_id)
        return TeamMember.objects.all()

    def resolve_all_invitation_links(self, info):
        return InvitationLink.objects.all()


class CreateTeam(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        organization_id = graphene.Int(required=True)
        description = graphene.String()

    team = graphene.Field(TeamType)

    @classmethod
    def mutate(cls, root, info, name, organization_id, description=None):
        team = Team(name=name, organization_id=organization_id, description=description)
        team.save()
        return CreateTeam(team=team)

class Mutation(graphene.ObjectType):
    create_team = CreateTeam.Field()
    # Add other mutations as necessary
