from django.urls import include, path
from .views import RegisterUserView, VerifyEmailView,SendEmailVerification, ChangePasswordView, UpdateProfileView, resend_verification_email


urlpatterns = [
    path('sign-up/', RegisterUserView.as_view(), name='sign-up'),
    path('verify-email/', SendEmailVerification.as_view(), name='verify-email'),
     path('verify-email/check/', VerifyEmailView.as_view(), name='resend-verification-email'),
     path('verify-email/resend/', resend_verification_email, name='resend-verification-email'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('update-profile/', UpdateProfileView.as_view(), name='update-profile'),

] 

