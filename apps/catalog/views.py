# -*- coding: utf-8 -*-

'''
    Javier Romero Blanco
    javi.azuaga@gmail.com
    http://barrabarra.es
    ©2011
'''

from django.db.models import Q
from django.conf import settings
from django.contrib import messages
from django.contrib.sites.models import Site
from django.contrib.syndication.views import Feed
from django.core import urlresolvers
from django.http import HttpResponseForbidden, HttpResponseGone
from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.template import RequestContext
from django.utils.translation import ugettext as _

from catalog.models import *
from stats import stats_functions
from utils.paginator import DiggPaginator, iround, InvalidPage
    
from operator import attrgetter
from datetime import date, timedelta

def index(request, template_name):

    context     = RequestContext(request)
    current_site= context['site']
    conf        = context['conf']
    page_title  = conf.site_name
    
    featured    = Product.featured.all()[:conf.featured_per_row]
    bestsellers = Product.bestseller.all().order_by('?')[:conf.bestsellers_per_row]
    recommended = Product.recommended.all().order_by('?')[:conf.recommended_per_row]
    try:
        metainfo = conf.metatags.all()
    except:
        metainfo = '' 
    
    # set cookie to allow add products to the cart
    request.session.set_test_cookie()
    
    if current_site.id == 2:
	object_list	= list()
	offers  	= Product.objects.filter(is_active=True, stock__gt=0, saving_site2__gt=0).order_by('?')[:8]
    else:
	offers = False
    
    return render_to_response(template_name, 
        {
          'page_title'  : page_title,
          'featured'    : featured,
          'bestsellers' : bestsellers,
          'recommended' : recommended,
          'offers'      : offers,
        },
        context_instance = context)

#@cache_page(60 * 60 * 2) # cada 2 horas
def show_category(request, path, template_name, brand_slug=None, page_number=1):

    if request.POST:
        if brand_slug and brand_slug != 'all':
            url = urlresolvers.reverse('catalog_brand', kwargs={'path': path, 'brand_slug': brand_slug})
        else:
            url = urlresolvers.reverse('catalog_category', kwargs={'path': path})
        return redirect(url)

    # reutilizamos variables del contexto
    context = RequestContext(request)
    current_site = context['site']
    
    try:
        brand = Brand.objects.get(slug=brand_slug)
    except:
        brand = None

    path = path.rstrip("/") # eliminamos la barra más a la derecha si la hay
    if path.count("/") > 0:
	parent_slug = path.split("/")[-2] # si hay al menos uno es que hay un slug padre
    else:
	parent_slug = None # si no únicamente hay un slug
    slug = path.split("/")[-1]

    # para no confundir categorias con mismo slug y distinto padre
    if parent_slug:
	object = get_object_or_404(Category, slug=slug, parent__slug=parent_slug)
    else:
	object = get_object_or_404(Category, slug=slug, parent=None)


    order_slug = request.GET.get('orden', None)
    ORDERING = {
      'nombre-a-z' : {'key':'nombre', 'reverse':''},
      'nombre-z-a' : {'key':'nombre', 'reverse':'-'},
    }
    if order_slug:
	ordering = ORDERING[order_slug]
    else: #default
	ordering = ORDERING['nombre-a-z']
    
    # recuperar productos para categoría (e hijos) y marca (e hijos) si la hay
    object_list = object.all_product_set(brand_slug)
    # ordenar segun se haya solicitado
    object_list = object_list.order_by('%s%s' % (ordering['reverse'], ordering['key']))
    page_title  = object.nombre
    
    if not object_list:
	recently_viewed = stats_functions.get_recently_viewed(request)
	view_recs       = stats_functions.recommended_from_views(request)
	paginator       = None
    else:
        # paginar
        products_per_page = 15 if current_site.id == 1 else 16
        try:
            paginator       = DiggPaginator(object_list, products_per_page, body=3, padding=1, margin=1,).page(page_number)
        except InvalidPage, e:
            return HttpResponseGone()
        object_list     = paginator.object_list
        recently_viewed = None
        view_recs       = None

    
    # recuperar la url para poder enlazar correctamente en el paginador
    if brand_slug != None and brand_slug != 'all':
        url = urlresolvers.reverse('catalog_brand', kwargs={'path': path, 'brand_slug': brand_slug})
    else:
        url = urlresolvers.reverse('catalog_category', kwargs={'path': path})
    
    try:
        metainfo = object.metatags.all()
    except:
        metainfo = ''

    return render_to_response(template_name, {
            'brand'             : brand,
            'object'            : object,
            'page_title'        : page_title,
            'object_list'       : object_list,
            'paginator'         : paginator,
            'recently_viewed'   : recently_viewed,
            'view_recs'         : view_recs,
            'url'               : url,
            'metainfo'          : metainfo,
        },
        context_instance = context)

#@cache_page(60 * 60 * 2) # cada 2 horas
def show_product(request, product_slug, template_name):
    object      = get_object_or_404(Product.objects.select_related(), slug=product_slug)
    
    try:
        metainfo = object.metatags.all()
    except:
        metainfo = ''
   
    # evaluate http method
    if request.method == 'POST':
        # add to cart...create the bound form
        postdata = request.POST.copy()
        #form     = ProductAddToCartForm(request, postdata)
        # check if posted data is valid
        #if form.is_valid():
            # add to cart and redirect
            #cart_functions.add_to_cart(request)
            # if test cookie worked, delete id
            #if request.session.test_cookie_worked():
                #request.session.delete_test_cookie()
            #url = urlresolvers.reverse('show_cart')
            #return redirect(url)
        #else:
	    #print form.errors
    #else:
        # it's a GET, so create the unbound form, note request as kwarg
        #form = ProductAddToCartForm(request=request, label_suffix=':')
    # assign the hidden input to the product_slug
    #form.fields['product_slug'].widget.attrs['value'] = object.slug
    # set the test cookie in the first GET request of a product
    # we already do this in index, but there can be a direct link to a product
    # and we must be ready to add it to cart
    request.session.set_test_cookie()
    # log product view in order to show it to others probably interested in it
    stats_functions.log_product_view(request, object)
    
    view_recs	    = stats_functions.recommended_from_views(request)
    #view_related    = object.cross_sells()
    recently_viewed = stats_functions.get_recently_viewed(request)

    return render_to_response(template_name, {
            'object'            : object,
            'page_title'        : object.nombre,
            'metainfo'          : metainfo,
            #'form'              : form,
            'view_recs'         : view_recs,
            #'view_related'      : view_related,
            'recently_viewed'   : recently_viewed,
        },
        context_instance=RequestContext(request))


#@cache_page(60 * 60 * 24) # cada día
def latest_products(request, template_name, page_number=1):
    # reutilizamos variables del contexto
    context = RequestContext(request)
    current_site = context['site']
    
    conf        = get_object_or_404(Config, site=current_site)
    page_title	= _(u'Latest products')
    days	= date.today() - timedelta(conf.latest_products_days)
    
    object_list = Product.objects.filter(is_active=True, created_at__range=(days, date.today()))
    
    # filtrar por precios
    min_price    = request.GET.get('min', None)
    max_price    = request.GET.get('max', None)
    if current_site.id == 1:
        if not min_price:
            try:
                min_price       = object_list.latest('price_site1').price_site1
            except:
                min_price       = 0
            total_min_price     = min_price
        else:
            total_min_price     = object_list.latest('price_site1').price_site1
            object_list         = object_list.filter(price_site1__gte=min_price)
        if not max_price:
            try:
                max_price       = object_list.reverse().latest('price_site1').price_site1
            except:
                max_price       = 0
            total_max_price     = max_price
        else:
            total_max_price     = object_list.reverse().latest('price_site1').price_site1
            object_list         = object_list.filter(price_site1__lte=max_price)
    if current_site.id == 2:
        if not min_price:
            try:
                min_price       = object_list.latest('price_site2').price_site2
            except:
                min_price       = 0
            total_min_price     = min_price
        else:
            total_min_price     = object_list.latest('price_site2').price_site2
            object_list         = object_list.filter(price_site2__gte=min_price)
        if not max_price:
            try:
                max_price       = object_list.reverse().latest('price_site2').price_site2
            except:
                max_price       = 0
            total_max_price     = max_price
        else:
            total_max_price     = object_list.reverse().latest('price_site2').price_site2
            object_list         = object_list.filter(price_site2__lte=max_price)

    url = urlresolvers.reverse('catalog_latests')

    if object_list.count() > 0:
        products_per_page = 15.0 if current_site.id == 1 else 16.0
        total_pages = iround(object_list.count()/products_per_page)
        if total_pages >= int(page_number):
            try:
                paginator = DiggPaginator(object_list, products_per_page, body=3, padding=1, margin=2,).page(page_number)
            except InvalidPage, e:
                return HttpResponseGone()
            object_list = paginator.object_list
    
    return render_to_response(template_name, locals(),
        context_instance=RequestContext(request))


def search_product(request, template_name):
    page_title = _(u'Product Search')

    return render_to_response(template_name, locals(),
        context_instance=RequestContext(request))


def search_results(request, template_name, page_number=1):
    page_title = _(u'Search results')

    try:
	request.GET['busqueda']
    except:
	no_search = True
	url = urlresolvers.reverse('catalog_search')
	return redirect(url)
    else:
	key_search = request.GET['busqueda']
	if key_search:
            object_list = Product.objects.filter(is_active = True).filter(
                    Q(name__icontains=key_search) | Q(description__icontains=key_search)
                )
            #object_list.append(Product.objects.filter(is_active = True).filter(description__icontains=key_search))

	else:
	    page_title = _(u'Product Search')
	    message = _(u'Please, insert a term to search for')
	    template_name = 'catalog/search.html'

    return render_to_response(template_name, locals(),
        context_instance=RequestContext(request))
