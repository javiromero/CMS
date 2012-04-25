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
from django.contrib.contenttypes import generic
from metatags.models import *
from sorl.thumbnail import ImageField

class Configuracion(models.Model):
    """
    Datos para configuración del sitio
    """
    titulo      = models.CharField(verbose_name=_(u'título'), max_length=120, unique=True, help_text=_(u'Título de la web'))
    eslogan     = models.CharField(_(u'Eslogan'), blank=True, max_length=255, null=True, help_text=_(u'Eslogan de la web. 255 caracteres max.'))
    logo        = ImageField(_(u'Logo'), upload_to='configuracion')
    favicon     = ImageField(_(u'Favicon'), upload_to='configuracion')

    blog        = models.URLField(verify_exists=False, blank=True, null=True,help_text=_(u'URL del blog'))
    blog_rss    = models.URLField(verify_exists=False, blank=True, null=True,help_text=_(u'URL RSS del blog'))
    blog_entradas       = models.IntegerField(_('Entradas'), blank=True, null=True, default=5, help_text=_(u'El número de entradas del RSS que se mostrarán'))

    cat1_nombre = models.CharField(_(u'Menú superior'), default=_(u'Para los que saben lo que quieren...'), max_length=255, help_text=_(u'Nombre de la categoría superior del menú principal. 255 caracteres max.'))
    cat2_nombre = models.CharField(_(u'Menú medio'), default=_(u'Para los que buscan quien los ayude...'), max_length=255, help_text=_(u'Nombre de la categoría media del menú principal. 255 caracteres max.'))
    cat3_nombre = models.CharField(_(u'Menú inferior'), default=_(u'Para los que se bastan solos...'), max_length=255, help_text=_(u'Nombre de la categoría inferior del menú principal. 255 caracteres max.'))
    
    tiempo_diapositivas = models.IntegerField(_(u'Tiempo entre diapositivas'), default=5000, help_text=_(u'Tiempo en segundos entre cada diapositiva en milisegundos. 5000 milisegundos = 5 segundos por defecto.'))
    
    google_analytics    = models.TextField(verbose_name=_(u'Código de Analytics'), max_length=100, blank=True, null=True,)
    verificacion_webmaster = models.CharField(verbose_name=_(u'Código de webmasters'), max_length=100, blank=True, null=True,)

    creado_el           = models.DateTimeField(_(u'Creado el'), editable=False, auto_now_add=True)
    actualizado_el      = models.DateTimeField(_(u'Actualizado el'), editable=False, auto_now=True)

    metatags    = generic.GenericRelation('metatags.Metatag')
    
    def telefono(self):
        try:
            return self.contactdata_set.all()[0].telefono
        except:
            return False
        
    def movil(self):
        try:
            return self.contactdata_set.all()[0].movil
        except:
            return False
        
    def email(self):
        try:
            return self.contactdata_set.all()[0].email
        except:
            return False
        
    def direccion(self):
        try:
            return self.contactdata_set.all()[0].direccion
        except:
            return False

    def codigo_postal(self):
        try:
            return self.contactdata_set.all()[0].codigo_postal
        except:
            return False
        
    def ciudad(self):
        try:
            return self.contactdata_set.all()[0].ciudad
        except:
            return False

    class Meta:
        verbose_name = _(u'Datos de Configuración')
        verbose_name_plural = _(u'Datos de Configuración')


class ContactData(models.Model):
    configuracion       = models.ForeignKey(Configuracion, verbose_name=_(u'Configuración'))
    telefono    = models.CharField(verbose_name=_(u'teléfono'), max_length=12, blank=True, null=True,)
    movil       = models.CharField(verbose_name=_(u'móvil'), max_length=12, blank=True, null=True,)
    email       = models.EmailField(verbose_name=_(u'email de contacto'), blank=True, null=True,)
    direccion   = models.CharField(verbose_name=_(u'dirección'), max_length=100, blank=True, null=True,)
    codigo_postal       = models.CharField(verbose_name=_(u'código postal'), max_length=100, blank=True, null=True,)
    ciudad      = models.CharField(verbose_name=_(u'ciudad'), max_length=100, blank=True, null=True,)

    class Meta:
        verbose_name = _(u'Datos de contacto')
        verbose_name_plural = _(u'Datos de contacto')


class NotificationEmail(models.Model):
    """
    Email addresses to be notified when contact forms are sent,
    editable on admin instead of putting them on the settings file
    """
    
    configuracion       = models.ForeignKey(Configuracion, verbose_name=_(u'Configuración'))
    email               = models.EmailField(verbose_name=_(u'Correo Electrónico'))
    
    def __unicode__(self):
        return self.email