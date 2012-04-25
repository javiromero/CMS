# -*- coding: utf-8 -*-
#import sys
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes.models import ContentType
from django.conf import settings
from sorl.thumbnail import ImageField
#import string

# WTFITS!?
#sys.setrecursionlimit(1500)

class Slider(models.Model):
    imagen      = ImageField(_(u'Imagen'), upload_to='slider', blank=True, help_text=_(u'Dimensiones: AAAxBBB'))
    video       = models.TextField(verbose_name=_(u'Codigo Video'), blank=True)
    titulo      = models.CharField(verbose_name=_(u'Titulo'), max_length=120, null=True, blank=True, help_text=_(u'Título de la diapositiva. 120 caracteres máx.'))
    contenido   = models.TextField(verbose_name=_(u'Contenido'), blank=True, help_text=_(u'Texto del cuerpo de la diapositiva'))
    enlace      = models.URLField(verbose_name=_(u'URL'), verify_exists=False, null=True, blank=True, help_text=_(u'Enlace que se quiera añadir a la diapostiva'))
    enlace_texto        = models.CharField(verbose_name=_(u'Texto URL'), max_length=60, null=True, blank=True, help_text=_(u'Texto del enlace. 60 caracteres max.'))
    enlace_analytics    = models.CharField(verbose_name=_(u'Analytics URL'), max_length=256, null=True, blank=True, help_text=_(u'Código Analytics del enlace. 256 caracteres máx.'))
    orden       = models.IntegerField(_(u'Orden'), default=0, help_text=_(u'Orden en el que se mostrará'))

    es_activo   = models.BooleanField(_(u'Activo'), default=True, help_text=_(u'Determina si se muestra en el sitio'))
    creado_el           = models.DateTimeField(_(u'Creado el'), editable=False, auto_now_add=True)
    actualizado_el      = models.DateTimeField(_(u'Actualizado el'), editable=False, auto_now=True)

    real_type = models.ForeignKey(ContentType, editable=False, null=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.real_type = self._get_real_type()
        super(Slider, self).save(*args, **kwargs)

    def _get_real_type(self):
        return ContentType.objects.get_for_model(type(self))

    def __unicode__(self):
        return '%s' % self.titulo

    def get_title(self):
        return self.titulo

    def get_content(self):
        return self.contenido

    class Meta:
        verbose_name = _(u'Diapositiva')
        verbose_name_plural = _(u'Diapositivas')
        ordering = ['orden',]
