from django.urls import include, path
from .views import RegisterUserView, VerifyEmailView, ChangePasswordView, UpdateProfileView


urlpatterns = [
    path('sign-up/', RegisterUserView.as_view(), name='sign-up'),
    path('verify-email/', VerifyEmailView.as_view(), name='verify-email'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('update-profile/', UpdateProfileView.as_view(), name='update-profile'),

] 

