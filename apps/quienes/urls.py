# -*- coding: utf-8 -*-
# coding=UTF-8
'''
    Sempatiza

    Desarrollado por Lastchance SL
    web: www.lastchance.es
    email: jao@lastchance.es
    Fecha: 2010
'''

from django.conf.urls.defaults import *
from quienes.views import *
from proyectos.models import *
from django.conf import settings
from django.views.decorators.cache import cache_page
from django.contrib import sitemaps
from django.contrib.sitemaps import GenericSitemap

urlpatterns = patterns('',
    # TM SYStem:
    url(r'^$', 'quienes.views.quienes', name='quienes',),
    url(r'^(?P<slug>[^/]+)/$', 'quienes.views.departamentos', name='list_departamentos',),
)
