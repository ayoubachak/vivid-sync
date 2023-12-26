# users/schema.py

import graphene
from graphene_django import DjangoObjectType

from social.schema import HashtagType
from .models import AccountType, VividUser
from graphene import relay
from django.db.models import Q
from graphql_jwt.decorators import login_required

class VividUserType(DjangoObjectType):

    hashtags = graphene.List(HashtagType)
    
    class Meta:
        model = VividUser
        fields = "__all__"
        interfaces = (relay.Node, )
    
    def resolve_hashtags(self, info):
        # Assuming the relationship name in the VividUser model is `hashtags`
        return self.hashtags.all()


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

class ChangeAccountType(graphene.Mutation):
    class Arguments:
        account_type = graphene.String(required=True)

    user = graphene.Field(VividUserType)
    success = graphene.Boolean()
    message = graphene.String()

    @classmethod
    @login_required
    def mutate(cls, root, info, account_type):
        # Get the current user from the context
        user = info.context.user
        if not user.is_authenticated:
            return cls(success=False, message="You must be logged in to change your account type.")
        # Check if the account type is valid
        if account_type not in AccountType.values:
            return cls(success=False, message="Invalid account type.")
        # Set the new account type
        user.account_type = account_type
        user.save()
        return cls(user=user, success=True, message="Account type changed successfully.")


class DeleteUserByEmail(graphene.Mutation):
    class Arguments:
        email = graphene.String(required=True)

    success = graphene.Boolean()
    message = graphene.String()

    @classmethod
    def mutate(cls, root, info, email):
        try:
            user = VividUser.objects.get(Q(email=email))
            user.delete()
            return cls(success=True, message="User deleted successfully.")
        except VividUser.DoesNotExist:
            return cls(success=False, message="User not found.")
        except Exception as e:
            return cls(success=False, message=str(e))

class Query(graphene.ObjectType):
    all_users = graphene.List(VividUserType)
    me = graphene.Field(VividUserType)
    def resolve_all_users(root, info):
        # Optionally: Ensure the user querying is authorized to view users
        return VividUser.objects.all()
    def resolve_me(self, info):
        user = info.context.user
        if user.is_authenticated:
            return user
        raise Exception('Authentication credentials were not provided')

class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    delete_user_by_email = DeleteUserByEmail.Field()
    change_account_type = ChangeAccountType.Field()
