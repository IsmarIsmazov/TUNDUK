from .base import *

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "corsheaders",
    'drf_yasg',
    'rest_framework.authtoken',
    'rest_framework_simplejwt',
    'rest_framework',
    'phonenumbers',
    'users',
    'catalog',
    'common',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_METHODS = (
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
)
CORS_ALLOW_HEADERS = ('content-disposition', 'accept-encoding',
                      'content-type', 'accept', 'origin', 'Authorization', 'access-control-allow-methods')

CORS_ALLOWED_ORIGINS = [
    "http://localhost:8080",
    "http://localhost:3080",
    "http://localhost:3000",
    "http://127.0.0.1:8000",
    "http://127.0.0.1:3000",
    "http://127.0.0.1:4040",
]
CORS_ORIGIN_WHITELIST = ['http://localhost:3000']
LOCAL_HOST = ['*']
ALLOWED_HOSTS = LOCAL_HOST + CORS_ALLOWED_ORIGINS

CSRF_TRUSTED_ORIGINS = ["https://5bee-109-201-165-30.ngrok-free.app"]
