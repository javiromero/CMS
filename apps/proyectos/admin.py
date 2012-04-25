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
from django.contrib.contenttypes import generic
from proyectos.models import *
from metatags.models import *

class MetatagInline(generic.GenericStackedInline):
    model = Metatag
    extra = 1
    max_num = 1
    verbose_name = "SEO"

class ProyectoImage_Inline(admin.TabularInline):
    model = ProyectoImage
    extra = 1
    max_num = 1
    exclude = ['orden']
    verbose_name = "Captura"

class ProyectoAdmin(admin.ModelAdmin):

    list_display = ('nombre', 'es_activo', 'actualizado_el', 'creado_el',)
    prepopulated_fields = {'slug_proy': ('nombre',)}
    search_fields = ('nombre',)
    ordering = ('nombre',)

    fieldsets = [
        (None, {'fields': ['nombre', 'slug_proy', 'titulo', 'es_activo']}),
        ('Datos', {'fields': ['realizado_para', 'categorias']}),
        ('Texto', {'fields': ['contenido']}),
    ]

    inlines = [
        ProyectoImage_Inline,
        MetatagInline,
    ]

    class Media:
        js = ('js/tiny_mce/tiny_mce.js',
              'js/editores.js')

admin.site.register(Proyecto, ProyectoAdmin)