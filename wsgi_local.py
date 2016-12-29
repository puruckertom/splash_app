"""
WSGI config for UberDjango project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""
import django.core.handlers.wsgi
import os

# Settings.py declaration
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

# entry point
app = django.core.handlers.wsgi.WSGIHandler()

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()