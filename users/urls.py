from django.urls import path
from . import views
from .views import obtain_jwt_token, refresh_token


urlpatterns = [
    path('api/token/', obtain_jwt_token, name='token_obtain'),
    path('api/token/refresh/', refresh_token, name='token_refresh'),
]
