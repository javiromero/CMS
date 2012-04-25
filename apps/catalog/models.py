# -*- coding: utf-8 -*-

'''
    Javier Romero Blanco
    javi.azuaga@gmail.com
    http://barrabarra.es
    ©2010
'''

from django.conf import settings
from django.contrib.contenttypes import generic
from django.contrib.sites.models import Site
from django.core.cache import cache
from django.db import models
from django.db.models import Q
from django.db.models.signals import post_delete, m2m_changed, post_save
from django.template.defaultfilters import slugify
from django.utils.translation import ugettext as _

from metatags.models import Metatag
from sorl.thumbnail import ImageField

from os import path
import mptt
import datetime


"""
  Configuración de la tienda online
"""
class Config(models.Model):  
    eslogan             = models.CharField(_(u'Eslogan'), blank=True, max_length=255, null=True, help_text=_(u'Eslogan de la tienda. 255 caracteres max.'))
    
    productos_por_fila  = models.IntegerField(_('Productos por fila'), default=5, help_text=_(u'El número de productos que se mostrarán en cada fila'))
    destacados_por_fila = models.IntegerField(_('Destacados por fila'), default=5, help_text=_(u'El número de productos destacados que se mostrarán en cada fila'))
    recomendados_por_fila       = models.IntegerField(_('Recomendados por fila'), default=5, help_text=_(u'El número de productos recomendados que se mostrarán en cada fila'))
    superventas_por_fila        = models.IntegerField(_('Superventas por fila'), default=5, help_text=_(u'El número de productos superventas que se mostrarán en cada fila'))
    
    dias_recientes      = models.PositiveIntegerField(_(u'Nº días para recientes'), default=7, help_text=_(u'Cuántos días se tendrán en cuenta para mostrar los productos recientes'))
    
    impuestos_incluidos = models.BooleanField(_(u'Iva incluído'), default=True, help_text=_(u'Los precios que se indican incluyen/no incluyen impuestos'))
    envio_gratis_desde  = models.DecimalField(_(u'Envío gratuíto desde'), help_text=_(u'El envío será gratuíto si la cesta alcanza esta cantidad'), max_digits=9, decimal_places=2, blank=True, null=True,)

    creado_el           = models.DateTimeField(_(u'Creado el'), editable=False, auto_now_add=True)
    actualizado_el      = models.DateTimeField(_(u'Actualizado el'), editable=False, auto_now=True)

    metatags            = generic.GenericRelation('metatags.Metatag')

    def __unicode__(self):
        return u'Configuración de la tienda'
    
    class Meta:
        verbose_name = _(u'Configuración de la tienda')
        verbose_name_plural = _(u'Configuración de la tienda')


"""
  Categorías de la tienda
"""
class Category(models.Model):
    nombre      = models.CharField(_('Titulo'), max_length=255)
    slug        = models.SlugField(_('Slug'), max_length=255, help_text=_(u'Valor único para la ruta a la página de la categoría. Creado a partir del nombre.'))
    
    imagen      = ImageField(_(u'Imagen'), upload_to='catalog/category')
    resumen     = models.TextField(_(u'Breve resumen de la categoría'))
    descripcion = models.TextField(_(u'Descripción'), help_text=_(u'Descripción completa de la categoría'))
    orden       = models.IntegerField(_(u'Orden'), default=0, help_text=_(u'Orden en el que se mostrará la categoría'))

    en_menu     = models.BooleanField(_(u'En menu'), default=False)
    menu_nom    = models.CharField(_(u'Nombre en el menú'), max_length=256, blank=True, null=True)
    en_cabeza   = models.BooleanField(_(u'En cabecera'), default=False)
    cabeza_nom  = models.CharField(_(u'Nombre en la cabecera'), max_length=256, blank=True, null=True)
    en_pie      = models.BooleanField(_(u'En pie'), default=False)
    pie_nom     = models.CharField(_(u'Nombre en el pie'), max_length=256, blank=True, null=True)

    es_activo   = models.BooleanField(_(u'Activo'), default=True, help_text=_(u'Determina si se muestra en el sitio'))
    creado_el           = models.DateTimeField(_(u'Creado el'), editable=False, auto_now_add=True)
    actualizado_el      = models.DateTimeField(_(u'Actualizado el'), editable=False, auto_now=True)
    
    marca       = models.ManyToManyField('Brand', verbose_name=_(u'Marcas'), blank=True, null=True)
    metatags    = generic.GenericRelation('metatags.Metatag')

    parent      = models.ForeignKey('self', verbose_name=_(u'Padre'), blank=True, null=True, related_name='children')
    PAGE_URL_KEY        = "category_%d"
    _complete_slug      = None # caché de instancia

    def __unicode__(self):
        name = self.nombre
        #for ancestor in self.get_ancestors(ascending=True):
            #name = ancestor.name + u' - ' + name
        return name

    def hijos(self):
        return self.children.filter(es_activo=True).order_by('orden')

    def get_titulo(self):
        return self.nombre
        
    def menu_hijos(self):
        return self.children.filter(es_activo=True, en_menu=True).order_by('orden')

    def cabeza_hijos(self):
        return self.children.filter(es_activo=True, en_cabeza=True).order_by('orden')
        
    def pie_hijos(self):
        return self.children.filter(es_activo=True, en_pie=True).order_by('orden')

    def destacados_productos(self):
        return self.product_set.filter(es_activo=True, es_destacado=True).order_by('orden')
        
    # Devuelve todos los productos de una categoria, una marca y de sus marcas descendientes
    def all_product_set(self, brand_slug=None):
	products = list()
	if brand_slug:
	    # get the brand object
	    brand       = Brand.objects.get(slug=brand_slug)
	    brands      = [b for b in brand.get_descendants().filter(es_activo=True)]
	    brands.append(brand)
	    
	    # get all active products from the category and the main and descendant brands
	    products = Product.objects.filter(es_activo=True, categorias=self, marca__in=brands)
	  
	else:
	    # get all active products from the category
	    products = self.product_set.filter(es_activo=True)

	return products

    def menu_nombre(self):
        return self.menu_nom if self.menu_nom else self.nombre

    def cabeza_nombre(self):
        return self.cabeza_nom if self.cabeza_nom else self.nombre
        
    def pie_nombre(self):
        return self.pie_nom if self.pie_nom else self.nombre
	    
	    
    def get_complete_slug(self):
        """Return the complete slug of this category by concatenating
        all parent's slugs."""
        
        if self._complete_slug:
            return self._complete_slug
        self._complete_slug = cache.get(self.PAGE_URL_KEY % (self.id))
        if self._complete_slug:
            return self._complete_slug

	url = self.slug
	
        for ancestor in self.get_ancestors(ascending=True):
            url = ancestor.slug + u'/' + url

        cache.set(self.PAGE_URL_KEY % (self.id), url)
        self._complete_slug = url
        return url

    @models.permalink
    def get_absolute_url(self):
	return ('catalog_category', (), {'path': self.get_complete_slug() })

    class Meta:
        #ordering = ['parent__id', 'orden', 'nombre']
        verbose_name = _(u'Categoría')
        verbose_name_plural = _(u'Categorías')


# Don't register the Category model twice.
try:
    mptt.register(Category)
except mptt.AlreadyRegistered:
    pass


"""
  Marcas de productos
"""
class Brand(models.Model):
    nombre      = models.CharField(_('Nombre'), max_length=255)
    slug        = models.SlugField(_('Slug'), max_length=255, help_text=_(u'Valor único para la ruta a la página de la categoría. Creado a partir del nombre.'))
    
    imagen      = ImageField(_(u'Logo'), upload_to='catalog/brand')
    link        = models.URLField(_(u'Link'), verify_exists=False, help_text=_(u'Enlace a la web de la marca'), blank=True, null=True)
    orden       = models.IntegerField(_(u'Orden'), default=0, help_text=_(u'Orden en el que se mostrará la categoría'))

    es_activo   = models.BooleanField(_('Activo'), default=True, help_text=_(u'Determina si se muestra en el sitio'))
    creado_el           = models.DateTimeField(_(u'Creado el'), editable=False, auto_now_add=True)
    actualizado_el      = models.DateTimeField(_(u'Actualizado el'), editable=False, auto_now=True)

    parent		= models.ForeignKey('self', verbose_name=_('Parent'), blank=True, null=True, related_name='children')
    PAGE_URL_KEY	= "brand_%d"
    _complete_slug	= None # caché de instancia
    
    def __unicode__(self):
        name = self.name
        #for ancestor in self.get_ancestors(ascending=True):
            #name = ancestor.name + u' - ' + name
        return name

    def hijos(self):
        return self.child.order_by('orden')

    def get_complete_slug(self):
        """Return the complete slug of this brand by concatenating
        all parent's slugs."""
        
        if self._complete_slug:
            return self._complete_slug
        self._complete_slug = cache.get(self.PAGE_URL_KEY % (self.id))
        if self._complete_slug:
            return self._complete_slug

	url = self.slug
	
        for ancestor in self.get_ancestors(ascending=True):
            url = ancestor.slug + u'/' + url

        cache.set(self.PAGE_URL_KEY % (self.id), url)
        self._complete_slug = url
        return url        
        
    @models.permalink
    def get_absolute_url(self):
        # no tiene sentido mostrar la marca si no es en alguna categoría
	return ('catalog_brand', (), {'path': self.get_complete_slug() })
	#return ('catalog_home', (), {})

    class Meta:
	verbose_name		= _(u'Marca')
	verbose_name_plural	= _(u'Marcas')
	ordering = ['parent__id', 'orden', 'creado_el', 'nombre']

# Don't register the Brand model twice.
try:
    mptt.register(Brand)
except mptt.AlreadyRegistered:
    pass


class ActiveProductManager(models.Manager):
    def get_query_set(self):
        return super(ActiveProductManager, self).get_query_set().filter(es_activo=True)

class FeaturedProductManager(models.Manager):
    def all(self):
        return super(FeaturedProductManager, self).all().filter(es_activo=True, stock__gt=0).filter(es_destacado=True)
        
class BestsellerProductManager(models.Manager):
    def all(self):
        return super(BestsellerProductManager, self).all().filter(es_activo=True, stock__gt=0).filter(es_superventas=True)

class RecommendedProductManager(models.Manager):
    def all(self):
        return super(RecommendedProductManager, self).all().filter(es_activo=True, stock__gt=0).filter(es_recomendado=True)


"""
  Productos de la tienda
"""
class Product(models.Model):
    nombre      = models.CharField(_('Nombre'), max_length=255)
    slug        = models.SlugField(_('Slug'), max_length=255, help_text=_(u'Valor único para la ruta a la página de la categoría. Creado a partir del nombre.'))
    
    resumen     = models.TextField(_(u'Breve resumen del producto'))
    descripcion = models.TextField(_(u'Descripción'), help_text=_(u'Descripción completa del producto'))
    orden       = models.IntegerField(_(u'Orden'), default=0, help_text=_(u'Orden en el que se mostrará'))
    
    categorias  = models.ManyToManyField(Category, verbose_name=_('Categorias'))
    marca	= models.ForeignKey(Brand, verbose_name=_('Marca'), blank=True, null=True)
    
    sku		= models.CharField(_('SKU'), max_length=50, blank=True, help_text=_(u'Referencia única del producto. Utilizado para mejorar el SEO.'))
    referencia  = models.CharField(_('Referencia Interna'), max_length=255, null=True, blank=True, help_text=_(u'Referencia interna del producto, usada en su negocio.'))
    stock	= models.IntegerField(_('Cantidad'), blank=True, null=True)

    es_destacado        = models.BooleanField(_('Destacado'), default=False)
    es_superventas      = models.BooleanField(_('Superventas'), default=False)
    es_recomendado      = models.BooleanField(_('Recomendado'), default=False)
    
    impuestos	= models.ForeignKey('ProductTax', verbose_name=_(u'Impuestos'))
    
    peso	= models.ForeignKey('ProductWeight', verbose_name=_('Peso'))
    peso_unidades       = models.CharField(_('Unidades de peso'), max_length=3, default='kg.', null=True, blank=True)
    longitud	= models.DecimalField(_('Longitud'), max_digits=6, decimal_places=2, null=True, blank=True)
    longitud_unidades   = models.CharField(_('Unidades de longitud'), max_length=3, default='m.', null=True, blank=True)
    ancho	= models.DecimalField(_('Ancho'), max_digits=6, decimal_places=2, null=True, blank=True)
    ancho_unidades      = models.CharField(_('Unidades de ancho'), max_length=3, default='m.', null=True, blank=True)
    alto	= models.DecimalField(_('Alto'), max_digits=6, decimal_places=2, null=True, blank=True)
    alto_unidades       = models.CharField(_('Unidades de alto'), max_length=3, default='m.',  null=True, blank=True)
    
    es_activo   = models.BooleanField(_(u'Activo'), default=True, help_text=_(u'Determina si se muestra en el sitio'))
    creado_el           = models.DateTimeField(_(u'Creado el'), editable=False, auto_now_add=True)
    actualizado_el      = models.DateTimeField(_(u'Actualizado el'), editable=False, auto_now=True)

    es_pack	= models.BooleanField(_('Pack'), default=False)
    pack	= models.ManyToManyField('Product', blank=True, verbose_name=_('Productos del pack'))
    
    objects	= models.Manager()
    active	= ActiveProductManager()
    featured	= FeaturedProductManager()
    bestseller	= BestsellerProductManager()
    recommended	= RecommendedProductManager()
    
    metatags	= generic.GenericRelation('metatags.Metatag')

    def __unicode__(self):
        return self.nombre

    def _get_mainImage(self):
        try:
	    img = self.image_set.all()[:1].get()
	except:
	    img = False
        return img
    imagen = property(_get_mainImage)

    def _get_gallery(self):
	gal = False
        if self.image_set.all().count() > 1:
            gal = self.image_set.all()
        return gal
    gallery = property(_get_gallery)

    #def get_image_filename(self):
	#return self.image.image.file.__str__()

    #def get_image_url(self):
	#return self.image.image.url.__str__()

    #def show_thumb(self):
	#tiny = path.join(path.dirname(self.get_image_filename()), 'admin', self.slug)
	#if not path.exists(tiny):
	    #im = Image.open(self.get_image_filename())
	    #im.thumbnail(TINY_SIZE, Image.ANTIALIAS)
	    #if not path.exists(path.dirname(tiny)):
		#from os import makedirs
		#makedirs(path.dirname(tiny))
	    #im.save(tiny, 'JPEG')
	#tiny_url = path.join(path.dirname(self.get_image_url()), 'admin', str(self.slug))
	#return '<a href="%s/"><img src="%s" alt="admin thumbnail"/></a>' % (self.id, tiny_url)
    #show_thumb.allow_tags = True
    #show_thumb.short_description = _(u'Image')

    #def update_thumb(self):
        #from os import remove
        #tiny = path.join(path.dirname(self.get_image_filename()), 'admin', self.slug)
        #remove(tiny)
        
        #return

    """
      Devuelve el precio mínimo actual para el sitio del producto, teniendo en cuenta
      los diversos precios existentes y los descuentos por marcas que puedan aplicarse

      Si el campo no está calculado, se calcula y se guarda.
      
      Get available price with this scheme start date <= today <= expiration date
      
      Esta funcion se complica.
      Recoge todos los precios para un producto teniendo en cuenta el sitio al que pertenecen y las fechas de inicio y fin.
      Todas las querysets de precios ya estan ordenadas por precio y fecha de inicio: ordering = ['price', '-start_date']
      
      Total, que se coje el precio mas bajo: actual_prices[0] y ese es el precio atual, si no hay precio definido, devuelve 9999 :D
      
      Si ademas del precio hay un descuento por marca activo, lo aplica, si no, el precio sigue igual porque el descuento por defecto es 0
    """
    def _get_price(self):
        price   = 9999
        if current_site.id == 1:
            price = self.price_site1
        else:
            price = self.price_site2
            
        if price != 9999 and price != None:
            return price
        else:
            conf = Config.objects.get(id=1)
            taxes_included = conf.impuestos_incluidos
            actual_prices = self.price_set.filter(Q(start_date__lte=datetime.date.today()),Q(end_date__gte=datetime.date.today())|Q(end_date__isnull=True))

            # tomar menor precio activo
            try:
                price = actual_prices[0].price
                # aplicar impuestos si es necesario
                if not taxes_included:
                    price = (price * self.tax.quantity) + price
                return price
            # no hay precios? devolver 9999
            except:
                return 9999
    price = property(_get_price)

    """
      Get price vality
    """
    def _get_price_until(self):
	actual_prices = self.price_set.filter(Q(start_date__lte=datetime.date.today()),Q(end_date__gte=datetime.date.today())|Q(end_date__isnull=True))
        try:
	    price = actual_prices[0]
	except:
	    price = None
	    
	if price:
	    return price.end_date
	else:
	    return False

    price_until = property(_get_price_until)

    """
      Get previous available price for the product
      
      Esta funcion tambien es complicadilla.
      Recoge todos los precios para un producto teniendo en cuenta el sitio al que pertenecen y las fechas de inicio y fin.
      Todas las querysets de precios ya estan ordenadas por precio y fecha de inicio: ordering = ['price', '-start_date']
      asi que se coge el precio mas alto: latest('price') para poder mostrar el mayor descuento posible.
      
      Tambien se mira si hay descuento de marca aplicable para, en ese caso mostrar el precio original
    """
    def _get_old_price(self):

        old_price   = None
            
        # devolver desde campo de la instancia o bien calcularlo y guardarlo
        if old_price != None and old_price != 9999:
            return old_price
        else:
            conf = Config.objects.get()
            taxes_included = conf.impuestos_incluidos
            actual_prices = self.price_set.filter(Q(start_date__lte=datetime.date.today()),Q(end_date__gte=datetime.date.today())|Q(end_date__isnull=True))
            
            # ¿y si hay descuento de precio y también de marca?
            # se devuelve el precio anterior porque será mayor que el menor menos
            # el descuento de marcas :)
            
            # si hay mas de un precio, coger el mayor para tener un porcentaje de descuento mas elevado
            if actual_prices.count() > 1:
                old_price = actual_prices.latest('price').price
                
                # aplicar impuestos si es necesario
                if not taxes_included:
                    old_price = (old_price * self.impuestos.quantity) + old_price
                    
                return old_price
            
            # y si no hay ni varios precios pues no hay precio anterior, se devuelve falso
            else:
                return None
    old_price = property(_get_old_price)
    
    # Calcula el porcentaje de ahorro entre precio anterior y precio actual del producto
    # y aplica descuento de marca en el sitio actual
    def _get_saving(self):
        saving = None
            
        # devolver el % ahorro desde la instancia o bien calcularlo y guardarlo
        if saving != None:
            return saving
        else:
            # old_price tambien aplica el descuento por marca si lo hay
            if self.old_price: 
                diference = self.old_price - self.price
                saving = (diference*100)/self.old_price
                saving = round(saving)
                return int(saving)
            else:
                return 0          
    saving = property(_get_saving)

    def _get_pack_saving(self):
        if self.is_pack:
            pack_price = 0
            for p in self.pack.all():
                pack_price = pack_price + p.price
            
            diference = pack_price - self.price
            saving = (diference*100)/pack_price
            saving = round(saving)
            return int(saving)
        else:
            return False
    pack_saving = property(_get_pack_saving)

    #def cross_sells(self):
        #from checkout.models import Order, OrderItem
        #from django.contrib.auth.models import User
        
        #orders          = Order.objects.filter(orderitem__product=self)[:20]
        #orders_list     = list(orders)
        #users           = User.objects.filter(order__orderitem__product=self)[:20]
        #users_list      = list(users)
        #items           = OrderItem.objects.filter( Q(order__in=orders_list) | Q(order__user__in=users_list) ).exclude(product=self)[:10]
        #items_list      = list(items)
        #products        = Product.active.filter(orderitem__in=items_list).distinct()
        #return products
        
    @models.permalink
    def get_absolute_url(self):
	return ('catalog_product', (), {'product_slug': self.slug})

    class Meta:
        ordering = ['orden', '-creado_el']
        verbose_name = _('Producto')
        verbose_name_plural = _('Productos')


class ProductWeight(models.Model):
    minimo      = models.DecimalField(_(u'Peso mínimo'), max_digits=8, decimal_places=3)
    maximo	= models.DecimalField(_(u'Peso máximo'), max_digits=8, decimal_places=3)

    def __unicode__(self):
	return _(u'de %(min)s a %(max)s') % {'min': self.minimo, 'max': self.maximo}

    class Meta:
	verbose_name = _('Peso')
	verbose_name_plural = _('Pesos')


class ProductTax(models.Model):
    descripcion	= models.CharField(_(u'Descripción'), max_length=255, help_text=_(u'Descripción del impuesto'))
    cantidad	= models.DecimalField(_(u'Cantidad'), max_digits=5, decimal_places=2, help_text=_(u'Cantidad del impuesto a aplicar en tanto por ciento (sin incluir símbolo)'))

    def __unicode__(self):
	return self.cantidad.__str__()+"%"

    class Meta:
	verbose_name		= _(u'Impuesto')
	verbose_name_plural	= _(u'Impuestos')


"""
 Precios. Separados para que cada producto pueda tener más de uno y además puede estar asignado a uno/varios sitios
"""
class ProductPrice(models.Model):
    producto	= models.ForeignKey('Product', verbose_name=_('Producto'), related_name='price_set')
    precio	= models.DecimalField(_('Precio'), max_digits=9, decimal_places=2)
    desde	= models.DateField(_('Desde'), help_text=_(u'Desde cuándo será válido este precio'))
    hasta	= models.DateField(_('Hasta'), null=True, blank=True, help_text=_(u'Hasta cuándo será válido este precio'))

    def __unicode__(self):
        return u"%s €" % self.precio
    
    class Meta:
        ordering = ['precio', '-desde']
        verbose_name = _(u'Precio del producto')
        verbose_name_plural = _(u'Precios del producto')
        unique_together = (('producto', 'precio', 'desde', 'hasta'),)
        

class ProductImage(models.Model):
    producto	= models.ForeignKey('Product', verbose_name=_('Product'), related_name='image_set')
    imagen	= ImageField(_('Imagen'), upload_to='catalog/product')
    texto	= models.CharField(_('Texto'), max_length=255, blank=True)
    
    def __unicode__(self):
        return self.texto
    
    class Meta:
        verbose_name = _(u'Imagen del producto')
        verbose_name_plural = _(u'Imágenes del producto')


class ProductVideo(models.Model):
    product	= models.ForeignKey('Product', verbose_name=_('Producto'), related_name='video_set')
    video	= models.CharField(_('Video'), max_length=265)
    texto	= models.CharField(_('Texto'), max_length=255, blank=True)
    
    def __unicode__(self):
        return self.texto

    class Meta:
        verbose_name = _(u'Video del producto')
        verbose_name_plural = _(u'Videos del producto')
