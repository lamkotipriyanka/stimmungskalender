"""
Django settings for stimmungskalender project.

Generated by 'django-admin startproject' using Django 3.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
from datetime import timedelta
from pathlib import Path

import django_cache_url
from decouple import Csv, config
from dj_database_url import parse as db_url
from django.utils.translation import gettext_lazy as _

from stimmungskalender import tupled_list

MAX_LOG_FILE_SIZE = 20971520  # 20 MB

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config("SECRET_KEY")

DEBUG = config("DEBUG", default=False, cast=bool)

SESSION_COOKIE_SECURE = config("SESSION_COOKIE_SECURE", default=False, cast=bool)

ALLOWED_HOSTS = config("ALLOWED_HOSTS", cast=Csv())

CSRF_TRUSTED_ORIGINS = config(
    "CSRF_TRUSTED_ORIGINS", default="http://127.0.0.1", cast=Csv()
)

ADMINS = config("ADMINS", default=[], cast=Csv(post_process=tupled_list))

# Application definition

INSTALLED_APPS = [
    "web.apps.WebConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "bootstrap4",
    "rosetta",
    "django_registration",
    "rest_framework",
    "rest_framework.authtoken",
    "dj_rest_auth",
    "corsheaders",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "stimmungskalender.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "web.context_processors.lang",
                "web.context_processors.mood_colors",
                "web.context_processors.ng_sk",
            ],
        },
    },
]

WSGI_APPLICATION = "stimmungskalender.wsgi.application"

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = []

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "de-de"

TIME_ZONE = "Europe/Berlin"

USE_I18N = True

USE_L10N = True

USE_TZ = True

FIRST_DAY_OF_WEEK = 1

LANGUAGE_PATHS = [
    os.path.join(BASE_DIR, "locale"),  # base folder where manage.py resides
    os.path.join(BASE_DIR, "simple/locale"),  # app folder
]

LANGUAGES = [
    ("de-DE", _("German")),
    ("en-GB", _("English")),
]

# Rosetta Settings

ROSETTA_SHOW_AT_ADMIN_PANEL = True

ROSETTA_MESSAGES_PER_PAGE = 100

# Custom Django Settings
# https://docs.djangoproject.com/en/3.2/ref/settings/

CSRF_COOKIE_NAME = "sk_csrftoken"

SESSION_COOKIE_NAME = "sk_sessionid"

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = "/static/"

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    "default": config(
        "DATABASE_URL", default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}", cast=db_url
    )
}

CACHES = {"default": config("CACHE_URL", cast=django_cache_url.parse)}

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

BOOTSTRAP4 = {
    "css_url": "/static/css/bootstrap.min.css",
    "javascript_url": "/static/js/bootstrap.bundle.min.js",
    "jquery_url": "/static/js/jquery-3.6.0.min.js",
}

STATIC_ROOT = config("STATIC_ROOT", default=None)

LOG_FILE_PATH = config("LOG_FILE_PATH", default=BASE_DIR / "sk_debug.log")

LOGGING = {
    "version": 1,
    "disable_existing_loggers": True,
    "formatters": {
        "verbose": {
            "format": "[{levelname} {asctime} {module} {funcName}] {message}",
            "style": "{",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "verbose",
        },
        "log_file": {
            "level": "DEBUG",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": LOG_FILE_PATH,
            "formatter": "verbose",
            "backupCount": 10,
            "maxBytes": MAX_LOG_FILE_SIZE,
        },
        "mail_admins": {
            "level": "ERROR",
            "class": "django.utils.log.AdminEmailHandler",
        },
    },
    "loggers": {
        "django": {
            "handlers": config("SK_LOG_HANDLERS", default="console", cast=Csv()),
            "level": config("DJANGO_LOG_LEVEL", default="ERROR"),
        },
    },
}

# Django Registration

REGISTRATION_OPEN = config("REGISTRATION_OPEN", default=False, cast=bool)

LOGOUT_REDIRECT_URL = "/accounts/login/"

# Django Rest Framework

REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 7,
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "dj_rest_auth.jwt_auth.JWTCookieAuthentication",
    ),
    "DEFAULT_SCHEMA_CLASS": "rest_framework.schemas.coreapi.AutoSchema",
}

# django cors header

CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOWED_ORIGINS = config(
    "CORS_ALLOWED_ORIGINS", default="http://localhost", cast=Csv()
)

# dj rest auth

REST_USE_JWT = True
JWT_AUTH_COOKIE = "sk-auth-cookie"
JWT_AUTH_REFRESH_COOKIE = "sk-refresh-token"

# Simple JWT

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=5),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=5),
}

# SK Settings

DEFAULT_VIEW_MODE = "lines"

PER_PAGE = 25

SK_DATE_FORMAT = "%Y-%m-%d"  # To identify a week

NG_SK_ENABLED = config("NG_SK_ENABLED", default=False, cast=bool)

NG_SK_PATH = config("NG_SK_PATH", default="ng-sk")  # without leading or trailing slash
