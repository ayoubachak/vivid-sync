import graphene
from graphene_django import DjangoObjectType
from .models import AnalyticsData, PostAnalytics, SentimentAnalysis
from graphene import relay

class AnalyticsDataType(DjangoObjectType):
    class Meta:
        model = AnalyticsData
        fields = "__all__"
        interfaces = (relay.Node, )

class PostAnalyticsType(DjangoObjectType):
    class Meta:
        model = PostAnalytics
        fields = "__all__"
        interfaces = (relay.Node, )

class SentimentAnalysisType(DjangoObjectType):
    class Meta:
        model = SentimentAnalysis
        fields = "__all__"
        interfaces = (relay.Node, )

class Query(graphene.ObjectType):
    all_analytics_data = graphene.List(AnalyticsDataType)
    all_post_analytics = graphene.List(PostAnalyticsType)
    all_sentiment_analyses = graphene.List(SentimentAnalysisType)

    def resolve_all_analytics_data(root, info):
        return AnalyticsData.objects.all()

    def resolve_all_post_analytics(root, info):
        return PostAnalytics.objects.all()

    def resolve_all_sentiment_analyses(root, info):
        return SentimentAnalysis.objects.all()
