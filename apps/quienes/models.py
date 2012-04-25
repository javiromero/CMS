# -*- coding: utf-8 -*-
# coding=UTF-8
'''
    Sempatiza

    Desarrollado por Lastchance SL
    web: www.lastchance.es
    email: jao@lastchance.es
    Fecha: 2010
'''

from django.db import models
from django.db.models import permalink
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes import generic
from django.contrib.sitemaps import Sitemap
from django.core.urlresolvers import reverse
from datetime import datetime
from metatags.models import *
from sorl.thumbnail import ImageField
from django.contrib.sitemaps import Sitemap
from django.core.urlresolvers import reverse


class Departamento(models.Model):
    """
    Departamento
    """
    titulo      = models.CharField(verbose_name=_(u'título'), max_length=120, unique=True, help_text=_(u'Título de la página. 120 caracteres máximo'))
    nombre      = models.CharField(verbose_name=_(u'nombre'), max_length=60, help_text=_(u'Nombre de la equipo. Debe ser corto'))
    slug        = models.SlugField(max_length=120, verbose_name=_(u'URL'), unique=True)
    
    orden       = models.PositiveSmallIntegerField(blank=True, null=True, help_text=_(u'Orden en el departamento. 0 es el primero por la izquierda'))
    resumen     = models.TextField(verbose_name=_(u'Resumen'), blank=True, help_text=_(u'Usado para portada'))
    imagen      = ImageField(upload_to='quienes/departamento', blank=True, null=True)
    contenido   = models.TextField(verbose_name=_(u'Texto'), blank=True)


    es_activo   = models.BooleanField(_(u'Activo'), default=True, help_text=_(u'Determina si se muestra en el sitio'))
    creado_el           = models.DateTimeField(_(u'Creado el'), editable=False, auto_now_add=True)
    actualizado_el      = models.DateTimeField(_(u'Actualizado el'), editable=False, auto_now=True)
    
    metatags = generic.GenericRelation('metatags.Metatag')

    class Meta:
        verbose_name = _(u'Departamento')
        verbose_name_plural = _(u'Departamento')

    def __unicode__(self):
        return self.nombre

    @models.permalink
    def get_absolute_url(self):
        return ('quienes.views.departamentos', [self.slug_dep])


class Quienes(models.Model):
    """
    Quienes
    """
    titulo      = models.CharField(verbose_name=_(u'título'), max_length=120, unique=True, help_text=_(u'Título de la página. 120 caracteres máximo'))
    resumen     = models.TextField(verbose_name=_(u'Resumen'), blank=True, help_text=_(u'Usado para portada'))
    imagen      = ImageField(upload_to='quienes/quienes', blank=True, null=True)
    contenido   = models.TextField(verbose_name=_(u'Texto'), blank=True,)

    es_activo   = models.BooleanField(_(u'Activo'), default=True, help_text=_(u'Determina si se muestra en el sitio'))
    creado_el           = models.DateTimeField(_(u'Creado el'), editable=False, auto_now_add=True)
    actualizado_el      = models.DateTimeField(_(u'Actualizado el'), editable=False, auto_now=True)
    
    metatags = generic.GenericRelation('metatags.Metatag')

    class Meta:
        verbose_name = _(u'Configuración de Quiénes somos')
        verbose_name_plural = _(u'Configuración de Quiénes somos')


class Equipo(models.Model):
    """
    Equipo
    """
    titulo      = models.CharField(verbose_name=_(u'título'), max_length=120, help_text=_(u'Título de la equipo. 120 caracteres máximo'))
    nombre      = models.CharField(verbose_name=_(u'nombre'), max_length=60, help_text=_(u'Nombre de la equipo. Debe ser corto'))
    departamento= models.ForeignKey('Departamento')
    direccion   = models.URLField(verify_exists=False, blank=True, null=True,help_text=_(u'Linked in URL del enlace'))
    
    orden       = models.PositiveSmallIntegerField(blank=True, null=True, help_text=_(u'Orden en el equipo. 0 es el primero por la izquierda'))
    contenido   = models.TextField(verbose_name=_(u'Texto'), blank=True,)
    imagen      = ImageField(upload_to='quienes/equipo', blank=True, null=True)

    es_activo   = models.BooleanField(_(u'Activo'), default=True, help_text=_(u'Determina si se muestra en el sitio'))
    creado_el           = models.DateTimeField(_(u'Creado el'), editable=False, auto_now_add=True)
    actualizado_el      = models.DateTimeField(_(u'Actualizado el'), editable=False, auto_now=True)
    
    metatags = generic.GenericRelation('metatags.Metatag')

    class Meta:
        verbose_name = _(u'Equipo')
        verbose_name_plural = _(u'Equipo')

        
