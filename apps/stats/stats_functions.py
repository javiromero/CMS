# -*- coding: utf-8 -*-

'''
    Javier Romero Blanco
    javi.azuaga@gmail.com
    http://barrabarra.es
    ©2010
'''

from catalog.models import Config, Product
from stats.models import ProductView
import base64
import random

try:
    conf	= Config.objects.get()
except:
    PRODUCTS_PER_ROW = 1
    RECOMMENDED_PER_ROW = 1
    BESTSELLERS_PER_ROW = 1
else:
    PRODUCTS_PER_ROW = conf.productos_por_fila
    RECOMMENDED_PER_ROW = conf.recomendados_por_fila
    BESTSELLERS_PER_ROW = conf.superventas_por_fila
    

def tracking_id(request):
    try:
        return request.session['tracking_id']
    except KeyError:
        tracking_id = ''
        characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()'
        tracking_id_length = 36
        for y in range(tracking_id_length):
            tracking_id += random.choice(characters)
        request.session['tracking_id'] = base64.b64encode(tracking_id)
        return request.session['tracking_id']

def log_product_view(request, product):
    t_id = tracking_id(request)
    try:
        v = ProductView.objects.get(tracking_id=t_id, product=product)
        v.save()
    except ProductView.DoesNotExist:
        v = ProductView()
        v.product = product
        v.ip_address = request.META.get('REMOTE_ADDR')
        v.tracking_id = t_id
        v.user = None
        if request.user.is_authenticated():
            v.user = request.user
        v.save()

        
"""
    Hay que limitar las consultas con LIMITS, que django añade con [:LIMITE]
    PERO además hay que pasar los resultados a listas, ya que Mysql no permite
    realizar consultas con IN y LIMIT:
        This version of MySQL doesn't yet support 'LIMIT & IN/ALL/ANY/SOME subquery'
        
    Seamos conservadores, 10 es un nº decente para limitar
"""
def recommended_from_views(request):
    t_id = tracking_id(request)
    # get recently viewed products
    viewed = get_recently_viewed(request)
    # if there are previously viewed products, get other tracking ids that have
    # viewed those products also
    if viewed:
        productviews = ProductView.objects.filter(product__in=viewed).values('tracking_id')[:10]
        t_ids = [v['tracking_id'] for v in productviews]
        # if there are other tracking ids, get other products.
        if t_ids:
            all_viewed = Product.active.filter(productview__tracking_id__in=t_ids)[:10]
            all_list   = list(all_viewed)
            # if there are other products, get them, excluding the
            # products that the customer has already viewed.
            if all_viewed:
                other_viewed = ProductView.objects.filter(product__in=all_list).exclude(product__in=viewed)[:10]
                other_list   = list(other_viewed)
                if other_viewed:
                    return Product.active.filter(productview__in=other_list).distinct()[0:RECOMMENDED_PER_ROW]

def get_recently_viewed(request):
    t_id = tracking_id(request)
    views = ProductView.objects.filter(tracking_id=t_id).values('product_id').order_by('-date')[0:PRODUCTS_PER_ROW]
    product_ids = [v['product_id'] for v in views]
    return Product.active.filter(id__in=product_ids)
