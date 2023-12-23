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
    path('terms-of-service/', views.terms_of_service, name='signup-verify-email'),
    
    path('login/', views.login, name='login'),
    path('logout/', views.custom_logout, name='logout'),
    path('me/', views.me, name='me'),

    # Django templates
    path('', views.landing_page, name='landing_page'),
    path('tools/', views.tools_page, name='tools_page'),
    path('pricing/', views.pricing_page, name='pricing_page'),
    path('about/', views.about_page, name='about_page'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # to handle the media
