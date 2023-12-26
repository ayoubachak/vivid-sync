import graphene
from graphene_django import DjangoObjectType
from .models import Organization, Industry  # Adjust the import path according to your project structure

class OrganizationType(DjangoObjectType):
    class Meta:
        model = Organization
        fields = "__all__"
        interfaces = (graphene.relay.Node, )

class IndustryType(DjangoObjectType):
    class Meta:
        model = Industry
        fields = "__all__"
        interfaces = (graphene.relay.Node, )


class Query(graphene.ObjectType):
    all_organizations = graphene.List(OrganizationType)
    organization_by_name = graphene.Field(OrganizationType, name=graphene.String(required=True))
    all_industries = graphene.List(IndustryType)

    def resolve_all_organizations(self, info):
        return Organization.objects.all()

    def resolve_organization_by_name(self, info, name):
        return Organization.objects.get(name=name)

    def resolve_all_industries(self, info):
        return Industry.objects.all()


class CreateOrganization(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        # Add other organization fields as necessary

    organization = graphene.Field(OrganizationType)

    @classmethod
    def mutate(cls, root, info, name, **kwargs):
        organization = Organization(name=name, **kwargs)
        organization.save()
        return CreateOrganization(organization=organization)

class Mutation(graphene.ObjectType):
    create_organization = CreateOrganization.Field()
    # Add other mutations as necessary


