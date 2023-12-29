from django.urls import include, path
from .views import (
    RegisterUserView, 
    VerifyEmailView,
    SendEmailVerification, 
    UpdateProfileView, 
    resend_verification_email,
    PasswordResetView,
    SendPasswordResetLink,
    PasswordResetConfirmView
    )


urlpatterns = [
    path('sign-up/', RegisterUserView.as_view(), name='sign-up'),
    path('verify-email/', SendEmailVerification.as_view(), name='verify-email'),
    path('verify-email/check/', VerifyEmailView.as_view(), name='resend-verification-email'),
    path('verify-email/resend/', resend_verification_email, name='resend-verification-email'),
    path('update-profile/', UpdateProfileView.as_view(), name='update-profile'),
    path('reset-link/send/', SendPasswordResetLink.as_view(), name='reset-link'),
    path('reset-password-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password-reset-confirm'),
] 

