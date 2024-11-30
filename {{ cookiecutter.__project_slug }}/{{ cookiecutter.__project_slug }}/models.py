"""
models.py
{{ cookiecutter.author_name }} <{{ cookiecutter.author_email }}>

{{ cookiecutter.__project_slug }} Models
"""

from django.contrib.auth import models as auth_models


class User(auth_models.AbstractUser):
    """Custom User Model."""

    pass
