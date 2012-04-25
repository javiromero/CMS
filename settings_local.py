# Django settings for cerrajerosds project.

import os
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
BASE_DIR = os.path.realpath(os.path.dirname(__file__))

DEBUG = True
TEMPLATE_DEBUG = True
PREPEND_WWW = False
SEND_BROKEN_LINK_EMAILS = False

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'db.sqlite3',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}


SITE_ROOT = os.path.join(PROJECT_ROOT, 'site')
MEDIA_ROOT = os.path.join(SITE_ROOT, 'media')
STATIC_ROOT = os.path.join(SITE_ROOT, 'static')

#CACHES = {
    #'default': {
        #'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    #}
#}

MIDDLEWARE_CLASSES = (
    'django.middleware.gzip.GZipMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.redirects.middleware.RedirectFallbackMiddleware',
    'middleware.ip_proxy.SetRemoteAddrFromForwardedFor',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

INTERNAL_IPS = ('127.0.0.1',)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.redirects',
    'django.contrib.sitemaps',
    'mptt',
    'south',
    'sorl.thumbnail',
    'debug_toolbar',
    'banners',
    'catalog',
    'stats',
    'configuracion',
    'contact',
    'metatags',
    'quienes',
    'slider',
    'social',
    'testimonios',
    'web',
    'clientes',
    'proyectos',
    'newsletter',
    'feincms', #only to run collectstatic and find templates
)

# to launch fake mail server in localhost run:
# python -m smtpd -n -c DebuggingServer localhost:1025

EMAIL_SUBJECT_PREFIX='[LOCAL] '
EMAIL_HOST='localhost'
EMAIL_PORT='1025'