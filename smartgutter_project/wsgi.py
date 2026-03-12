"""
WSGI config for SmartGutter AI project.
"""
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'smartgutter_project.settings')

application = get_wsgi_application()
