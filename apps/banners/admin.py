# To change this template, choose Tools | Templates
# and open the template in the editor.

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from banners.models import *
from metatags.models import *
from sorl.thumbnail import default
from sorl.thumbnail.admin import AdminImageMixin

ADMIN_THUMBS_SIZE = '60x60'

class ModelAdmin(AdminImageMixin, admin.ModelAdmin):
    pass

class BannerAdmin(ModelAdmin):
    list_display = ('img_thumb', 'nombre', 'posicion', 'es_activo', 'actualizado_el', 'creado_el')
    list_display_links = ('img_thumb', 'nombre',)

    class Media:
        js = ('js/tiny_mce/tiny_mce.js',
              'js/editores.js')
              
    def img_thumb(self, obj):
        if obj.imagen:
            thumb = default.backend.get_thumbnail(obj.imagen.file, ADMIN_THUMBS_SIZE)
            return u'<img width="%s" src="%s" />' % (thumb.width, thumb.url)
        else:
            return "No Image" 
    img_thumb.short_description = 'Banner'
    img_thumb.allow_tags = True
    
admin.site.register(Banner,BannerAdmin)
