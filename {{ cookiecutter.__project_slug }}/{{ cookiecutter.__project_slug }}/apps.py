"""
apps.py
{{ cookiecutter.author_name }} <{{ cookiecutter.author_email }}>

{{ cookiecutter.__project_slug }} App Config
"""

from django.apps import AppConfig

class {{ cookiecutter.__project_app_class }}Config(AppConfig):
    name = "{{ cookiecutter.__project_slug }}"
