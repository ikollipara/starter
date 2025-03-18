"""
Django settings for {{ cookiecutter.project_name }} project.


For more information on this file, see
https://docs.djangoproject.com/en/stable/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/stable/ref/settings/
"""

import sys
from pathlib import Path

import environs

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

env = environs.Env()

env.read_env(BASE_DIR / ".env")
if "test" in sys.argv:
    env.read_env(BASE_DIR / ".env.testing", override=True)


SECRET_KEY = env.str("SECRET_KEY")
DEBUG = env.bool("DEBUG", default=False)

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=[])

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    {% if cookiecutter.allauth %}"allauth", {% endif %}
    {% if cookiecutter.allauth %}"allauth.account", {% endif %}
    "django_browser_reload",
    "debug_toolbar",
    "django_simple_factory",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    {% if cookiecutter.allauth %}"allauth.account.middleware.AccountMiddleware",{% endif %}
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django_browser_reload.middleware.BrowserReloadMiddleware",
]

ROOT_URLCONF = "config.urls"
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
            "loaders": [
                (
                    "django.template.loaders.cached.Loader",
                    [
                        # Default Django loader
                        "django.template.loaders.filesystem.Loader",
                        # Inluding this is the same as APP_DIRS=True
                        "django.template.loaders.app_directories.Loader",
                    ],
                )
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

INTERNAL_IPS = env.list("INTERNAL_IPS", [])
LOG_LEVEL = env.str("LOG_LEVEL")

EMAIL_BACKEND = env.str("EMAIL_BACKEND")

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
DATABASES = {"default": env.dj_db_url("DATABASE_URL")}


AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"

USE_I18N = True
USE_TZ = True

# Static and Media

STATIC_URL = "static/"
STATICFILES_DIRS = [
    BASE_DIR / "static" / "dist",
    BASE_DIR / "static" / "public",
]
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_FINDERS = [
    # Default finders
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media"

# Django Rich

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {
        "require_debug_true": {
            "()": "django.utils.log.RequireDebugTrue",
        }
    },
    "formatters": {
        "rich": {"datefmt": "[%X]"},
    },
    "handlers": {
        "console": {
            "class": "rich.logging.RichHandler",
            "filters": ["require_debug_true"],
            "formatter": "rich",
            "level": "DEBUG",
            "rich_tracebacks": True,
            "tracebacks_show_locals": True,
        }
    },
    "loggers": {
        "django": {
            "handlers": [],
            "level": "INFO",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "INFO",
    },
}

TEST_RUNNER = "django_rich.test.RichRunner"

# Storages

STORAGES = {
    # ...
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
    "default": {"BACKEND": "django.core.files.storage.FileSystemStorage"},
}

{% if cookiecutter.allauth %}
# Django All Auth

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",
    # `allauth` specific authentication methods, such as login by email
    "allauth.account.auth_backends.AuthenticationBackend",
]

ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_USERNAME_REAUIRED = False
ACCOUNT_EMAIL_REQUIRED = True
{% endif %}
