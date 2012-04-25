# To change this template, choose Tools | Templates
# and open the template in the editor.

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from testimonios.models import *
from metatags.models import *

class TestimoniosAdmin(admin.ModelAdmin):

    class Media:
        js = ('js/tiny_mce/tiny_mce.js',
              'js/editores.js')


admin.site.register(Testimonios, TestimoniosAdmin)
