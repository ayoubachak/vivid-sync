from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TeamViewSet, TeamMemberViewSet, TeamRoleViewSet, InvitationLinkViewSet

router = DefaultRouter()
router.register(r'', TeamViewSet)
router.register(r'team/members', TeamMemberViewSet)
router.register(r'team/roles', TeamRoleViewSet)
router.register(r'invite/link', InvitationLinkViewSet)


urlpatterns = [
    path('', include(router.urls)),
]