from django.db import models
from social.models import SocialMediaProfile

class AnalyticsData(models.Model):
    profile = models.ForeignKey(SocialMediaProfile, on_delete=models.CASCADE, related_name='analytics')
    date = models.DateField()
    followers_count = models.IntegerField(default=0)
    likes_count = models.IntegerField(default=0)
    comments_count = models.IntegerField(default=0)
    shares_count = models.IntegerField(default=0)
    engagement_rate = models.FloatField(default=0.0)
    reach = models.IntegerField(default=0)
    impressions = models.IntegerField(default=0)

    def __str__(self):
        return f"Analytics for {self.profile.user.username} on {self.profile.platform.name} - {self.date}"


class PostAnalytics(models.Model):
    post = models.ForeignKey('social.Post', on_delete=models.CASCADE, related_name='analytics')
    date = models.DateField()
    likes_count = models.IntegerField(default=0)
    comments_count = models.IntegerField(default=0)
    shares_count = models.IntegerField(default=0)
    reach = models.IntegerField(default=0)
    impressions = models.IntegerField(default=0)
    engagement_rate = models.FloatField(default=0.0)

    def __str__(self):
        return f"Post Analytics for Post ID {self.post.id} - {self.date}"


class SentimentAnalysis(models.Model):
    post = models.ForeignKey('social.Post', on_delete=models.CASCADE, related_name='sentiment_analysis')
    positive_score = models.FloatField(default=0.0)
    negative_score = models.FloatField(default=0.0)
    neutral_score = models.FloatField(default=0.0)
    sentiment = models.CharField(max_length=50)  # e.g., "Positive", "Negative", "Neutral"

    def __str__(self):
        return f"Sentiment Analysis for Post ID {self.post.id}"
