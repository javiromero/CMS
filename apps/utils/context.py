# -*- coding: utf-8 -*-
'''
    Javier Romero

    Desarrollado por Barrabarra
    web: http://barrabarra.es
    email: javi@barrabarra.es
    Fecha: 2011
'''

from django.conf import settings
from django.contrib.sites.models import Site
from django.core.cache import cache
from django.http import HttpResponseServerError

from configuracion.models import Configuracion
from catalog.models import Category
from contact.forms import ContactmeForm
from contact.models import ContactConfig
from web.models import Pagina
from banners.models import Banner
from social.models import RedSocial

if settings.DEBUG:
    CACHE_EXPIRES = 60 # cada minuto
else:
    CACHE_EXPIRES = 60 * 60 * 2 # cada 2 horas

def context(request):
    current_site = Site.objects.get_current()
    
    #marcas      = cache.get('marcas')
    #if marcas is None:
        #marcas	= Brand.objects.filter(is_active=True, parent=None).order_by('ordering')
        #cache.set('marcas', marcas, CACHE_EXPIRES)
    
    # Configuración general
    conf        = cache.get('conf')
    if conf is None:
        try:
            conf	= Configuracion.objects.get()
        except Configuracion.DoesNotExist: 
            return HttpResponseServerError(u'Debe <a href="/admin/configuracion/configuracion/add/">configurar el sitio</a> en la administración.')

        cache.set('conf', conf, CACHE_EXPIRES)

    # Formulario rápido
    form        = ContactmeForm(initial = {
                                        #'nombre'    : u'Pedro',
                                        #'telefono'  : u'999222555',
                                        #'email'     : u'usuario@correo.es',
                                        #'mensaje'   : u'Quiero presupuestos para varios proyectos',
                                        'nombre'    : u'Nombre',
                                        'telefono'  : u'Teléfono',
                                        'email'     : u'Correo Electrónico',
                                        'mensaje'   : u'Me gustaría saber más información acerca de...',
                               })

    ## Categorías de la tienda
    #try:
        #cat_shop= Category.objects.filter(es_activo=True, en_menu=True).order_by('tree_id')
    #except Category.DoesNotExist:
        #cat_shop= False

    # Páginas de categoría superior
    cat1        = cache.get('cat1')
    if cat1 is None:
        cat1    = Pagina.objects.filter(es_activo=True, en_menu=True, plantilla='web/categoria_1.html').order_by('tree_id')
        cache.set('cat1', cat1, CACHE_EXPIRES)
        
    # Páginas de categoría media
    cat2        = cache.get('cat2')
    if cat2 is None:
        cat2    = Pagina.objects.filter(es_activo=True, en_menu=True, plantilla='web/categoria_2.html').order_by('tree_id')
        cache.set('cat2', cat2, CACHE_EXPIRES)

    # Páginas de categoría inferior
    cat3        = cache.get('cat3')
    if cat3 is None:
        cat3    = Pagina.objects.filter(es_activo=True, en_menu=True, plantilla='web/categoria_3.html').order_by('tree_id')
        cache.set('cat3', cat3, CACHE_EXPIRES)
    
    # Páginas finales
    pag         = cache.get('pag')
    if pag is None:
        pag     = Pagina.objects.filter(es_activo=True, en_menu=True, plantilla='web/pagina.html').order_by('tree_id')
        cache.set('pag', pag, CACHE_EXPIRES)

    # Redes sociales
    social      = cache.get('social')
    if social is None:
        social  = RedSocial.objects.filter(es_activo=True).order_by('orden')
        cache.set('social', social, CACHE_EXPIRES)

    # Banners
    banners     = cache.get('banners')
    if banners is None:
        banners     = Banner.objects.filter(es_activo=True, posicion="Id").order_by('orden')
        cache.set('banners', banners, CACHE_EXPIRES)
        
    pie = Pagina.objects.filter(es_activo=True, en_pie=True)
	

    try:
        contact = ContactConfig.objects.get()
    except:
        contact = False
    
    return {
        'site'          : current_site,
        'conf'          : conf,
        'pie'           : pie,
        
        # Menu izquierda
        'cat1'          : cat1,
        'cat2'          : cat2,
        'cat3'          : cat3,
        'pag'           : pag,

        # Elementos derecha
        'quick_form'    : form,
        'social'        : social,
        'banners'       : banners,
        'contact'       : contact,
    }