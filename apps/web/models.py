# -*- coding: utf-8 -*-
# coding=UTF-8
'''
    Sempatiza

    Desarrollado por Lastchance SL
    web: www.lastchance.es
    email: jao@lastchance.es
    Fecha: 2010
'''

from django.conf import settings
from django.core.cache import cache
from django.db import models
from django.db.models import permalink
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes import generic
from django.contrib.sitemaps import Sitemap
from django.core.urlresolvers import reverse
from metatags.models import *
from datetime import datetime
from sorl.thumbnail import ImageField
import mptt


class HomePage(models.Model):
    """
    Portada
    """
    titulo      = models.CharField(verbose_name=_(u'Subtítulo (h2)'), max_length=120, unique=True, help_text=_(u'Subtítulo de la página de portada. 120 caracteres máximo'))
    contenido   = models.TextField(verbose_name=_(u'Contenido'), help_text=_(u'Contenido detallado'), blank=True)
    
    es_activo   = models.BooleanField(_(u'Activo'), default=True, help_text=_(u'Determina si se muestra en el sitio'))
    creado_el           = models.DateTimeField(_(u'Creado el'), editable=False, auto_now_add=True)
    actualizado_el      = models.DateTimeField(_(u'Actualizado el'), editable=False, auto_now=True)

    metatags    = generic.GenericRelation('metatags.Metatag')

    class Meta:
        verbose_name = _(u'Portada')
        verbose_name_plural = _(u'Portada')

    def __unicode__(self):
       return u"Portada %s" % self.titulo
      

class Pagina(models.Model):
    """
    Paginas
    """

    nombre      = models.CharField(verbose_name=_(u'Nombre (h1)'), max_length=60, unique=False, help_text=_(u'Nombre de la página. Debe ser corto'))
    titulo      = models.CharField(verbose_name=_(u'Subtítulo (h2)'), max_length=120, unique=False, help_text=_(u'Subtítulo de la página. 120 caracteres máximo'))
    slug        = models.SlugField(_('Slug'), max_length=255, help_text=_(u'Valor único para la ruta a la página. Creado a partir del nombre.'))

    resumen     = models.TextField(verbose_name=_(u'Resumen'), help_text=_(u'Resumen de la página, utilizado como entradilla'))
    contenido   = models.TextField(verbose_name=_(u'Contenido'), help_text=_(u'Contenido completo de la página'))
    plantilla   = models.CharField(verbose_name=_(u'Plantilla'), max_length=256, choices=settings.WEB_TEMPLATES, help_text=_(u'Plantilla que empleará esta página'))
    
    boton_nombre= models.CharField(verbose_name=_(u'Nombre del botón'), max_length=255, blank=True, help_text=_(u'Nombre del botón para la página con plantilla Página'))
    boton_enlace= models.URLField(verbose_name=_(u'Enlace del botón'), blank=True, verify_exists=False, help_text=_(u'Enlace del botón de la página con plantilla Página'))
    
    en_menu     = models.BooleanField(_(u'En menu'), default=False)
    menu_nom    = models.CharField(_(u'Nombre en menú'), max_length=255, blank=True, null=True)
    en_cabeza   = models.BooleanField(_(u'En cabecera'), default=False)
    cabeza_nom  = models.CharField(_(u'Nombre en cabecera'), max_length=255, blank=True, null=True)
    en_pie      = models.BooleanField(_(u'En pie'), default=False)
    pie_nom     = models.CharField(_(u'Nombre en pie'), max_length=255, blank=True, null=True)
    
    es_activo   = models.BooleanField(_(u'Activo'), default=True, help_text=_(u'Determina si se muestra en el sitio'))
    creado_el           = models.DateTimeField(_(u'Creado el'), editable=False, auto_now_add=True)
    actualizado_el      = models.DateTimeField(_(u'Actualizado el'), editable=False, auto_now=True)
    
    metatags    = generic.GenericRelation('metatags.Metatag')
    parent      = models.ForeignKey('self', verbose_name=_(u'Padre'), blank=True, null=True, related_name='children')
    
    PAGE_URL_KEY        = "page_%d"
    _complete_slug      = None # caché de instancia
    
    def _get_mainImage(self):
        img = False
        try:
            img = self.images.all().order_by('-orden')[0]
        except:
            pass
        
        return img

    main_image = property(_get_mainImage)

    def _get_gallery(self):
        gal = False
        if self.images.all().count() < 2:
	    gal = False
        else:
            gal = self.images.all().order_by('-orden')
        return gal

    gallery = property(_get_gallery)
    
    def hijos(self):
        return self.children.filter(es_activo=True).order_by('lft')
        
    def menu_hijos(self):
        return self.children.filter(es_activo=True, en_menu=True).order_by('lft')

    def cabeza_hijos(self):
        return self.children.filter(es_activo=True, en_cabeza=True).order_by('lft')
        
    def pie_hijos(self):
        return self.children.filter(es_activo=True, en_pie=True).order_by('lft')

    def get_titulo(self):
        return self.titulo if self.titulo else self.nombre
        
    def menu_nombre(self):
        return self.menu_nom if self.menu_nom else self.nombre

    def cabeza_nombre(self):
        return self.cabeza_nom if self.cabeza_nom else self.nombre
        
    def pie_nombre(self):
        return self.pie_nom if self.pie_nom else self.nombre
    
    
    def __unicode__(self):
       return self.nombre

    def get_complete_slug(self):
        """Return the complete slug of this category by concatenating
        all parent's slugs."""
        
        if self._complete_slug:
            return self._complete_slug
        self._complete_slug = cache.get(self.PAGE_URL_KEY % (self.id))
        if self._complete_slug:
            return self._complete_slug

        url = self.slug
        
        for ancestor in self.get_ancestors(ascending=True):
            url = ancestor.slug + u'/' + url

        cache.set(self.PAGE_URL_KEY % (self.id), url)
        self._complete_slug = url
        
        return url

    @models.permalink
    def get_absolute_url(self):
        return ('page', (), {'path': self.get_complete_slug() })

    class Meta:
        verbose_name = _(u'Página')
        verbose_name_plural = _(u'Páginas')
        #ordering = ['parent__id', 'lft', 'nombre']
        
    def get_children(self):
        return self.get_children().filter(es_activo=True)
        
# Don't register the Pagina model twice.
try:
    mptt.register(Pagina)
except mptt.AlreadyRegistered:
    pass

    
class ImagenPagina(models.Model):
    pagina      = models.ForeignKey(Pagina, verbose_name=_(u'Página'), related_name='images')
    orden       = models.IntegerField(_(u'Orden'), default=0, help_text=_(u'Orden en el que se mostrará'))
    imagen      = ImageField(_(u'Imagen'), upload_to='web/pagina')
    titulo      = models.CharField(verbose_name=_(u'Título'), max_length=120, unique=True, help_text=_(u'Título de la imagen'))
    descripcion = models.TextField(_(u'Descripción'), help_text=_(u'Descripción de la imagen'), blank=True, null=True)

    class Meta:
        verbose_name = _(u'Imagen de página')
        verbose_name_plural = _(u'Imágenes de página')
        ordering = ['orden',]


class VideoPagina(models.Model):
    pagina      = models.ForeignKey(Pagina, verbose_name=_(u'Página'), related_name='videos')
    orden       = models.IntegerField(_(u'Orden'), default=0, help_text=_(u'Orden en el que se mostrará'))
    video       = models.CharField(verbose_name=_(u'Codigo del video'), max_length=256, help_text=_(u'ID del código del video'))
    titulo      = models.CharField(verbose_name=_(u'Título'), max_length=120, unique=True, help_text=_(u'Título del video'))
    descripcion = models.TextField(_(u'Descripción'), help_text=_(u'Descripción del video'), blank=True, null=True)

    class Meta:
        verbose_name = _(u'Video de página')
        verbose_name_plural = _(u'Videos de página')
        ordering = ['orden',]


class ArchivoPagina(models.Model):
    pagina      = models.ForeignKey(Pagina, verbose_name=_(u'Página'), related_name='files')
    orden       = models.IntegerField(_(u'Orden'), default=0, help_text=_(u'Orden en el que se mostrará'))
    archivo     = models.FileField(_(u'Archivo'), upload_to='web/pagina/archivos')
    titulo      = models.CharField(verbose_name=_(u'Título'), max_length=120, unique=True, help_text=_(u'Título de archivo'))
    descripcion = models.TextField(_(u'Descripción'), help_text=_(u'Descripción del archivo'), blank=True, null=True)

    class Meta:
        verbose_name = _(u'Archivo de página')
        verbose_name_plural = _(u'Archivos de página')
        ordering = ['orden',]
        
class NamedURLSitemap(Sitemap):
    """
    Given a set of named URLs, returns sitemap items for each.
    """
    def __init__(self, names):
        self.names = names

    def items(self):
        return self.names

    def changefreq(self, obj):
        return "weekly"

    def lastmod(self, obj):
        return datetime.now()

    def location(self, obj):
        return reverse(obj)
