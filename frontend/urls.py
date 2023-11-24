from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # React Frontend
    path('test', views.index, name='index'),
    # Authentication
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.custom_logout, name='logout'),
    path('me/', views.me, name='me'),

    # Django templates
    path('', views.landing_page, name='landing_page'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # to handle the media
