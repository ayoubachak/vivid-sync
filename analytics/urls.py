from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AnalyticsDataViewSet, PostAnalyticsViewSet, SentimentAnalysisViewSet

router = DefaultRouter()
router.register(r'analytics-data', AnalyticsDataViewSet)
router.register(r'post-analytics', PostAnalyticsViewSet)
router.register(r'sentiment-analysis', SentimentAnalysisViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
