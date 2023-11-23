from django.urls import path
from .views import ObtainJWTToken, RefreshToken, UserMeView

urlpatterns = [
    path('token/', ObtainJWTToken.as_view(), name='token_obtain'),
    path('token/refresh/', RefreshToken.as_view(), name='token_refresh'),
    path('me/', UserMeView.as_view(), name='user-me'),

]

