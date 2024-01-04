from django.urls import path
from .views import InitiateInstagramBusinesssAuth, InstagramBusinessCallback

urlpatterns = [
    path('instagram/auth/init/', InitiateInstagramBusinesssAuth.as_view(), name='initiate-instagram-business-auth'),
    path('instagram/login/callback/', InstagramBusinessCallback.as_view(), name='instagram-business-callback'),
]
