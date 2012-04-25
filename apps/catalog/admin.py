# -*- coding: utf-8 -*-

'''
    Javier Romero Blanco
    javi.azuaga@gmail.com
    http://barrabarra.es
    ©2010
'''

from django.conf import settings
from django.contrib import admin
from django.contrib.contenttypes import generic
from django.utils.translation import ugettext_lazy as _
from catalog.forms import *
from catalog.models import *
from metatags.models import Metatag
from feincms.admin import editor
from sorl.thumbnail import default
from sorl.thumbnail.admin import AdminImageMixin

ADMIN_THUMBS_SIZE = '60x60'

class ModelAdmin(AdminImageMixin, admin.ModelAdmin):
    pass

class TabularInline(AdminImageMixin, admin.TabularInline):
    pass
    
class MetatagInline(generic.GenericStackedInline):
    model = Metatag
    extra = 0
    max_num = 1
    verbose_name = _(u'Metaetiquetas SEO')


class ConfigAdmin(admin.ModelAdmin):
    form = ConfigModelForm
    list_display = ('eslogan', 'productos_por_fila', 'destacados_por_fila', 'recomendados_por_fila', 'superventas_por_fila', 'dias_recientes', 'impuestos_incluidos', 'envio_gratis_desde', 'actualizado_el')
    
    fieldsets = [
        (None, { 'fields': ['eslogan',]}),
        (_(u'Presentación'), { 'fields': ['productos_por_fila', 'destacados_por_fila', 'recomendados_por_fila', 'superventas_por_fila', 'dias_recientes']}),
        (_(u'Impuestos'), { 'fields': ['impuestos_incluidos']}),
        (_(u'Envío'), { 'fields': ['envio_gratis_desde']}),
    ]
    
    inlines = [
        MetatagInline,
    ]
    
    class Media:
       js = ('js/tiny_mce/tiny_mce.js',
             'js/editores.js')

admin.site.register(Config, ConfigAdmin)


class CategoryAdmin(editor.TreeEditor):
    form = CategoryAdminForm
    # sets up values for how admin site lists category
    list_display = ('nombre', 'es_activo', 'en_menu', 'en_cabeza', 'en_pie', 'created_at_short', 'updated_at_short',)
    list_display_links = ('nombre',)
    ordering = ['parent', 'lft', 'nombre']
    search_fields = ['nombre', 'descripcion']

    # sets up slug to be generated from category name
    prepopulated_fields = {'slug' : ('nombre',)}
    
    fieldsets = [
        (None, { 'fields': [('nombre','slug', 'es_activo'), 'parent', 'marca']}),
        (_(u'Contenido'), { 'fields': ['imagen', 'resumen', 'descripcion']}),
        ('Posiciones', {
                        'classes': ('collapse',),
                        #'fields': ['orden', ('en_menu', 'menu_nom'), ('en_cabeza', 'cabeza_nom'), ('en_pie', 'pie_nom')]
                        'fields': [('en_menu', 'menu_nom'), ('en_cabeza', 'cabeza_nom'), ('en_pie', 'pie_nom')]
                       }),

    ]
    
    inlines = [
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

admin.site.register(Category, CategoryAdmin)


class BrandAdmin(editor.TreeEditor):
    list_display = ('nombre', 'es_activo', 'orden', 'created_at_short', 'updated_at_short',)
    list_display_links = ('nombre',)
    list_per_page = 20
    ordering = ['parent', 'lft', 'nombre'] 
    prepopulated_fields = {'slug' : ('nombre',)}

    inlines = [
        MetatagInline,
    ]

    def created_at_short(self, obj):
        return obj.created_at.strftime('%d %b %Y %H:%M')
    created_at_short.short_description = _(u'Creado el')
    created_at_short.admin_order_field='creado_el'

    def updated_at_short(self, obj):
        return obj.updated_at.strftime('%d %b %Y %H:%M')
    updated_at_short.short_description = _(u'Actualizado el')
    updated_at_short.admin_order_field='actualizado_el'

    class Media:
       js = ('js/tiny_mce/tiny_mce.js',
             'js/editores.js')

admin.site.register(Brand, BrandAdmin)


class ProductPriceInline(admin.StackedInline):
    #formset = RequireOneFormSet
    model = ProductPrice
    verbose_name = _(u'Precios')
    extra = 0


class ProductImageInline(TabularInline):
    model = ProductImage
    extra = 0
    verbose_name = _(u'Imagen del producto')


class ProductVideoInline(admin.TabularInline):
    model = ProductVideo
    extra = 0
    verbose_name = _(u'Video del producto')


class ProductWeightAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}

admin.site.register(ProductWeight, ProductWeightAdmin)

class ProductTaxAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}
        
admin.site.register(ProductTax, ProductTaxAdmin)

class ProductAdmin(ModelAdmin):
    ## sets values for how the admin site lists your products
    list_display = ('img_thumb', 'nombre', 'marca', 'es_activo', 'sku', 'stock', 'es_pack', 'updated_at_short',) 
    list_filter = ('marca', 'categorias',)
    list_display_links = ('img_thumb', 'nombre',)
    list_per_page = 25
    ordering = ['-creado_el']
    prepopulated_fields = {'slug' : ('nombre',)}
    search_fields = ['nombre', 'categorias__nombre', 'marca__nombre', 'sku', 'referencia',]
    ## exclude = ('created_at', 'updated_at',)
    filter_horizontal = ('categorias','pack',)
    fieldsets = (
        (None, {
            'fields': ('nombre', 'slug', 'es_activo', 'marca', 'categorias')
        }),
        (_('Contenido'), {
            'fields': ('resumen', 'descripcion', )
        }),
        (_('Detalles'), {
            'fields': ( ('es_destacado', 'es_superventas', 'es_recomendado'), 'referencia','sku', 'stock', ('es_pack', 'pack'),  'orden', 'impuestos', )
        }),
        (_('Dimensiones'), {
            'fields': ( ('peso', 'peso_unidades'), ('alto', 'alto_unidades'), ('longitud', 'longitud_unidades'), ('ancho', 'ancho_unidades'), )
        }),
        
    )

    inlines = [
	MetatagInline,
        ProductImageInline,
        ProductVideoInline,
        ProductPriceInline,
    ]
    
    def updated_at_short(self, obj):
        return obj.updated_at.strftime('%d %b %Y %H:%M')
    updated_at_short.short_description = _(u'Actualizado el')
    updated_at_short.admin_order_field='actualizado_el'
    
    def img_thumb(self, obj):
        if obj.imagen:
            thumb = default.backend.get_thumbnail(obj.imagen.imagen.file, ADMIN_THUMBS_SIZE)
            return u'<img width="%s" src="%s" />' % (thumb.width, thumb.url)
        else:
            return "No Image" 
    img_thumb.short_description = 'Imagen'
    img_thumb.allow_tags = True
    
    class Media:
       js = ('js/tiny_mce/tiny_mce.js',
             'js/editores.js',
             'js/prevent-autosend.js')

admin.site.register(Product, ProductAdmin)
