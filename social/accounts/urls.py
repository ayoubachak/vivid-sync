
from django.urls import path, include
from . import views

urlpatterns = [
     path('instagram/', include('social.accounts.instagram.urls')),
     path('facebook/', include('social.accounts.facebook.urls')),
]
