"""
WSGI config for devsearch project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# Set the DJANGO_SETTINGS_MODULE environment variable to point to your settings file.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'devsearch.settings')

# Get the Django application instance.
application = get_wsgi_application()

