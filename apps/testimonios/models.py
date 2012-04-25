# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes.models import ContentType
from catalog.models import Category
from web.models import Pagina
from sorl.thumbnail import ImageField

class TestimoniosConfig(models.Model):
    titulo     = models.CharField(verbose_name=_(u'Título de la página de testimonios'), max_length=120)
    texto      = models.TextField(verbose_name=_(u'Contenido para pagina de testimonios'), blank=True,)
    
    titulo_lat     = models.CharField(verbose_name=_(u'Título del lateral de testimonios'), max_length=120)
    texto_lat      = models.TextField(verbose_name=_(u'Resumen para laterales'), blank=True,)

    analytics  = models.TextField(verbose_name=_(u'Analytics de la página de testimonios'), blank=True,)
    imagen     = ImageField(_(u'Imagen de la página de testimonios'), upload_to='testimonios/config')    
    
    class Meta:
        verbose_name = _(u'Configuración de Testimonios')
        verbose_name_plural = _(u'Configuraciones de Testimonios')


class Testimonios(models.Model):
    nombre      = models.CharField(verbose_name=_(u'Nombre'), max_length=120, help_text=_(u'Nombre de la persona'))
    comentario  = models.TextField(verbose_name=_(u'Comentario'), max_length=220, help_text=_(u'Comentario, max 220 caracteres'))
    orden       = models.IntegerField(_(u'Orden'), default=0, help_text=_(u'Orden en el que se mostrará'))
    imagen      = ImageField(_(u'Imagen del testimonio'), upload_to='testimonios', blank=True, null=True)

    en_portada  = models.BooleanField(_(u'En portada'), default=True, help_text=_(u'Determina si se muestra en la portada'))
    es_activo   = models.BooleanField(_(u'Activo'), default=True, help_text=_(u'Determina si se muestra en el sitio'))
    creado_el           = models.DateTimeField(_(u'Creado el'), editable=False, auto_now_add=True)
    actualizado_el      = models.DateTimeField(_(u'Actualizado el'), editable=False, auto_now=True)
    
    categoria   = models.ForeignKey(Category, verbose_name=_(u'Categoría'), blank=True)
    pagina      = models.ForeignKey(Pagina, verbose_name=_(u'Página'), blank=True)
    
    class Meta:
        verbose_name = _(u'Testimonio')
        verbose_name_plural = _(u'Testimonios')
        ordering = ['orden',]

    def __unicode__(self):
        return u"%s" % self.nombre

    def en_portada(self):
        return self.filter(en_portada=True).order_by('orden')