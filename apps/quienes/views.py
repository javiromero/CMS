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
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django import template
from django.template import RequestContext, Template, loader
from django.template.loader import render_to_string
from django.core.mail import send_mail, BadHeaderError
from quienes.models import *
from metatags.models import Metatag
from proyectos.models import Proyecto
from clientes.models import Cliente
from configuracion.models import Configuracion

#template.add_to_builtins('web.templatetags.activo')
##template.add_to_builtins('web.templatetags.LinksPie')
#template.add_to_builtins('web.templatetags.inclusion_tag')
#template.add_to_builtins('configuracion.templatetags.conf_tags')
#template.add_to_builtins('social.templatetags.red_social')


def departamentos(request, slug):
    '''
    Vista de detalle
    '''

    try:
        f = Departamento.objects.get(slug_dep=slug)
        l = f.equipo_set.all().order_by('orden')
        mark_type = ContentType.objects.get_for_model(f)
        c = Metatag.objects.filter(content_type__pk=mark_type.id, object_id=f.id)
        return render_to_response("quienes/departament_detail.html",
					{'object': f,
					'equipos': l,
					'c': c,
					},
					context_instance = RequestContext(request))
    except Seccion.DoesNotExist:
        raise Http404


def quienes(request):
    """ Mapa web con enlaces a todas las páginas públicas """

    equipos = Equipo.objects.filter(es_activo=True).order_by('orden')
    
    try:
        quienes = Quienes.objects.get()
    except:
        quienes = None

    return render_to_response("quienes/quienes.html",
                                {
                                    'equipos': equipos,
                                    'object': quienes,
                                },
                                context_instance = RequestContext(request))


