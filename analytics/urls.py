from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AnalyticsDataViewSet, PostAnalyticsViewSet, SentimentAnalysisViewSet

router = DefaultRouter()
router.register(r'analytics/analytics-data', AnalyticsDataViewSet)
router.register(r'analytics/post-analytics', PostAnalyticsViewSet)
router.register(r'analytics/sentiment-analysis', SentimentAnalysisViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
