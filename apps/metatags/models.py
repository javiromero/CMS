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
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

ROBOTS_CHOICES = (
    ('0', 'index, follow'),
    ('1', 'noindex, follow'),
)

class Metatag(models.Model):
    """
    Meta Tags para SEO
    """
    robots      = models.CharField(max_length=2, choices=ROBOTS_CHOICES, default=0, verbose_name=_(u'meta robots'),help_text=_(u'Por defecto \"index, follow\"'))
    palabras_clave      = models.CharField(max_length=150, blank=True, null=True, verbose_name=_(u'meta keyword'), help_text=_(u'Palabras clave separadas por comas. Relacionado con el texto. Máx. 150 car.'))
    descripcion = models.CharField(max_length=150, blank=True, null=True, verbose_name=_(u'meta description'), help_text=_(u'Breve descripción. Relacionado con el texto. Máx. 150 car.'))
    titulo      = models.CharField(max_length=70, blank=True, null=True, verbose_name=_(u'meta titulo'), help_text=_(u'Titulo de la pagina. Máx. 70 car.'))
    content_type= models.ForeignKey(ContentType)
    object_id   = models.PositiveIntegerField()
    content_object      = generic.GenericForeignKey('content_type', 'object_id')

    def __unicode__(self):
       return self.palabras_clave
