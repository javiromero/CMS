# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Config'
        db.create_table('catalog_config', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('eslogan', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('productos_por_fila', self.gf('django.db.models.fields.IntegerField')(default=5)),
            ('destacados_por_fila', self.gf('django.db.models.fields.IntegerField')(default=5)),
            ('recomendados_por_fila', self.gf('django.db.models.fields.IntegerField')(default=5)),
            ('superventas_por_fila', self.gf('django.db.models.fields.IntegerField')(default=5)),
            ('dias_recientes', self.gf('django.db.models.fields.PositiveIntegerField')(default=7)),
            ('impuestos_incluidos', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('envio_gratis_desde', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=9, decimal_places=2, blank=True)),
            ('creado_el', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('actualizado_el', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('catalog', ['Config'])

        # Adding model 'Category'
        db.create_table('catalog_category', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=255, db_index=True)),
            ('imagen', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100)),
            ('resumen', self.gf('django.db.models.fields.TextField')()),
            ('descripcion', self.gf('django.db.models.fields.TextField')()),
            ('orden', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('en_menu', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('menu_nom', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True)),
            ('en_cabeza', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('cabeza_nom', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True)),
            ('en_pie', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('pie_nom', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True)),
            ('es_activo', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('creado_el', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('actualizado_el', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='children', null=True, to=orm['catalog.Category'])),
            ('lft', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('rght', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('tree_id', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('level', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
        ))
        db.send_create_signal('catalog', ['Category'])

        # Adding M2M table for field marca on 'Category'
        db.create_table('catalog_category_marca', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('category', models.ForeignKey(orm['catalog.category'], null=False)),
            ('brand', models.ForeignKey(orm['catalog.brand'], null=False))
        ))
        db.create_unique('catalog_category_marca', ['category_id', 'brand_id'])

        # Adding model 'Brand'
        db.create_table('catalog_brand', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=255, db_index=True)),
            ('imagen', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100)),
            ('link', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('orden', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('es_activo', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('creado_el', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('actualizado_el', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='children', null=True, to=orm['catalog.Brand'])),
            ('lft', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('rght', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('tree_id', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('level', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
        ))
        db.send_create_signal('catalog', ['Brand'])

        # Adding model 'Product'
        db.create_table('catalog_product', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=255, db_index=True)),
            ('resumen', self.gf('django.db.models.fields.TextField')()),
            ('descripcion', self.gf('django.db.models.fields.TextField')()),
            ('orden', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('marca', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['catalog.Brand'], null=True, blank=True)),
            ('sku', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('referencia', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('stock', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('es_destacado', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('es_superventas', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('es_recomendado', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('impuestos', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['catalog.ProductTax'])),
            ('peso', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['catalog.ProductWeight'])),
            ('peso_unidades', self.gf('django.db.models.fields.CharField')(default='kg.', max_length=3, null=True, blank=True)),
            ('longitud', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=6, decimal_places=2, blank=True)),
            ('longitud_unidades', self.gf('django.db.models.fields.CharField')(default='m.', max_length=3, null=True, blank=True)),
            ('ancho', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=6, decimal_places=2, blank=True)),
            ('ancho_unidades', self.gf('django.db.models.fields.CharField')(default='m.', max_length=3, null=True, blank=True)),
            ('alto', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=6, decimal_places=2, blank=True)),
            ('alto_unidades', self.gf('django.db.models.fields.CharField')(default='m.', max_length=3, null=True, blank=True)),
            ('es_activo', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('creado_el', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('actualizado_el', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('es_pack', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('catalog', ['Product'])

        # Adding M2M table for field categorias on 'Product'
        db.create_table('catalog_product_categorias', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('product', models.ForeignKey(orm['catalog.product'], null=False)),
            ('category', models.ForeignKey(orm['catalog.category'], null=False))
        ))
        db.create_unique('catalog_product_categorias', ['product_id', 'category_id'])

        # Adding M2M table for field pack on 'Product'
        db.create_table('catalog_product_pack', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_product', models.ForeignKey(orm['catalog.product'], null=False)),
            ('to_product', models.ForeignKey(orm['catalog.product'], null=False))
        ))
        db.create_unique('catalog_product_pack', ['from_product_id', 'to_product_id'])

        # Adding model 'ProductWeight'
        db.create_table('catalog_productweight', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('minimo', self.gf('django.db.models.fields.DecimalField')(max_digits=8, decimal_places=3)),
            ('maximo', self.gf('django.db.models.fields.DecimalField')(max_digits=8, decimal_places=3)),
        ))
        db.send_create_signal('catalog', ['ProductWeight'])

        # Adding model 'ProductTax'
        db.create_table('catalog_producttax', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('cantidad', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2)),
        ))
        db.send_create_signal('catalog', ['ProductTax'])

        # Adding model 'ProductPrice'
        db.create_table('catalog_productprice', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('producto', self.gf('django.db.models.fields.related.ForeignKey')(related_name='price_set', to=orm['catalog.Product'])),
            ('precio', self.gf('django.db.models.fields.DecimalField')(max_digits=9, decimal_places=2)),
            ('desde', self.gf('django.db.models.fields.DateField')()),
            ('hasta', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
        ))
        db.send_create_signal('catalog', ['ProductPrice'])

        # Adding unique constraint on 'ProductPrice', fields ['producto', 'precio', 'desde', 'hasta']
        db.create_unique('catalog_productprice', ['producto_id', 'precio', 'desde', 'hasta'])

        # Adding model 'ProductImage'
        db.create_table('catalog_productimage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('producto', self.gf('django.db.models.fields.related.ForeignKey')(related_name='image_set', to=orm['catalog.Product'])),
            ('imagen', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100)),
            ('texto', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal('catalog', ['ProductImage'])

        # Adding model 'ProductVideo'
        db.create_table('catalog_productvideo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(related_name='video_set', to=orm['catalog.Product'])),
            ('video', self.gf('django.db.models.fields.CharField')(max_length=265)),
            ('texto', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal('catalog', ['ProductVideo'])


    def backwards(self, orm):
        
        # Removing unique constraint on 'ProductPrice', fields ['producto', 'precio', 'desde', 'hasta']
        db.delete_unique('catalog_productprice', ['producto_id', 'precio', 'desde', 'hasta'])

        # Deleting model 'Config'
        db.delete_table('catalog_config')

        # Deleting model 'Category'
        db.delete_table('catalog_category')

        # Removing M2M table for field marca on 'Category'
        db.delete_table('catalog_category_marca')

        # Deleting model 'Brand'
        db.delete_table('catalog_brand')

        # Deleting model 'Product'
        db.delete_table('catalog_product')

        # Removing M2M table for field categorias on 'Product'
        db.delete_table('catalog_product_categorias')

        # Removing M2M table for field pack on 'Product'
        db.delete_table('catalog_product_pack')

        # Deleting model 'ProductWeight'
        db.delete_table('catalog_productweight')

        # Deleting model 'ProductTax'
        db.delete_table('catalog_producttax')

        # Deleting model 'ProductPrice'
        db.delete_table('catalog_productprice')

        # Deleting model 'ProductImage'
        db.delete_table('catalog_productimage')

        # Deleting model 'ProductVideo'
        db.delete_table('catalog_productvideo')


    models = {
        'catalog.brand': {
            'Meta': {'ordering': "['parent__id', 'orden', 'creado_el', 'nombre']", 'object_name': 'Brand'},
            'actualizado_el': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'creado_el': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'es_activo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'orden': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': "orm['catalog.Brand']"}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255', 'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'catalog.category': {
            'Meta': {'object_name': 'Category'},
            'actualizado_el': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'cabeza_nom': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'creado_el': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'descripcion': ('django.db.models.fields.TextField', [], {}),
            'en_cabeza': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'en_menu': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'en_pie': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'es_activo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'marca': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['catalog.Brand']", 'null': 'True', 'blank': 'True'}),
            'menu_nom': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'orden': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': "orm['catalog.Category']"}),
            'pie_nom': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'resumen': ('django.db.models.fields.TextField', [], {}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255', 'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'catalog.config': {
            'Meta': {'object_name': 'Config'},
            'actualizado_el': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'creado_el': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'destacados_por_fila': ('django.db.models.fields.IntegerField', [], {'default': '5'}),
            'dias_recientes': ('django.db.models.fields.PositiveIntegerField', [], {'default': '7'}),
            'envio_gratis_desde': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '9', 'decimal_places': '2', 'blank': 'True'}),
            'eslogan': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'impuestos_incluidos': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'productos_por_fila': ('django.db.models.fields.IntegerField', [], {'default': '5'}),
            'recomendados_por_fila': ('django.db.models.fields.IntegerField', [], {'default': '5'}),
            'superventas_por_fila': ('django.db.models.fields.IntegerField', [], {'default': '5'})
        },
        'catalog.product': {
            'Meta': {'ordering': "['orden', '-creado_el']", 'object_name': 'Product'},
            'actualizado_el': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'alto': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'}),
            'alto_unidades': ('django.db.models.fields.CharField', [], {'default': "'m.'", 'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'ancho': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'}),
            'ancho_unidades': ('django.db.models.fields.CharField', [], {'default': "'m.'", 'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'categorias': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['catalog.Category']", 'symmetrical': 'False'}),
            'creado_el': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'descripcion': ('django.db.models.fields.TextField', [], {}),
            'es_activo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'es_destacado': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'es_pack': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'es_recomendado': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'es_superventas': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'impuestos': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['catalog.ProductTax']"}),
            'longitud': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'}),
            'longitud_unidades': ('django.db.models.fields.CharField', [], {'default': "'m.'", 'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'marca': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['catalog.Brand']", 'null': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'orden': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'pack': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['catalog.Product']", 'symmetrical': 'False', 'blank': 'True'}),
            'peso': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['catalog.ProductWeight']"}),
            'peso_unidades': ('django.db.models.fields.CharField', [], {'default': "'kg.'", 'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'referencia': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'resumen': ('django.db.models.fields.TextField', [], {}),
            'sku': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255', 'db_index': 'True'}),
            'stock': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'catalog.productimage': {
            'Meta': {'object_name': 'ProductImage'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'producto': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'image_set'", 'to': "orm['catalog.Product']"}),
            'texto': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        'catalog.productprice': {
            'Meta': {'ordering': "['precio', '-desde']", 'unique_together': "(('producto', 'precio', 'desde', 'hasta'),)", 'object_name': 'ProductPrice'},
            'desde': ('django.db.models.fields.DateField', [], {}),
            'hasta': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'precio': ('django.db.models.fields.DecimalField', [], {'max_digits': '9', 'decimal_places': '2'}),
            'producto': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'price_set'", 'to': "orm['catalog.Product']"})
        },
        'catalog.producttax': {
            'Meta': {'object_name': 'ProductTax'},
            'cantidad': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'catalog.productvideo': {
            'Meta': {'object_name': 'ProductVideo'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'video_set'", 'to': "orm['catalog.Product']"}),
            'texto': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'video': ('django.db.models.fields.CharField', [], {'max_length': '265'})
        },
        'catalog.productweight': {
            'Meta': {'object_name': 'ProductWeight'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'maximo': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '3'}),
            'minimo': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '3'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'metatags.metatag': {
            'Meta': {'object_name': 'Metatag'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'palabras_clave': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'robots': ('django.db.models.fields.CharField', [], {'default': '0', 'max_length': '2'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['catalog']
