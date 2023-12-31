"""
Django settings for vividsync project.

Generated by 'django-admin startproject' using Django 4.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os
from dotenv import load_dotenv


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
DOTENV_PATH = BASE_DIR / '.env'
load_dotenv(
    dotenv_path=DOTENV_PATH, 
    verbose=True,
    override=True
)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')
SITE_ID = 1

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
APPEND_SLASH = True

ALLOWED_HOSTS=['*']
CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_WHITELIST = (
  'http://localhost:8000',
  'http://localhost:5173',
  'http://127.0.0.1:5173',
  'http://127.0.0.1:8000',
  'https://localhost:8000',
  'https://localhost:5173',
  'https://127.0.0.1:5173',
  'https://127.0.0.1:8000',
)
# CORS_ALLOWED_ORIGINS =[
#     "http://127.0.0.1:8000",
#     "http://localhost:8000",
#     "http://127.0.0.1:5173",
#     "http://localhost:5173",
# ]

# SMTP Setup
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.getenv('SMTP_EMAIL') # Your Gmail address
EMAIL_HOST_PASSWORD = os.getenv('SMTP_PASSWORD')    # Your Gmail password
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django_extensions', # for ssl testing
    'graphene_django',
    'vividql', # graphql app
    'drf_yasg', # swagger api docs
    'frontend', # frontend of the application
    # 'auth', # should handle the authentication
    # social media authentication
    'allauth', 
    'allauth.account', 
    'allauth.socialaccount', 
    'allauth.socialaccount.providers.google', 
    'allauth.socialaccount.providers.facebook', 
    'allauth.socialaccount.providers.twitter', 
    'allauth.socialaccount.providers.github', 
    # for cors
    'corsheaders', 
    # apps
    'users',
    'organizations',
    'teams',
    'content',
    'analytics',
    'social',
    'registration',
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # needed for cors
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # needed by allauth
    "allauth.account.middleware.AccountMiddleware",
    # needed by cors
]

ROOT_URLCONF = 'vividsync.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'frontend/templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.static',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # Needed by allauth
                'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'vividsync.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'frontend/static', 
    BASE_DIR / 'frontend/res',  
]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Media files
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Authentication
AUTH_USER_MODEL = 'users.VividUser'

AUTHENTICATION_BACKENDS = [
    # ... other authentication backends ...
    'django.contrib.auth.backends.ModelBackend',  # session based authentication backend
    'authentication.backends.JWTAuthenticationBackend', # for jwtauthentication backend
    # needed by allauth
    # 'allauth.account.auth_backends.AuthenticationBackend', # social medial authentication
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ],
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],
}

# Google Auth
GOOGLE_OAUTH2_CLIENT_ID = os.getenv('GOOGLE_OAUTH2_CLIENT_ID')
GOOGLE_OAUTH2_CLIENT_SECRET = os.getenv('GOOGLE_OAUTH2_CLIENT_SECRET')
GOOGLE_OAUTH2_PROJECT_ID = os.getenv('GOOGLE_OAUTH2_PROJECT_ID')
BASE_BACKEND_URL = os.getenv('BASE_BACKEND_URL', 'http://localhost:8000/')
# Github Auth
GITHUB_OAUTH2_CLIENT_ID = os.getenv('GITHUB_OAUTH2_CLIENT_ID')
GITHUB_OAUTH2_CLIENT_SECRET = os.getenv('GITHUB_OAUTH2_CLIENT_SECRET')
# Facebook Auth
FACEBOOK_OAUTH2_APP_ID = os.getenv('FACEBOOK_OAUTH2_APP_ID')
FACEBOOK_OAUTH2_APP_SECRET = os.getenv('FACEBOOK_OAUTH2_APP_SECRET')
# Instagram Auth
VIVIDSYNC_INSTAGRAM_APP_ID = os.getenv('VIVIDSYNC_INSTAGRAM_APP_ID')
VIVIDSYNC_INSTAGRAM_APP_SECRET = os.getenv('VIVIDSYNC_INSTAGRAM_APP_SECRET')
VIVIDSYNC_INSTAGRAM_APP_AUTH_INIT_URI = os.getenv('VIVIDSYNC_INSTAGRAM_APP_AUTH_INIT_URI')
VIVIDSYNC_INSTAGRAM_APP_REDIRECT_URI = os.getenv('VIVIDSYNC_INSTAGRAM_APP_REDIRECT_URI')

VIVIDSYNC_FACEBOOK_APP_ID = os.getenv('VIVIDSYNC_FACEBOOK_APP_ID')
VIVIDSYNC_FACEBOOK_APP_SECRET = os.getenv('VIVIDSYNC_FACEBOOK_APP_SECRET')
VIVIDSYNC_FACEBOOK_LOGIN_INSTAGRAM_REDIRECT_URI = os.getenv('VIVIDSYNC_FACEBOOK_LOGIN_INSTAGRAM_REDIRECT_URI')
VIVIDSYNC_FACEBOOK_LOGIN_INSTAGRAM_AUTH_INIT_URI = os.getenv('VIVIDSYNC_FACEBOOK_LOGIN_INSTAGRAM_AUTH_INIT_URI')

VIVIDSYNC_FACEBOOK_LOGIN_FACEBOOK_REDIRECT_URI = os.getenv('VIVIDSYNC_FACEBOOK_LOGIN_FACEBOOK_REDIRECT_URI')
VIVIDSYNC_FACEBOOK_LOGIN_FACEBOOK_AUTH_INIT_URI = os.getenv('VIVIDSYNC_FACEBOOK_LOGIN_FACEBOOK_AUTH_INIT_URI')

VIVIDSYNC_LINKEDIN_CLIENT_ID = os.getenv('VIVIDSYNC_LINKEDIN_CLIENT_ID')
VIVIDSYNC_LINKEDIN_CLIENT_SECRET = os.getenv('VIVIDSYNC_LINKEDIN_CLIENT_SECRET')
VIVIDSYNC_LINKEDIN_REDIRECT_URI = os.getenv('VIVIDSYNC_LINKEDIN_REDIRECT_URI')
VIVIDSYNC_LINKEDIN_AUTH_INIT_URI = os.getenv('VIVIDSYNC_LINKEDIN_AUTH_INIT_URI')


LOGIN_REDIRECT_URL="/me/"


# needed by allauth
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        # For each OAuth based provider, either add a ``SocialApp``
        # (``socialaccount`` app) containing the required client
        # credentials, or list them here:
        'APP': {
            'client_id': GOOGLE_OAUTH2_CLIENT_ID,
            'secret': GOOGLE_OAUTH2_CLIENT_SECRET,
        }
    },
    'github': {
        'APP': {
            'client_id': GITHUB_OAUTH2_CLIENT_ID,
            'secret': GITHUB_OAUTH2_CLIENT_SECRET,
        }
    },

}


# Graphql 
GRAPHENE = {
    'SCHEMA': 'vividql.schema.schema'  # Path to GraphQL schema
}

# Metadata
META_DATA = {
    "name": "Vivid Sync",
    "version": "1.0.0",
    "description": "Vivid Sync is a centered media platform where you can manage all your social media",
    "author": "Your Name",
    "email": "your.email@example.com",
    "license": "MIT",
    "dependencies": {
        "django": "3.2.10",
        "other_library": "1.2.3"
    },
    "keywords": [
        "django",
        "web",
        "application"
    ]
}
