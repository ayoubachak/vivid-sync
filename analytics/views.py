from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import AnalyticsData, PostAnalytics, SentimentAnalysis
from .serializers import AnalyticsDataSerializer, PostAnalyticsSerializer, SentimentAnalysisSerializer

class AnalyticsDataViewSet(viewsets.ModelViewSet):
    queryset = AnalyticsData.objects.all()
    serializer_class = AnalyticsDataSerializer
    permission_classes = [AllowAny]

class PostAnalyticsViewSet(viewsets.ModelViewSet):
    queryset = PostAnalytics.objects.all()
    serializer_class = PostAnalyticsSerializer
    permission_classes = [AllowAny]

class SentimentAnalysisViewSet(viewsets.ModelViewSet):
    queryset = SentimentAnalysis.objects.all()
    serializer_class = SentimentAnalysisSerializer
    permission_classes = [AllowAny]


