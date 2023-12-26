import graphene
from graphene_django import DjangoObjectType
from graphene import relay
from .models import SocialMediaPlatform, SocialMediaProfile, Post, Comment, Reply, ExternalUser, Hashtag

class SocialMediaPlatformType(DjangoObjectType):
    class Meta:
        model = SocialMediaPlatform
        fields = "__all__"
        interfaces = (relay.Node, )

class SocialMediaProfileType(DjangoObjectType):
    class Meta:
        model = SocialMediaProfile
        fields = "__all__"
        interfaces = (relay.Node, )

class PostType(DjangoObjectType):
    class Meta:
        model = Post
        fields = "__all__"
        interfaces = (relay.Node, )

class CommentType(DjangoObjectType):
    class Meta:
        model = Comment
        fields = "__all__"
        interfaces = (relay.Node, )

class ReplyType(DjangoObjectType):
    class Meta:
        model = Reply
        fields = "__all__"
        interfaces = (relay.Node, )

class ExternalUserType(DjangoObjectType):
    class Meta:
        model = ExternalUser
        fields = "__all__"
        interfaces = (relay.Node, )

class HashtagType(DjangoObjectType):
    class Meta:
        model = Hashtag
        fields = '__all__'
        interfaces = (relay.Node, )

class Query(graphene.ObjectType):
    all_social_media_platforms = graphene.List(SocialMediaPlatformType)
    all_social_media_profiles = graphene.List(SocialMediaProfileType)
    all_posts = graphene.List(PostType)
    all_comments = graphene.List(CommentType)
    all_replies = graphene.List(ReplyType)
    all_external_users = graphene.List(ExternalUserType)
    all_hashtags = graphene.List(HashtagType)

    def resolve_all_social_media_platforms(root, info):
        return SocialMediaPlatform.objects.all()

    def resolve_all_social_media_profiles(root, info):
        return SocialMediaProfile.objects.all()

    def resolve_all_posts(root, info):
        return Post.objects.all()

    def resolve_all_comments(root, info):
        return Comment.objects.all()

    def resolve_all_replies(root, info):
        return Reply.objects.all()

    def resolve_all_external_users(root, info):
        return ExternalUser.objects.all()
    
    def resolve_all_hashtags(root, info):
        return Hashtag.objects.all()
    

