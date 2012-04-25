# -*- coding: utf-8 -*-

'''
    Javier Romero Blanco
    javi.azuaga@gmail.com
    http://barrabarra.es
    ©2010
'''

from django.conf.urls.defaults import *

urlpatterns = patterns('catalog.views',
    url(r'^$',
        'index',
        {'template_name':'catalog/index.html'},
        name='catalog_home'),
        
    url(r'^anadidos-recientemente/pagina/(?P<page_number>\d+)/$',
        'latest_products',
        {'template_name':'catalog/latest-offers.html'},
        name='catalog_latests'),
    url(r'^anadidos-recientemente/$',
        'latest_products',
        {'template_name':'catalog/latest-offers.html'},
        name='catalog_latests'),
    url(r'^busqueda/$',
        'search_product',
        {'template_name':'catalog/search.html'},
        name='catalog_search'),
        
    url(r'^producto/(?P<product_slug>[-\w]+)/$',
        'show_product',
        {'template_name':'catalog/product.html'},
        name='catalog_product'),
        
    url(r'^resultados-de-la-busqueda/pagina/(?P<page_number>\d+)/$',
        'search_results',
        {'template_name':'catalog/search-results.html'},
        name='catalog_search_results'),
    url(r'^resultados-de-la-busqueda/$',
        'search_results',
        {'template_name':'catalog/search-results.html'},
        name='catalog_search_results'),
        
    url(r'^(?P<path>.*)/marca/(?P<brand_slug>[-\w]*)/pagina/(?P<page_number>\d+)/$',
        'show_category',
        {'template_name':'catalog/category.html'},
        name='catalog_brand'),
    url(r'^(?P<path>.*)/marca/(?P<brand_slug>[-\w]*)/$',
        'show_category',
        {'template_name':'catalog/category.html'},
        name='catalog_brand'),
    url(r'^(?P<path>.*)/pagina/(?P<page_number>\d+)/$',
        'show_category',
        {'template_name':'catalog/category.html'},
        name='catalog_category'),
    url(r'^(?P<path>.*)/$',
        'show_category',
        {'template_name':'catalog/category.html'},
        name='catalog_category'),
    )
