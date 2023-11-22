from django.contrib import admin

# Register your models here.
from analytics.models import AnalyticsData, PostAnalytics, SentimentAnalysis

@admin.register(AnalyticsData)
class AnalyticsDataAdmin(admin.ModelAdmin):
    list_display = ('profile', 'date', 'followers_count', 'likes_count')
    list_filter = ('profile', 'date')

@admin.register(PostAnalytics)
class PostAnalyticsAdmin(admin.ModelAdmin):
    list_display = ('post', 'date', 'likes_count', 'comments_count')
    list_filter = ('post', 'date')

@admin.register(SentimentAnalysis)
class SentimentAnalysisAdmin(admin.ModelAdmin):
    list_display = ('post', 'sentiment', 'positive_score', 'negative_score')
    list_filter = ('post', 'sentiment')
