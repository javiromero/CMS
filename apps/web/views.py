# -*- coding: utf-8 -*-
# coding=UTF-8
'''
    Sempatiza

    Desarrollado por Lastchance SL
    web: www.lastchance.es
    email: jao@lastchance.es
    Fecha: 2010
'''

from django.conf import settings
from django.contrib.sites.models import Site
from django.core import urlresolvers
from django.http import HttpResponseRedirect, HttpResponse, Http404, HttpResponseServerError
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404, redirect
from django import template
from django.template import RequestContext, Template, loader
from django.template.loader import render_to_string
from django.core.mail import *
from web.models import *
from web.forms import *
from slider.models import *
from testimonios.models import *
from clientes.models import Cliente
from proyectos.models import Proyecto
from quienes.models import *
from banners.models import *
from metatags.models import Metatag
from configuracion.models import Configuracion
from social.models import RedSocial

from django.utils.translation import ugettext_lazy as _
from contact.forms import ContactmeForm

#template.add_to_builtins('web.templatetags.activo')
#template.add_to_builtins('web.templatetags.LinksPie')
#template.add_to_builtins('web.templatetags.inclusion_tag')
#template.add_to_builtins('configuracion.templatetags.conf_tags')
#template.add_to_builtins('social.templatetags.red_social')


def index(request):
    '''
        Vista para home
    '''

    if request.is_ajax:
        pass
        
    if request.POST:
        form    = ContactmeForm(request.POST)
        if form.is_valid():
            message     = form.save(commit=False)
            message.ip  = request.META['REMOTE_ADDR']
            message.save()
            
            try:
                url = request.POST['url']
            except:
                url = urlresolvers.reverse('index')
            return redirect(url)
    
    else:
        # Formulario de contacto rápido
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

    # Portada
    try:
        object  = HomePage.objects.get()
    except HomePage.DoesNotExist:
        return HttpResponseServerError(u'Debe <a href="/admin/web/homepage/add/">configurar una portada</a> en la administración.')

    # Metas de portada
    try:
        metas   = object.metatags.get()
    except Metatag.DoesNotExist:
        metas   = False

    # Diapositivas
    slides      = Slider.objects.filter(es_activo=True).order_by('orden')
    
    ## Categorías de la tienda
    #try:
        #cat_shop= Category.objects.filter(es_activo=True, en_menu=True).order_by('tree_id')
    #except Category.DoesNotExist:
        #cat_shop= False

    ## Páginas de sección
    #sec         = Pagina.objects.filter(es_activo=True, en_menu=True, plantilla='web/seccion.html').order_by('tree_id')

    ## Páginas de categoría
    #cat         = Pagina.objects.filter(es_activo=True, en_menu=True, plantilla='web/categoria.html').order_by('tree_id')
    
    ## Páginas finales
    #pag         = Pagina.objects.filter(es_activo=True, en_menu=True, plantilla='web/pagina.html').order_by('tree_id')
    
    ## Redes sociales
    #social      = RedSocial.objects.filter(es_activo=True).order_by('orden')

    ## Banners
    #banners     = Banner.objects.filter(es_activo=True, posicion="Id").order_by('orden')

    return render_to_response("web/index.html",
                            {
                            'object'    : object,
                            'metatags'  : metas,
                            'slides'    : slides,
                            'quick_form': form,
                            #'cat_shop'  : cat_shop,
                            #'cat'       : cat,
                            #'sec'       : sec,
                            #'pag'       : pag,
                            #'social'    : social,
                            #'banners'    : banners
                            },
                            context_instance = RequestContext(request))


def paginas(request, path):
    '''
    Vista de detalle
    '''
    
    path = path.rstrip("/") # eliminamos la barra más a la derecha si la hay
    if path.count("/") > 0:
        parent_slug = path.split("/")[-2] # si hay al menos uno es que hay un slug padre
    else:
        parent_slug = None # si no únicamente hay un slug
    slug = path.split("/")[-1]

    # para no confundir categorias con mismo slug y distinto padre
    if parent_slug:
        object = get_object_or_404(Pagina, slug=slug, parent__slug=parent_slug)
    else:
        object = get_object_or_404(Pagina, slug=slug, parent=None)
        
    try:
        metainfo = object.metatags.all()
    except:
        metainfo = ''

    # Añadir listado de páginas si es mapa web
    if object.plantilla == 'web/mapaweb.html':
        mapa    = Pagina.objects.filter(es_activo=True)
        pr_list = Proyecto.objects.filter(es_activo=True)
    else:
        mapa    = False
        pr_list = False

    return render_to_response(object.plantilla, {
            'object'    : object,
            'metas'     : metainfo,
            'mapa'      : mapa,
            'pr_list'   : pr_list,
           },
           context_instance = RequestContext(request))


def proyectos(request):
    '''
    Vista de listado de servicios
    '''

    object_list = Proyecto.objects.filter(es_activo=True)
    if not object_list.exists():
        return error_404(request)

    return render_to_response("web/proyecto_list.html",
                                {
                                'object_list'   : object_list,
                                },
                                context_instance = RequestContext(request))

def proyecto_detail(request, slug_proy):
    '''
    Vista de detalle
    '''
    
    object      = get_object_or_404(Proyecto, slug_proy__exact=slug_proy, es_activo=True)
        
    try:
        metainfo = object.metatags.all()
    except:
        metainfo = ''

    return render_to_response("web/proyecto_detail.html",
                                {
                                    'object'    : object,
                                    'metas'     : metainfo,
                                },
                                context_instance = RequestContext(request))

def clientes(request):
    '''
    Vista de listado de servicios
    '''

    object_list = Cliente.objects.filter(es_activo=True)
    if not object_list.exists():
        return error_404(request)

    return render_to_response("web/cliente_list.html",
                                {
                                    'object_list'   : object_list,
                                },
                                context_instance = RequestContext(request))


def error_404(request):
    return error(request, error_code=404)

def error_403(request):
    return error(request, error_code=403)

def error(request, error_code):
    # Errores personalizados
    try:
        object = Pagina.objects.get(plantilla='web/error.html', es_activo=True)
    except Pagina.DoesNotExist:
        return HttpResponseServerError(u'Debe <a href="/admin/web/pagina/add/">configurar una pagina de error</a> en la administración.')

    try:
        metainfo = object.metatags.all()
    except:
        metainfo = ''
        
    response = render_to_response(object.plantilla,
                            {
                            'object'    : object,
                            'metas'     : metainfo,
                            },
                            context_instance = RequestContext(request))

    response.status_code = error_code
    return response