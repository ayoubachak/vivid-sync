# users/schema.py

import graphene
from graphene_django import DjangoObjectType
from .models import VividUser
from graphene import relay

class VividUserType(DjangoObjectType):
    class Meta:
        model = VividUser
        fields = "__all__"
        interfaces = (relay.Node, )

class CreateUser(graphene.Mutation):
    class Arguments:
        username = graphene.String(required=True)
        # Add other user fields

    user = graphene.Field(VividUserType)

    @classmethod
    def mutate(cls, root, info, username, **kwargs):
        user = VividUser(username=username, **kwargs)
        user.set_password(kwargs.get('password'))
        user.save()
        return CreateUser(user=user)

class Query(graphene.ObjectType):
    all_users = graphene.List(VividUserType)

    def resolve_all_users(root, info):
        # Optionally: Ensure the user querying is authorized to view users
        return VividUser.objects.all()

class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()

