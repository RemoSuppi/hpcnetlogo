"""
WSGI config for jobs_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

APACHE_CONFIGURATION = os.path.dirname(__file__)
PROJECT = os.path.dirname(APACHE_CONFIGURATION)
WORKSPACE = os.path.dirname(PROJECT)
sys.path.append(WORKSPACE)
sys.path.append(PROJECT)

MYPROJ = '/var/www/html/jobs_project/jobs_project'

# Add the path to 3rd party django application and to django itself.

sys.path.append(MYPROJ)
os.environ['DJANGO_SETTINGS_MODULE'] = 'jobs_project.settings'

application = get_wsgi_application()

