"""
Django settings for {{ cookiecutter.project_name }} project.


For more information on this file, see
https://docs.djangoproject.com/en/stable/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/stable/ref/settings/
"""

import sys
from pathlib import Path

import environ

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env(DEBUG=(bool, False))

environ.Env.read_env(BASE_DIR / ".env")
if "test" in sys.argv:
    environ.Env.read_env(BASE_DIR / ".env.testing")


def devel(value):
    """Enable a dependency only in development.

    :param value: Any value.
    :type value:  typing.Any
    :return: Either the value or None
    :rtype: Any | None
    """
    if DEBUG:
        return value


def options(arr):
    """Filter a list to only include truthy values

    :param arr: An array of elements
    :type arr: typing.Iterable
    :return: A new list with only truthy values
    :rtype: list
    """

    return [el for el in arr if el]


SECRET_KEY = env("SECRET_KEY")
DEBUG = env("DEBUG")
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=[])
INSTALLED_APPS = options(
    [
        "{{ cookiecutter.__project_slug }}",
        "whitenoise.runserver_nostatic",
        "django_components",
        "django.contrib.admin",
        "django.contrib.auth",
        "allauth",
        "allauth.account",
        "huey.contrib.djhuey",
        devel("django_browser_reload"),
        devel("debug_toolbar"),
        "django_simple_factory",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.messages",
        "django.contrib.staticfiles",
    ]
)
MIDDLEWARE = options(
    [
        "django.middleware.security.SecurityMiddleware",
        "django.contrib.sessions.middleware.SessionMiddleware",
        "django.middleware.common.CommonMiddleware",
        "django.middleware.csrf.CsrfViewMiddleware",
        "django.contrib.auth.middleware.AuthenticationMiddleware",
        "django.contrib.messages.middleware.MessageMiddleware",
        "django.middleware.clickjacking.XFrameOptionsMiddleware",
        "allauth.account.middleware.AccountMiddleware",
        "whitenoise.middleware.WhiteNoiseMiddleware",
        devel("debug_toolbar.middleware.DebugToolbarMiddleware"),
        devel("django_browser_reload.middleware.BrowserReloadMiddleware"),
    ]
)
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
                        # Components loader
                        "django_components.template_loader.Loader",
                    ],
                )
            ],
        },
    },
]
INTERNAL_IPS = env.list("INTERNAL_IPS", [])
LOG_LEVEL = env("LOG_LEVEL")
EMAIL_BACKEND = env("EMAIL_BACKEND")
WSGI_APPLICATION = "config.wsgi.application"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
DATABASES = {"default": env.db()}
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True
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

STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "static"
STATICFILES_FINDERS = [
    # Default finders
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    # Django components
    "django_components.finders.ComponentsFileSystemFinder",
]
STORAGES = {
    # ...
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
    "default": {"BACKEND": "django.core.files.storage.FileSystemStorage"},
}

MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media"

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
AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",
    # `allauth` specific authentication methods, such as login by email
    "allauth.account.auth_backends.AuthenticationBackend",
]
AUTH_USER_MODEL = "{{ cookiecutter.__project_slug }}.User"


COMPONENTS = {"dirs": []}

ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_USERNAME_REAUIRED = False
ACCOUNT_EMAIL_REQUIRED = True

HUEY = {
    "huey_class": env("HUEY_WORKER_CLASS"),
    "name": env("HUEY_DBNAME"),
    "consumer": {
        "workers": env.int("HUEY_NUM_WORKERS", 1),
        "worker_type": env("HUEY_WORKER_TYPE"),
        "period": env.bool("HUEY_ENABLE_PERIODIC", True),
    },
}
