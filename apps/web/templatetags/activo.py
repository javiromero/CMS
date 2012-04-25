# coding=UTF-8
from django import template
from web.models import *

register = template.Library()
@register.filter
def pintar_menu(request, pattern):
        clase = ""
        if request.slug_secc == pattern:
            clase = "abierta"
        else:
            clase = pattern
        html = '<ul class="submenu '+clase+'">'
        secciones = Pagina.objects.filter(seccion=request.id).order_by('orden')
        for item in secciones:
            html += "<li class='p'><a href='/"+request.slug_secc+"/"+item.slug_pag+"' title='"+item.titulo+"'>" + item.titulo + "</a></li>"
        html+='</ul>'
        return html


