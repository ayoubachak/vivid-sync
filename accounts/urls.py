
from django.urls import path, include
from . import views

urlpatterns = [
     path('instagram/', include('accounts.instagram.urls')),
]
