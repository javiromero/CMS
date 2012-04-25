# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _
from sorl.thumbnail import ImageField
from django.contrib.contenttypes.models import ContentType

# Create your models here.
class Banner(models.Model):
    GENDER_CHOICES = (
        ('Id', 'Banner Index'),
        ('In', 'Banner Interior'),
    )
    
    nombre      = models.CharField(verbose_name=_(u'Nombre'), max_length=60, help_text=_(u'Nombre - Max 60'))
    subtitulo   = models.CharField(verbose_name=_(u'Subtítulo'), max_length=120, help_text=_(u'Subtítulo - Max 120'))
    
    contenido   = models.TextField(verbose_name=_(u'Contenido'), help_text=_(u'Contenido'), blank=True)
    posicion    = models.CharField(verbose_name=_(u'Posición'), max_length=2, choices=GENDER_CHOICES, help_text=_(u'Lugar donde aparecerá el banner'))
    imagen      = ImageField(verbose_name=_(u'Imagen'), upload_to='banners', blank=True, help_text=_(u'Dimensiones de Imagen Banner Index: AAAxBBB - Dimensiones de Imagen Banner Lateral: ancho m&aacute;ximo AAApx'))
    url         = models.URLField(verbose_name=_(u'URL'), verify_exists=False, blank=True, null=True,help_text=_(u'URL del banner'))
    orden       = models.IntegerField(_(u'Orden'), default=0, help_text=_(u'Orden en el que se mostrará'))

    es_activo   = models.BooleanField(verbose_name=_(u'Activo'), default=True, help_text=_("Determina si se muestra en el sitio"))
    creado_el           = models.DateTimeField(_(u'Creado el'), editable=False, auto_now_add=True)
    actualizado_el      = models.DateTimeField(_(u'Actualizado el'), editable=False, auto_now=True)

    real_type   = models.ForeignKey(ContentType, editable=False, null=True)
    
    class Meta:
        verbose_name = _(u'Banner')
        verbose_name_plural = _(u'Banners')
        ordering = ['orden',]

    def save(self, *args, **kwargs):
        if not self.id:
            self.real_type = self._get_real_type()
        super(Banner, self).save(*args, **kwargs)

    def _get_real_type(self):
        return ContentType.objects.get_for_model(type(self))

    def __unicode__(self):
        return u"%s en %s" % (self.nombre, self.get_posicion_display())
