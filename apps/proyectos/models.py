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
from django.utils.translation import ugettext_lazy as _
from datetime import datetime
from django.db.models import permalink
from clientes.models import Cliente
from web.models import Pagina
from metatags.models import *
from sorl.thumbnail import ImageField

class Proyecto(models.Model):
    """
    Proyecto
    """

    nombre      = models.CharField(verbose_name=_(u'nombre'), max_length=60, unique=True, help_text=_(u'Nombre del proyecto. Debe ser corto'))
    titulo      = models.CharField(verbose_name=_(u'título'), max_length=120, unique=True, help_text=_(u'Título de la página. 120 caracteres máximo'))
    slug_proy   = models.SlugField(max_length=120, verbose_name=_(u'URL'), unique=True)
    contenido   = models.TextField(verbose_name=_(u'Contenido'), help_text=_(u'Descripción del proyecto'))
    realizado_para = models.ForeignKey('clientes.Cliente')
    categorias  = models.ManyToManyField('web.Pagina')

    es_activo   = models.BooleanField(_(u'Activo'), default=True, help_text=_(u'Determina si se muestra en el sitio'))
    creado_el           = models.DateTimeField(_(u'Creado el'), editable=False, auto_now_add=True)
    actualizado_el      = models.DateTimeField(_(u'Actualizado el'), editable=False, auto_now=True)

    metatags    = generic.GenericRelation('metatags.Metatag')

    class Meta:
        verbose_name = _('proyecto')
        verbose_name_plural = _('proyectos')

    def __unicode__(self):
        return self.nombre

    def _get_mainImage(self):
        img = False
        try:
            img = self.fotos.all().order_by('-orden')[0]
        except:
            pass
        
        return img

    main_image = property(_get_mainImage)

    @models.permalink
    def get_absolute_url(self):
        return ('web.views.proyecto_detail', [self.slug_proy])


class ProyectoImage(models.Model):
    """
    A picture of an item.  Can have many pictures associated with an item.
    Thumbnails are automatically created.
    """

    category    = models.ForeignKey(Proyecto, null=True, blank=True, related_name="fotos")
    imagen      = ImageField(upload_to='proyectos', blank=True, null=True)
    caption     = models.CharField(verbose_name=_(u"Descripción de la foto"), max_length=100, null=True, blank=True)
    orden       = models.IntegerField(verbose_name=_(u"Orden"), default=0)

    def _get_filename(self):
        if self.category:
            return '%s-%s' % (self.category.slug_proy, self.id)
        else:
            return 'default'
    _filename = property(_get_filename)

    def __unicode__(self):
        if self.category:
            return u"Imagen del proyecto %s" % self.category.nombre
        elif self.caption:
            return u"Imagen con descripción \"%s\"" % self.caption
        else:
            return u"%s" % self.imagen

    class Meta:
        ordering = ['category']
        verbose_name = _(u"Imagen de Proyecto")
        verbose_name_plural = _(u"Imágenes del Proyecto")