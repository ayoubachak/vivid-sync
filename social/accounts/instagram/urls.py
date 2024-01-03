from django.urls import path
from .views import InitiateInstagramAuth, InstagramCallback

urlpatterns = [
    path('auth/init/', InitiateInstagramAuth.as_view(), name='initiate-instagram-auth'),
    path('login/callback/', InstagramCallback.as_view(), name='instagram-callback'),
]
