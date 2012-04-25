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
from social.models import *
from sorl.thumbnail import default
from sorl.thumbnail.admin import AdminImageMixin

ADMIN_THUMBS_SIZE = '60x60'

class ModelAdmin(AdminImageMixin, admin.ModelAdmin):
    pass

class RedSocialAdmin(ModelAdmin):
    list_display = ('img_thumb', 'nombre', 'es_activo', 'actualizado_el', 'creado_el',)
    list_display_links = ('img_thumb', 'nombre',)
    
    def img_thumb(self, obj):
        if obj.imagen:
            thumb = default.backend.get_thumbnail(obj.imagen.file, ADMIN_THUMBS_SIZE)
            return u'<img width="%s" src="%s" />' % (thumb.width, thumb.url)
        else:
            return "No Image" 
    img_thumb.short_description = 'Diapositiva'
    img_thumb.allow_tags = True

admin.site.register(RedSocial, RedSocialAdmin)