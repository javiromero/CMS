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
from sorl.thumbnail import ImageField

class RedSocial(models.Model):
    """
    Redes sociales
    """
    nombre      = models.CharField(verbose_name=_(u'título'), max_length=120, help_text=_(u'Título'))
    enlace      = models.URLField(verbose_name=_(u'URL'), verify_exists=False, null=True, blank=True, help_text=_(u'Enlace que se quiera añadir a la diapostiva'))
    enlace_analytics = models.CharField(verbose_name=_(u'Analytics URL'), max_length=256, null=True, blank=True, help_text=_(u'Código Analytics del enlace. 256 caracteres máx.'))
    orden       = models.IntegerField(_(u'Orden'), default=0, help_text=_(u'Orden en el que se mostrará'))
    imagen      = ImageField(_(u'Icono de la red social'), upload_to='social')
    
    es_activo   = models.BooleanField(_(u'Activo'), default=True, help_text=_(u'Determina si se muestra en el sitio'))
    creado_el           = models.DateTimeField(_(u'Creado el'), editable=False, auto_now_add=True)
    actualizado_el      = models.DateTimeField(_(u'Actualizado el'), editable=False, auto_now=True)

    def __unicode__(self):
        return self.nombre
    
    class Meta:
        verbose_name = _(u'Red social')
        verbose_name_plural = _(u'Redes sociales')
        ordering = ['orden',]
