"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os
import cx_Oracle


cx_Oracle.init_oracle_client(lib_dir=os.getenv('LD_LIBRARY_PATH'))

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings.production')

application = get_wsgi_application()
