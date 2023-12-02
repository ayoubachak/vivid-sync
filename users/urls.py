from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VividUserViewSet

router = DefaultRouter()
router.register(r'', VividUserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
