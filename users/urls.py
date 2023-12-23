from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VividUserViewSet, accept_terms_of_service

router = DefaultRouter()
router.register(r'', VividUserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('terms-of-service/accept/', accept_terms_of_service, name="accept-terms-of-service"),
]
