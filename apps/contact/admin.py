# -*- coding: utf-8 -*-
'''
    Javier Romero

    Desarrollado por Barrabarra
    web: http://barrabarra.es
    email: javi@barrabarra.es
    Fecha: 2011
'''

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from contact.models import *
from contact.forms import *
from sorl.thumbnail import default
from sorl.thumbnail.admin import AdminImageMixin

ADMIN_THUMBS_SIZE = '60x60'

class ModelAdmin(AdminImageMixin, admin.ModelAdmin):
    pass


class NotificationEmailInline(admin.StackedInline):
    model       = NotificationEmail
    extra       = 1
    verbose_name = _(u'Correos electrónicos a los que notificar')


class ContactAdmin(ModelAdmin):
    form = ContactModelForm
    list_display = ('contacto_titulo', 'exito_titulo', 'actualizado_el', 'creado_el',)
    fieldsets = [
        (_(u'Página Contactar'), {'fields': ['contacto_titulo', 'contacto_texto', 'contacto_analytics', 'contacto_imagen']}),
        (_(u'Página Éxito'), {'fields': ['exito_titulo', 'exito_texto', 'exito_analytics', 'exito_imagen']}),
        (_(u'Formularios'), {'fields': ['analytics_contacto', 'analytics_contactame']}),
    ]

    inlines     = [
        NotificationEmailInline,
    ]
    
    class Media:
       js = ('js/tiny_mce/tiny_mce.js',
	     'js/editores_contacto.js') 

admin.site.register(ContactConfig, ContactAdmin)

class MessageAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'fecha',)
    ordering = ['-fecha']

admin.site.register(Message, MessageAdmin)

class ResponseAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'asunto', 'fecha')
    ordering = ['-fecha']
    
    class Media:
       js = ('js/tiny_mce/tiny_mce.js',
             'js/editores.js')

admin.site.register(Response, ResponseAdmin)