import graphene
from graphene_django import DjangoObjectType
from .models import Content, ContentPlatformStatus
from graphene import relay

class ContentType(DjangoObjectType):
    class Meta:
        model = Content
        fields = "__all__"
        interfaces = (relay.Node, )

class ContentPlatformStatusType(DjangoObjectType):
    class Meta:
        model = ContentPlatformStatus
        fields = "__all__"
        interfaces = (relay.Node, )

class Query(graphene.ObjectType):
    all_contents = graphene.List(ContentType)
    all_content_platform_statuses = graphene.List(ContentPlatformStatusType)

    def resolve_all_contents(root, info):
        return Content.objects.all()

    def resolve_all_content_platform_statuses(root, info):
        return ContentPlatformStatus.objects.all()

