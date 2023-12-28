from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    VividUserViewSet, 
    accept_terms_of_service, 
    upload_profile_picture, 
    delete_profile_picture, 
    check_username_availability, 
    update_user_profile,
    CurrentUserView
)


router = DefaultRouter()
router.register(r'', VividUserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('me/info/', CurrentUserView.as_view(), name="current-user"),  # Add this line
    path('terms-of-service/accept/', accept_terms_of_service, name="accept-terms-of-service"),
    path('profile-picture/upload/', upload_profile_picture, name="upload-profile-picture"),
    path('profile-picture/delete/', delete_profile_picture, name="delete-profile-picture"),
    path('check/username/<str:username>/', check_username_availability, name="check-username-availability"),
    path('update/profile/', update_user_profile, name='update-user-profile'),

]
