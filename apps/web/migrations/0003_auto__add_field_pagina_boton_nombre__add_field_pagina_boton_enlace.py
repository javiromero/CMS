# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Pagina.boton_nombre'
        db.add_column('web_pagina', 'boton_nombre', self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True), keep_default=False)

        # Adding field 'Pagina.boton_enlace'
        db.add_column('web_pagina', 'boton_enlace', self.gf('django.db.models.fields.URLField')(default='', max_length=200, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Pagina.boton_nombre'
        db.delete_column('web_pagina', 'boton_nombre')

        # Deleting field 'Pagina.boton_enlace'
        db.delete_column('web_pagina', 'boton_enlace')


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
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'palabras_clave': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'robots': ('django.db.models.fields.CharField', [], {'default': '0', 'max_length': '2'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '70', 'null': 'True', 'blank': 'True'})
        },
        'web.archivopagina': {
            'Meta': {'ordering': "['orden']", 'object_name': 'ArchivoPagina'},
            'archivo': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'descripcion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
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
            'descripcion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'orden': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'pagina': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'images'", 'to': "orm['web.Pagina']"}),
            'titulo': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '120'})
        },
        'web.pagina': {
            'Meta': {'object_name': 'Pagina'},
            'actualizado_el': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'boton_enlace': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'boton_nombre': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
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
        'web.videopagina': {
            'Meta': {'ordering': "['orden']", 'object_name': 'VideoPagina'},
            'descripcion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'orden': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'pagina': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'videos'", 'to': "orm['web.Pagina']"}),
            'titulo': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '120'}),
            'video': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        }
    }

    complete_apps = ['web']
