# -*- coding: utf-8 -*-
'''
    Javier Romero Blanco
    javi.azuaga@gmail.com
    http://barrabarra.es
    ©2010
'''

from django.conf.urls.defaults import *
from django.utils.translation import ugettext_lazy as _
from contact.views import *
from django.conf import settings

SITE_ID = settings.SITE_ID


urlpatterns = patterns('',
                       url(r'^$',
                            contact_form,
                            {'template_name': 'contact/contact.html'},
                            name='contact'),
                       url(r'^gracias/$',
                            contact_form_sent,
                            {'template_name':'contact/thankyou.html'},
                            name='contact_sent'),
                       )
