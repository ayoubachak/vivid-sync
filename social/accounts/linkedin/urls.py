from django.urls import path
from .views import InitiateLinkedInAuth, LinkedInCallback

urlpatterns = [
    path('auth/init/', InitiateLinkedInAuth.as_view(), name='initiate-instagram-auth'),
    path('login/callback/', LinkedInCallback.as_view(), name='instagram-callback'),
]
