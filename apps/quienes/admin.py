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
from quienes.models import *
from metatags.models import *
from django import forms
from django.forms.util import ErrorList

class MetatagInline(generic.GenericStackedInline):
    model = Metatag
    extra = 1
    max_num = 1
    verbose_name = "SEO"

class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'actualizado_el', 'creado_el',)
    prepopulated_fields = {'slug': ('nombre',)}
    search_fields = ('nombre',)
    ordering = ('nombre',)
    fieldsets = [
        (None, {'fields': ['nombre', 'slug', 'titulo','imagen', 'orden']}),
        ('Texto', {'fields': ['resumen', 'contenido']}),
    ]

    inlines = [
        MetatagInline,
    ]

    class Media:
        js = ('js/tiny_mce/tiny_mce.js',
              'js/editores.js')

class QuienesModelForm(forms.ModelForm):
    def clean(self):
        quienes = Quienes.objects.all()
        if quienes.exists() and not self.initial:
            self._errors.setdefault('__all__', ErrorList()).append("Ya existe una configuración para Quienes somos. Para hacer cambios edite la existente.")
        return self.cleaned_data

class QuienesAdmin(admin.ModelAdmin):
    form = QuienesModelForm
    list_display = ('titulo', 'actualizado_el', 'creado_el',)
    search_fields = ('titulo',)
    ordering = ('titulo',)
    fieldsets = [
        (None, {'fields': ['titulo','imagen']}),
        ('Texto', {'fields': ['resumen', 'contenido']}),
    ]

    inlines = [
        MetatagInline,
    ]

    class Media:
        js = ('js/tiny_mce/tiny_mce.js',
              'js/editores.js')

class EquipoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'actualizado_el', 'creado_el',)
    search_fields = ('nombre',)
    ordering = ('nombre',)
    fieldsets = [
        (None, {'fields': ['orden', 'nombre', 'titulo','departamento','direccion','imagen']}),
        ('Texto', {'fields': ['contenido']}),
    ]

    inlines = [
        MetatagInline,
    ]

    class Media:
        js = ('js/tiny_mce/tiny_mce.js',
              'js/editores.js')

admin.site.register(Quienes,QuienesAdmin)
admin.site.register(Departamento,DepartamentoAdmin)
admin.site.register(Equipo,EquipoAdmin)

