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
from django import forms
from django.contrib.contenttypes import generic
from configuracion.models import *
from metatags.models import *
from django.forms.util import ErrorList
from sorl.thumbnail import default
from sorl.thumbnail.admin import AdminImageMixin

ADMIN_THUMBS_SIZE = '60x60'

class ModelAdmin(AdminImageMixin, admin.ModelAdmin):
    pass

class MetatagInline(generic.GenericStackedInline):
    model = Metatag
    extra = 1
    max_num = 1
    verbose_name = "SEO"


class ContactDataInline(admin.StackedInline):
    model = ContactData
    extra = 1
    verbose_name = _(u'Datos de contacto')


class ConfiguracionModelForm(forms.ModelForm):
    def clean(self):
        if Configuracion.objects.count() > 1:
            self._errors.setdefault('__all__', ErrorList()).append("Ya existe una configuración. Para hacer cambios edite la existente.")
        return self.cleaned_data

class ConfiguracionAdmin(ModelAdmin):
    form = ConfiguracionModelForm
    list_display = ('logo_thumb', 'titulo', 'actualizado_el', 'creado_el',)
    list_display_links = ('logo_thumb', 'titulo',)
    ordering = ('titulo',)
    fieldsets = [
        (None, {'fields': ['titulo', 'eslogan', 'logo', 'favicon']}),
        ('Blog', {'fields': ['blog', 'blog_rss', 'blog_entradas']}),
        (u'Menú principal', {'fields': ['cat1_nombre', 'cat2_nombre', 'cat3_nombre']}),
        ('Diapositivas', {'fields': ['tiempo_diapositivas']}),
        ('Códigos', {'fields': ['google_analytics', 'verificacion_webmaster']}),
    ]

    inlines = [
        ContactDataInline,
        MetatagInline,
    ]
    
    def logo_thumb(self, obj):
        if obj.logo:
            thumb = default.backend.get_thumbnail(obj.logo.file, ADMIN_THUMBS_SIZE)
            return u'<img width="%s" src="%s" />' % (thumb.width, thumb.url)
        else:
            return "No Image" 
    logo_thumb.short_description = 'Logo'
    logo_thumb.allow_tags = True

admin.site.register(Configuracion, ConfiguracionAdmin)
