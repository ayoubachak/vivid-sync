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

    path('password-reset/<uidb64>/<token>/', views.password_reset, name='password-reset'),
    path('forgot-password/', views.forgot_password, name='forgot-password'),

    path('login/', views.login, name='login'),
    path('logout/', views.custom_logout, name='logout'),
    path('me/', views.me, name='me'),

    # main dashboard pages
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('create/', views.create_view, name='create'),
    path('inbox/', views.inbox_view, name='inbox'),
    path('feed/', views.feed_view, name='feed'),
    path('schedule/', views.schedule_view, name='feed'),
    path('analyze/', views.analyze_view, name='analyze'),
    path('ads/', views.ads_view, name='ads'),
    path('teams/', views.teams_view, name='teams'),
    path('accounts/', views.accounts_view, name='accounts'),
    path('settings/', views.general_settings, name='general-settings'),


    # Django templates
    path('', views.landing_page, name='landing_page'),
    path('tools/', views.tools_page, name='tools_page'),
    path('pricing/', views.pricing_page, name='pricing_page'),
    path('about/', views.about_page, name='about_page'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # to handle the media
