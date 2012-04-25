# -*- coding: utf-8 -*-
# coding=UTF-8
'''
    Sempatiza

    Desarrollado por Lastchance SL
    web: www.lastchance.es
    email: jao@lastchance.es
    Fecha: 2010
'''
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from clientes.models import *

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'es_activo', 'en_portada', 'actualizado_el', 'creado_el',)

admin.site.register(Cliente, ClienteAdmin)
