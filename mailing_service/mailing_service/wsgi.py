"""
WSGI config for mailing_service project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mailing_service.settings')

application = get_wsgi_application()

from newsletters.tasks import start_scheduler

start_scheduler()




os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mailing_service.settings')
application = get_wsgi_application()
