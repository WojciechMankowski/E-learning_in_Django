"""
WSGI config for myshop project.
It exposes the WSGI callable as a module-level variable named ``application``.
For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os
import sys
from django.core.wsgi import get_wsgi_application
projekt_home = "/home/wojtek92/E-learning_in_Django"
if projekt_home not in sys.path:
    sys.path.insert(0, projekt_home)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'educa.settings')

application = get_wsgi_application()