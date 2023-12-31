"""
URL configuration for vividsync project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from graphene_django.views import GraphQLView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import path
from django.views.static import serve
from django.conf import settings


schema_view = get_schema_view(
    openapi.Info(
        title="VividSync API",
        default_version='v1',
        description="Vivid API description",
        terms_of_service="https://www.ayoubachak.me/",
        contact=openapi.Contact(email="ayoub.achak01@gmail.com"),
        license=openapi.License(name="No Liscence"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # path('meta.json', serve, {'document_root': settings.STATIC_ROOT, 'path': 'meta.json'}),
    path('admin/', admin.site.urls),
    path('accounts/registration/', include('allauth.urls')),
    # Auth
    path('api/auth/', include('authentication.urls')),
    path('api/registration/', include('registration.urls')),
    # GraqphQL
    path('graphql/', GraphQLView.as_view(graphiql=True)),
    # Swagger
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    # Apps 
    path('api/analytics/', include('analytics.urls')),
    path('api/content/', include('content.urls')),
    path('api/social/', include('social.urls')),
    path('api/users/', include('users.urls')),
    path('api/organizations/', include('organizations.urls')),
    path('api/teams/', include('teams.urls')), 
    # Front End Application
    path('', include('frontend.urls')),

]

