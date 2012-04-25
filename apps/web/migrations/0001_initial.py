# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'HomePage'
        db.create_table('web_homepage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(unique=True, max_length=120)),
            ('contenido', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('es_activo', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('creado_el', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('actualizado_el', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('web', ['HomePage'])

        # Adding model 'Pagina'
        db.create_table('web_pagina', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=255, db_index=True)),
            ('resumen', self.gf('django.db.models.fields.TextField')()),
            ('contenido', self.gf('django.db.models.fields.TextField')()),
            ('plantilla', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('en_menu', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('menu_nom', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('en_cabeza', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('cabeza_nom', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('en_pie', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('pie_nom', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('es_activo', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('creado_el', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('actualizado_el', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='children', null=True, to=orm['web.Pagina'])),
            ('lft', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('rght', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('tree_id', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('level', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
        ))
        db.send_create_signal('web', ['Pagina'])

        # Adding model 'Sitemap'
        db.create_table('web_sitemap', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(unique=True, max_length=60)),
            ('titulo', self.gf('django.db.models.fields.CharField')(unique=True, max_length=120)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=255, db_index=True)),
            ('resumen', self.gf('django.db.models.fields.TextField')()),
            ('contenido', self.gf('django.db.models.fields.TextField')()),
            ('imagen', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100)),
            ('es_activo', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('creado_el', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('actualizado_el', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('web', ['Sitemap'])

        # Adding model 'ImagenPagina'
        db.create_table('web_imagenpagina', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pagina', self.gf('django.db.models.fields.related.ForeignKey')(related_name='images', to=orm['web.Pagina'])),
            ('orden', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('imagen', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100)),
            ('titulo', self.gf('django.db.models.fields.CharField')(unique=True, max_length=120)),
            ('descripcion', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('web', ['ImagenPagina'])

        # Adding model 'VideoPagina'
        db.create_table('web_videopagina', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pagina', self.gf('django.db.models.fields.related.ForeignKey')(related_name='videos', to=orm['web.Pagina'])),
            ('orden', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('video', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('titulo', self.gf('django.db.models.fields.CharField')(unique=True, max_length=120)),
            ('descripcion', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('web', ['VideoPagina'])

        # Adding model 'ArchivoPagina'
        db.create_table('web_archivopagina', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pagina', self.gf('django.db.models.fields.related.ForeignKey')(related_name='files', to=orm['web.Pagina'])),
            ('orden', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('archivo', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('titulo', self.gf('django.db.models.fields.CharField')(unique=True, max_length=120)),
            ('descripcion', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('web', ['ArchivoPagina'])

        # Adding model 'NamedURLSitemap'
        db.create_table('web_namedurlsitemap', (
            ('sitemap_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['web.Sitemap'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('web', ['NamedURLSitemap'])


    def backwards(self, orm):
        
        # Deleting model 'HomePage'
        db.delete_table('web_homepage')

        # Deleting model 'Pagina'
        db.delete_table('web_pagina')

        # Deleting model 'Sitemap'
        db.delete_table('web_sitemap')

        # Deleting model 'ImagenPagina'
        db.delete_table('web_imagenpagina')

        # Deleting model 'VideoPagina'
        db.delete_table('web_videopagina')

        # Deleting model 'ArchivoPagina'
        db.delete_table('web_archivopagina')

        # Deleting model 'NamedURLSitemap'
        db.delete_table('web_namedurlsitemap')


    models = {
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
        },
        'web.archivopagina': {
            'Meta': {'ordering': "['orden']", 'object_name': 'ArchivoPagina'},
            'archivo': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'descripcion': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'orden': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'pagina': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'files'", 'to': "orm['web.Pagina']"}),
            'titulo': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '120'})
        },
        'web.homepage': {
            'Meta': {'object_name': 'HomePage'},
            'actualizado_el': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'contenido': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'creado_el': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'es_activo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '120'})
        },
        'web.imagenpagina': {
            'Meta': {'ordering': "['orden']", 'object_name': 'ImagenPagina'},
            'descripcion': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'orden': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'pagina': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'images'", 'to': "orm['web.Pagina']"}),
            'titulo': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '120'})
        },
        'web.namedurlsitemap': {
            'Meta': {'object_name': 'NamedURLSitemap', '_ormbases': ['web.Sitemap']},
            'sitemap_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['web.Sitemap']", 'unique': 'True', 'primary_key': 'True'})
        },
        'web.pagina': {
            'Meta': {'object_name': 'Pagina'},
            'actualizado_el': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'cabeza_nom': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'contenido': ('django.db.models.fields.TextField', [], {}),
            'creado_el': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'en_cabeza': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'en_menu': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'en_pie': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'es_activo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'menu_nom': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': "orm['web.Pagina']"}),
            'pie_nom': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'plantilla': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'resumen': ('django.db.models.fields.TextField', [], {}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255', 'db_index': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'web.sitemap': {
            'Meta': {'object_name': 'Sitemap'},
            'actualizado_el': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'contenido': ('django.db.models.fields.TextField', [], {}),
            'creado_el': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'es_activo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '60'}),
            'resumen': ('django.db.models.fields.TextField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255', 'db_index': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '120'})
        },
        'web.videopagina': {
            'Meta': {'ordering': "['orden']", 'object_name': 'VideoPagina'},
            'descripcion': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'orden': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'pagina': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'videos'", 'to': "orm['web.Pagina']"}),
            'titulo': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '120'}),
            'video': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        }
    }

    complete_apps = ['web']
