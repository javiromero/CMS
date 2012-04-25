# -*- coding: utf-8 -*-
from django.template import Library, Node
from web.models import *

register = Library()

class LatestContentNode(Node):
    def __init__(self, model_pk, num, varname):
        self.model_pk, self.num, self.varname = model_pk, num, varname
        self.filtro = Seccion.objects.get(pk=self.model_pk)

    def render(self, context):
        context['output'] = self.filtro
        try:
            context[self.varname] = Pagina._default_manager.filter(seccion=self.filtro, status='p')[:self.num]
            return ''
        except  Pagina.DoesNotExist:
            context[self.varname] = ""
            return ''

def get_latest(parser, token):
    bits = token.contents.split()
    if len(bits) != 5:
        raise TemplateSyntaxError, "get_latest tag takes exactly four arguments"
    if bits[3] != 'as':
        raise TemplateSyntaxError, "third argument to get_latest tag must be 'as'"
    return LatestContentNode(bits[1], bits[2], bits[4])

get_latest = register.tag(get_latest)


'''
http://www.b-list.org/weblog/2006/jun/07/django-tips-write-better-template-tags/

Ejemplo de uso en la plantilla

{% get_latest 1 5 as recent_entrantes %}
1 = id de la Sección
5 = número de elementos a mostrar

'''