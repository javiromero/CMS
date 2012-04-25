# To change this template, choose Tools | Templates
# and open the template in the editor.

from slider.models import Slider
from django.contrib import admin
from sorl.thumbnail import default
from sorl.thumbnail.admin import AdminImageMixin

ADMIN_THUMBS_SIZE = '60x60'

class ModelAdmin(AdminImageMixin, admin.ModelAdmin):
    pass

class SliderAdmin(ModelAdmin):
    list_display = ('img_thumb', 'titulo', 'es_activo', 'actualizado_el', 'creado_el',)

              
    def img_thumb(self, obj):
        if obj.imagen:
            thumb = default.backend.get_thumbnail(obj.imagen.file, ADMIN_THUMBS_SIZE)
            return u'<img width="%s" src="%s" />' % (thumb.width, thumb.url)
        else:
            return "No Image" 
    img_thumb.short_description = 'Diapositiva'
    img_thumb.allow_tags = True
    
    class Media:
        js = ('js/tiny_mce/tiny_mce.js',
              'js/editores_diapositivas.js')

admin.site.register(Slider,SliderAdmin)
