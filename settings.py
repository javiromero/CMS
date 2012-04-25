# -*- coding: utf-8 -*-
'''
    Javier Romero

    Desarrollado por //Barrabarra
    w: http://barrabarra.es
    m: javi@barrabarra.es
    Fecha: 2011
'''

import os
import sys
gettext = lambda s: s

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
SITE_ROOT = os.path.join(PROJECT_ROOT, 'site')
sys.path.insert(0, os.path.join(PROJECT_ROOT, "apps"))

ADMINS = (
     (u'YOU', 'YOU@YOURSELF.COM'),
)

MANAGERS = ADMINS


TIME_ZONE = 'Europe/Madrid'
LANGUAGE_CODE = 'es'
LANGUAGES = (
              ('es', u'Español'),
              ('en', u'English'),
            )

SITE_ID = 1
USE_I18N = True
USE_L10N = True

MEDIA_URL = '/media/'
STATIC_URL = '/static/'
ADMIN_MEDIA_PREFIX = '/static/admin/'

STATICFILES_DIRS = (
    os.path.join(SITE_ROOT, 'collect_static'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #'django.contrib.staticfiles.finders.DefaultStorageFinder',
    #'compressor.finders.CompressorFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'YOUR VERY SECRECT KEY'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

# Context Processors
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.auth',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.request',
    'utils.context.context',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.gzip.GZipMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.redirects.middleware.RedirectFallbackMiddleware',
    'middleware.ip_proxy.SetRemoteAddrFromForwardedFor',
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    os.path.join(SITE_ROOT, 'templates'),
)

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

WEB_TEMPLATES = (
    ('web/categoria_1.html', u'Categoría Sup'),
    ('web/categoria_2.html', u'Categoría Media'),
    ('web/categoria_3.html', u'Categoría Inf'),
    ('web/seccion.html', u'Sección'),
    ('web/pagina.html', u'Página'),
    ('web/estatica.html', u'Estática'),
    ('web/listado.html', u'Listado'),
    ('web/mapaweb.html', u'Mapa Web'),
    ('web/error.html', u'Página Error'),
)
    
# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

NEWSLETTER_OPTIN_MESSAGE = "Se ha inscrito correctamente."
NEWSLETTER_OPTOUT_MESSAGE = "Se ha eliminado correctamente."

try:
   from settings_local import *
except ImportError, e:
   pass

try:
   from settings_server import *
except ImportError, e:
   pass


if DEBUG:
    TEMPLATE_CONTEXT_PROCESSORS += ('django.core.context_processors.debug',)
if USE_I18N:
    TEMPLATE_CONTEXT_PROCESSORS += ('django.core.context_processors.i18n',)
