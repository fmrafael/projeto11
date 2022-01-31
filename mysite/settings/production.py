from mysite.settings.settings import *

DEBUG = False

ALLOWED_HOSTS = ['.digitimes.com.br']

#HTTPS settings
SECURE_SSL_REDIRECT = True
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

#HSTS settings - not in django deploy steps
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_PRELOAD = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL  = '/static/'

