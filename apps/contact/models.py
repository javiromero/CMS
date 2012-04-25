# -*- coding: utf-8 -*-
'''
    Javier Romero

    Desarrollado por Barrabarra
    web: http://barrabarra.es
    email: javi@barrabarra.es
    Fecha: 2011
'''

from django.conf import settings
from django.contrib.sites.models import Site
from django.contrib.sites.managers import CurrentSiteManager
from django.core.mail import EmailMultiAlternatives
from django.db import models
from django.db.models.signals import post_save
from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _

from catalog.models import Product
#from checkout.models import Order
from configuracion.models import Configuracion
from sorl.thumbnail import ImageField


class ContactConfig(models.Model):
    """
    Contact
    """
    contacto_titulo     = models.CharField(verbose_name=_(u'Título de la página de contacto'), max_length=120)
    contacto_texto      = models.TextField(verbose_name=_(u'Contenido'), blank=True,)
    contacto_analytics  = models.TextField(verbose_name=_(u'Analytics de la página de contacto'), blank=True,)
    contacto_imagen     = ImageField(_(u'Imagen de la página de contacto'), blank=True, upload_to='contacto')
    
    exito_titulo        = models.CharField(verbose_name=_(u'Título de la página de formulario enviado'), max_length=120)
    exito_texto         = models.TextField(verbose_name=_(u'Contenido'), blank=True,)
    exito_analytics     = models.TextField(verbose_name=_(u'Analytics de la página de formulario enviado'), blank=True,)
    exito_imagen        = ImageField(_(u'Imagen de la página de formulario enviado'), blank=True, upload_to='contacto')
    
    analytics_contacto  = models.TextField(verbose_name=_(u'Analytics del botón de formulario de contacto completo'), blank=True,)
    analytics_contactame = models.TextField(verbose_name=_(u'Analytics del botón de formulario de contacto rápido'), blank=True,)
    
    creado_el           = models.DateTimeField(_(u'Creado el'), editable=False, auto_now_add=True)
    actualizado_el      = models.DateTimeField(_(u'Actualizado el'), editable=False, auto_now=True)
    
    class Meta:
        verbose_name = _(u'Configuración de contacto')
        verbose_name_plural = _(u'Configuración de contacto')


class NotificationEmail(models.Model):
    """
    Email addresses to be notified when contact forms are sent,
    editable on admin instead of putting them on the settings file
    """
    
    configuracion       = models.ForeignKey(ContactConfig, verbose_name=_(u'Configuración de contacto'))
    email               = models.EmailField(verbose_name=_(u'Correo Electrónico'))
    
    def __unicode__(self):
        return self.email


class Message(models.Model):

    # contact info
    fecha       = models.DateTimeField(auto_now_add=True)
    ip          = models.IPAddressField(_(u'IP'))
    
    nombre      = models.CharField(_(u'Nombre'), max_length=150)
    email       = models.EmailField(_(u'Email'), max_length=150)
    telefono    = models.CharField(_(u'Teléfono'), max_length=9, null = True, blank = True)
    mensaje     = models.TextField(_(u'Mensaje'), max_length=256, null = True, blank = True)
    condiciones = models.BooleanField(_(u'Condiciones aceptadas'), default=False)
       
    class Meta:
        ordering = ['-fecha',]
        verbose_name = _(u'Mensaje recibido')
        verbose_name_plural = _(u'Mensajes recibidos')

    def save(self, *args, **kwargs):
        #current_site    = Site.objects.get_current()
        #config          = Configuracion.objects.get(id=1)
        #subject         = render_to_string('contact/emails/contact-subject.txt', {'message': self, 'site_name': current_site.name})
        #text_content    = render_to_string('contact/emails/contact-body-text.txt', {'message': self, 'current_site': current_site })
        #html_content    = render_to_string('contact/emails/contact-body-html.html', {'message': self,'current_site': current_site })

        #sender          = 'no-responder@%s' % current_site.domain
        #recipients      = [self.email,]
        #cco             = [n.email for n in config.notificationemail_set.all()]
    
        ## mail bonito a visitante con copia a managers
        #msg = EmailMultiAlternatives(subject, text_content, sender, recipients, bcc=cco)
        #msg.attach_alternative(html_content, "text/html")
        #msg.send()

        super(Message, self).save(*args, **kwargs) # Call the "real" save() method.

    def __unicode__(self):
        return _(u'Mensaje de %(name)s el %(date)s') % {'name': self.name, 'date': self.date}


class Response(models.Model):
    fecha       = models.DateTimeField(auto_now_add=True)
    nombre      = models.CharField(_(u'Nombre'), max_length=150)
    email       = models.EmailField(_(u'Email'), max_length=150)
    asunto      = models.CharField(_(u'Asunto'), max_length=150)
    mensaje     = models.TextField(_(u'Mensaje'), max_length=256, null = True, blank = True)  
    adjunto     = models.FileField(_(u'Adjunto'), upload_to='contact/response', blank=True, null=True)

    def __unicode__(self):
        return _(u'Mensaje para %(name)s (%(email)s)') % {'name': self.nombre, 'email': self.email}
    
    # Enviar el email tras guardar el fichero
    def save(self, *args, **kwargs):
        super(Response, self).save(*args, **kwargs) # Call the "real" save() method.
        #if self.pk == None:
        current_site    = Site.objects.get_current()
        config          = Configuracion.objects.get(id=1)
        subject         = render_to_string('contact/emails/response-subject.txt', {'response': self, 'site_name': current_site.name})
        text_content    = render_to_string('contact/emails/response-body-text.txt', {'response': self, 'current_site': current_site })
        html_content    = render_to_string('contact/emails/response-body-html.html', {'response': self,'current_site': current_site })
        
        sender      = 'no-responder@%s' % current_site.domain
        recipients  = [self.email,]
        cco         = [n.email for n in config.notificationemail_set.all()]
        
        # mail bonito a dirección y cco a managers
        msg = EmailMultiAlternatives(subject, text_content, sender, recipients, bcc=cco)
        msg.attach_alternative(html_content, "text/html")
        if self.file:
            msg.attach_file("%s/%s" % (settings.MEDIA_ROOT, self.file.name))
        msg.send()


    class Meta:
        verbose_name = _(u'Mensaje enviado')
        verbose_name_plural = _(u'Mensajes enviados')
