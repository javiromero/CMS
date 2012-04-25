# -*- coding: utf-8 -*-

'''
    Javier Romero Blanco
    javi.azuaga@gmail.com
    http://barrabarra.es
    ©2010
'''


from django import template
from django.conf import settings
from cart import cart_functions
from catalog.models import Config, Category
import datetime


register = template.Library()

# Cart item count gets cached so we don hit the db on every page load
@register.inclusion_tag("tags/cart_box.html")
def cart_box(request):
    cart_item_count = cart_functions.get_cart_total_items(request)
    cart_items = cart_functions.get_cart_items(request)
    cart_subtotal = cart_functions.cart_subtotal(request)
    
    # steps for the shopping progress bar
    progress = {'/pago/':1, '/pago/datos-de-envio/':2, '/pago/tipo-de-envio/':2, '/pago/revisar-y-pagar/':3,}
    for p in progress:
	if p == request.path:
	  current = progress[p]

    # if current isn't defined, set it to one
    try:
	current
    except NameError:
	current = 0

    return {
	'cart_item_count': cart_item_count,
	'cart_items': cart_items,
	'cart_subtotal': cart_subtotal,
	'progress': current,
	'MEDIA_URL': settings.MEDIA_URL,
    }

"""
# Wi'll do this also with the category's menu
@register.inclusion_tag("tags/category_list.html")
def category_list(request_path):
    main_categories = Category.objects.filter(is_active=True).filter(parent__isnull=True)
    return {
        'main_categories': main_categories,
        'request_path': request_path
    }
"""

# Product list
@register.inclusion_tag("tags/product_list_one.html")
def product_list_one(products, header_text):
    return {
        'products': products,
        'header_text': header_text
    }

# Product list
@register.inclusion_tag("tags/product_list_two.html")
def product_list_two(products, header_text):
    return {
        'products': products,
        'header_text': header_text
    }

# Product list
@register.inclusion_tag("tags/product_list_four.html")
def product_list_four(products, header_text):
    return {
        'products': products,
        'header_text': header_text
    }

# Content for the footer
@register.inclusion_tag("tags/footer.html")
def footer_links():
    try:
	conf_list = Config.on_site.get()
    except  Config.DoesNotExist:
	conf_list = ''
	
    social_media = SocialMedia.objects.filter(status=True)
    date = datetime.datetime.now()
    
    return {
	'date': date,
	'conf_list': conf_list,
	'social_media': social_media,
        
        'footer_sections': Section.footer.all(),
        'footer_pages': Page.objects.filter(is_active=True, on_footer=True),
        'footer_links': Link.objects.filter(is_active=True, on_footer=True),
	}
    
# To check current url in the navigation tab
@register.simple_tag
def active(request, pattern):
    import re

    if re.search(pattern, request.path):
        return 'active'
    return ''

# To check current url in the navigation tab and mark select option as selected
# Used in the filter by brand select, to keep the selected option marked
@register.simple_tag
def selected_path(request, pattern):
    import re

    if re.search(pattern, request.path):
        return 'selected="selected"'
    return ''

# To check current url in the navigation tab and mark select option as selected
# Used in order by select to keep the selected option marked
@register.simple_tag
def selected_get(request, pattern):
    import re

    if re.search(pattern, request.GET.get('orden', '')):
        return 'selected="selected"'
    return ''

# To print the correct ammount of tabulations in the brand selects
# Used in the filter by brand select, to correctly anidate children
@register.simple_tag
def tabulate_select(counter):
    char = ''
    for i in range(counter):
	char = char + ' ◦ '

    return char
