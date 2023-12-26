from django.urls import include, path
from rest_framework import routers
from .views import OrganizationViewSet, IndustryViewSet


router = routers.DefaultRouter()
router.register(r'', OrganizationViewSet)
router.register(r'industries', IndustryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
