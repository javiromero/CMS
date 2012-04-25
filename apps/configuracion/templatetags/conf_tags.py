# coding=UTF-8
from django.template import Library, Node
from django.db.models import get_model
from configuracion.models import *

register = Library()

class ConfDatos(Node):
    def render(self, context):
        context['conf_list'] = Configuracion.objects.get(pk=1)
        return ''

def conf_list(parser, token):
    """
    {% get_conf_list %}
    """
    return ConfDatos()

register.tag('get_conf_list', conf_list)