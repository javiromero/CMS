# -*- coding: utf-8 -*-
# coding=UTF-8
from django.template import Library, Node
from social.models import *

register = Library()

def social():
    soc = SocialMedia.objects.filter(status=True).order_by('nombre')[:3]
    return {'object': soc}

register.inclusion_tag('social.html')(social)