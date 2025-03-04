"""
ASGI config for backend project.
ASGI (Asynchronous Server Gateway Interface) configuration for the Django project.
This allows Django to handle asynchronous requests and WebSockets.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application

# Set the default Django settings module for the 'asgi' application.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

# Create an ASGI application instance.
application = get_asgi_application()
