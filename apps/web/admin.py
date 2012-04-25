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
from web.models import *
from web.forms import HomePageModelForm, PaginaAdminForm
from metatags.models import *
from django import forms
from django.forms.util import ErrorList
from feincms.admin import editor

class MetatagInline(generic.GenericStackedInline):
    model = Metatag
    extra = 0
    max_num = 1
    verbose_name = _(u'Metaetiquetas SEO')


class HomeAdmin(admin.ModelAdmin):
    form = HomePageModelForm
    list_display = ('__unicode__', 'es_activo', 'actualizado_el', 'creado_el',)
    fieldsets = [
        (None, {'fields': ['titulo', 'es_activo']}),
        ('Texto', {'fields': [ 'contenido']}),
    ]

    inlines = [
        MetatagInline,
    ]

    class Media:
        js = ('js/tiny_mce/tiny_mce.js',
              'js/editores.js')


class ImagenPaginaInline(admin.TabularInline):
    model = ImagenPagina
    extra = 0
    verbose_name = _(u'Imagen de página')

class VideoPaginaInline(admin.TabularInline):
    model = VideoPagina
    extra = 0
    verbose_name = _(u'Video de página')

class ArchivoPaginaInline(admin.TabularInline):
    model = ArchivoPagina
    extra = 0
    verbose_name = _(u'Archivo de página')

class PaginaAdmin(editor.TreeEditor):
    form = PaginaAdminForm
    list_display = ('nombre', 'plantilla', 'es_activo', 'en_menu', 'en_cabeza', 'en_pie', 'created_at_short', 'updated_at_short',)
    list_display_links = ('nombre',)
    ordering = ['parent', 'lft', 'nombre']
    search_fields = ('nombre', 'titulo',)
    
    prepopulated_fields = {'slug': ('nombre',)}
    
    fieldsets = [
        (None, {'fields': [('nombre', 'titulo'), 'slug', 'plantilla', 'parent', 'es_activo',]}),
        ('Contenido', {'fields': ['resumen', 'contenido']}),
        ('Botón de página', {
                        'classes': ('collapse',),
                        'fields': ['boton_nombre', 'boton_enlace']
                       }),
        ('Posiciones', {
                        'classes': ('collapse',),
                        'fields': [('en_menu', 'menu_nom'), ('en_cabeza', 'cabeza_nom'), ('en_pie', 'pie_nom')]
                       }),
    ]

    inlines = [
	ImagenPaginaInline,
	VideoPaginaInline,
	ArchivoPaginaInline,
        MetatagInline,
    ]

    def created_at_short(self, obj):
        return obj.creado_el.strftime('%d %b %H:%M')
    created_at_short.short_description = _(u'Creado el')
    created_at_short.admin_order_field='creado_el'

    def updated_at_short(self, obj):
        return obj.actualizado_el.strftime('%d %b %H:%M')
    updated_at_short.short_description = _(u'Actualizado el')
    updated_at_short.admin_order_field='actualizado_el'
    
    class Media:
        js = ('js/tiny_mce/tiny_mce.js',
              'js/editores.js')


admin.site.register(HomePage, HomeAdmin)
admin.site.register(Pagina, PaginaAdmin)
