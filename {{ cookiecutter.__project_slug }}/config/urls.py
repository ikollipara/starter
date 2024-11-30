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
    urls.path(
        conf.settings.STATIC_URL,
        *static.static(document_root=conf.settings.STATIC_ROOT),
    ),
    urls.path(
        conf.settings.MEDIA_URL,
        *static.static(document_root=conf.settings.MEDIA_ROOT),
    ),
]

if conf.settings.DEBUG:
    from debug_toolbar import toolbar

    urlpatterns.append(
        urls.path("__reload__/", urls.include("django_browser_reload.urls"))
    )
    urlpatterns += toolbar.debug_toolbar_urls()
