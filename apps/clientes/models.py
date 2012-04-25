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

class Cliente(models.Model):
    """
    Clientes
    """

    nombre      = models.CharField(verbose_name=_(u'nombre'), max_length=120, help_text=_(u'Nombre del cliente'))

    logo        = ImageField(upload_to='clientes', blank=True, null=True)
    url         = models.URLField(verify_exists=False, blank=True, null=True,help_text=_(u'Web del cliente'))
    en_portada  = models.BooleanField(verbose_name=_(u'En portada'), default=False, help_text=_("Esto determina si el logo del cliente aparece en la portada"))

    es_activo   = models.BooleanField(_(u'Activo'), default=True, help_text=_(u'Determina si se muestra en el sitio'))
    creado_el           = models.DateTimeField(_(u'Creado el'), editable=False, auto_now_add=True)
    actualizado_el      = models.DateTimeField(_(u'Actualizado el'), editable=False, auto_now=True)

    def _get_filename(self):
        if self.nombre:
            return '%s-%s' % (self.nombre, self.id)
        else:
            return 'default'
    _filename = property(_get_filename)

    def __unicode__(self):
        if self.nombre:
            return self.nombre
        else:
            return u"%s" % self.logo

    class Meta:
        ordering = ['nombre']
        verbose_name = _(u"Cliente")