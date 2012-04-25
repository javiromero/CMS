from django import template
from django.core.urlresolvers import reverse
from web.models import Pagina, Seccion
register = template.Library()

@register.simple_tag
def navactive(request, urls):
    if request.path in ( reverse(url) for url in urls.split() ):
        return "active"
    return ""

@register.simple_tag
def pintar_menu(seccion, request):
    seccion_grupo = Seccion.objects.get(slug_secc=seccion)
    paginas = Pagina.objects.filter(seccion=seccion_grupo.id).order_by('orden')
    html=""
    activo = ""
    entrada = 0
    for item in paginas:
        if request.path == "/"+seccion_grupo.slug_secc+"/"+item.slug_pag+"/":
            activo = "activo"
            entrada = 1
        html += "<li><a class='"+activo+"' href='/"+seccion_grupo.slug_secc+"/"+item.slug_pag+"' title='"+item.titulo+"'>" + item.titulo + "</a></li>"
        activo =""
    if entrada:
        html = "<ul class='submenu' style='display:block'>" + html + "</ul>"
    else:
        html = "<ul class='submenu'>" + html + "</ul>"
    return html
