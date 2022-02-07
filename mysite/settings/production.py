from mysite.settings.settings import *
import cx_Oracle

DEBUG = False

ALLOWED_HOSTS = ['.digitimes.com.br', '144.22.165.220', '127.0.0.1']

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



cx_Oracle.init_oracle_client(lib_dir=os.getenv('LD_LIBRARY_PATH'))


