from django.urls import path
from .views import InitiateInstagramBasicAuth, InstagramBasicCallback

urlpatterns = [
    path('auth/init/', InitiateInstagramBasicAuth.as_view(), name='initiate-instagram-auth'),
    path('login/callback/', InstagramBasicCallback.as_view(), name='instagram-callback'),
]
