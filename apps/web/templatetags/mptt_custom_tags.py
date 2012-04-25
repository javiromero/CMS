"""
Template tags for working with lists of model instances which represent
trees.
"""
from django import template
from django.db.models import get_model
from django.db.models.fields import FieldDoesNotExist
from django.utils.encoding import force_unicode
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext as _

from mptt.utils import tree_item_iterator, drilldown_tree_for_node

register = template.Library()


### ITERATIVE TAGS

class FullTreeForModelActiveNode(template.Node):
    def __init__(self, model, context_var):
        self.model = model
        self.context_var = context_var

    def render(self, context):
        cls = get_model(*self.model.split('.'))
        if cls is None:
            raise template.TemplateSyntaxError(
                _('full_tree_for_model tag was given an invalid model: %s') % self.model
            )
        context[self.context_var] = cls._tree_manager.filter(es_activo=True)
        return ''
        
@register.tag
def full_tree_for_model_active(parser, token):
    """
    Populates a template variable with a ``QuerySet`` containing the
    full tree for a given model.

    Usage::

       {% full_tree_for_model [model] as [varname] %}

    The model is specified in ``[appname].[modelname]`` format.

    Example::

       {% full_tree_for_model tests.Genre as genres %}

    """
    bits = token.contents.split()
    if len(bits) != 4:
        raise template.TemplateSyntaxError(_('%s tag requires three arguments') % bits[0])
    if bits[2] != 'as':
        raise template.TemplateSyntaxError(_("second argument to %s tag must be 'as'") % bits[0])
    return FullTreeForModelActiveNode(bits[1], bits[3])