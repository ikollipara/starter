"""
urls.py
{{ cookiecutter.author_name }} <{{ cookiecutter.author_email }}>

Main Url Configuration
"""

from django import conf
from django import urls
from django.conf.urls import static
from django.contrib import admin

urlpatterns = [
    urls.path("admin/", admin.site.urls),
    *static.static(conf.settings.STATIC_URL, document_root=conf.settings.STATIC_ROOT),
    *static.static(conf.settings.MEDIA_URL, document_root=conf.settings.MEDIA_ROOT),
]

if conf.settings.DEBUG:
    {%- if cookiecutter.debug_toolbar %}from debug_toolbar import toolbar{% endif %}

    urlpatterns.append(
        urls.path("__reload__/", urls.include("django_browser_reload.urls"))
    )
    {%- if cookiecutter.debug_toolbar %}urlpatterns += toolbar.debug_toolbar_urls(){% endif %}
