from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # React Frontend
    path('test', views.index, name='index'),
    # Authentication
    path('signup/', views.signup, name='signup'),
    path('signup/verify-email/', views.verify_email, name='signup-verify-email'),
    path('terms-of-service/', views.terms_of_service, name='terms-of-service'),
    path('complete-profile/', views.complete_profile, name='complete-profile'),
    path('complete-profile/account-type/', views.setup_account_type, name='setup-account-type'),
    path('complete-profile/personal-info/', views.setup_personal_info, name='setup-personal-info'),
    path('complete-profile/last-steps/', views.last_steps, name='setup-last-steps'),
    path('complete-profile/congratulations/', views.congratulations, name='setup-congratulations'),

    path('login/', views.login, name='login'),
    path('logout/', views.custom_logout, name='logout'),
    path('me/', views.me, name='me'),

    # add a path to the dashboard
    path('dashboard/', views.dashboard, name='dashboard'),

    # Django templates
    path('', views.landing_page, name='landing_page'),
    path('tools/', views.tools_page, name='tools_page'),
    path('pricing/', views.pricing_page, name='pricing_page'),
    path('about/', views.about_page, name='about_page'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # to handle the media
