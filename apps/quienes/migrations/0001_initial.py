# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Departamento'
        db.create_table('quienes_departamento', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(unique=True, max_length=120)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=120, db_index=True)),
            ('orden', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
            ('resumen', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('imagen', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100, null=True, blank=True)),
            ('contenido', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('es_activo', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('creado_el', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('actualizado_el', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('quienes', ['Departamento'])

        # Adding model 'Quienes'
        db.create_table('quienes_quienes', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(unique=True, max_length=120)),
            ('resumen', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('imagen', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100, null=True, blank=True)),
            ('contenido', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('es_activo', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('creado_el', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('actualizado_el', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('quienes', ['Quienes'])

        # Adding model 'Equipo'
        db.create_table('quienes_equipo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('departamento', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['quienes.Departamento'])),
            ('direccion', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('orden', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
            ('contenido', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('imagen', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100, null=True, blank=True)),
            ('es_activo', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('creado_el', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('actualizado_el', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('quienes', ['Equipo'])


    def backwards(self, orm):
        
        # Deleting model 'Departamento'
        db.delete_table('quienes_departamento')

        # Deleting model 'Quienes'
        db.delete_table('quienes_quienes')

        # Deleting model 'Equipo'
        db.delete_table('quienes_equipo')


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
        'quienes.departamento': {
            'Meta': {'object_name': 'Departamento'},
            'actualizado_el': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'contenido': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'creado_el': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'es_activo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'orden': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'resumen': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '120', 'db_index': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '120'})
        },
        'quienes.equipo': {
            'Meta': {'object_name': 'Equipo'},
            'actualizado_el': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'contenido': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'creado_el': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'departamento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['quienes.Departamento']"}),
            'direccion': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'es_activo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'orden': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '120'})
        },
        'quienes.quienes': {
            'Meta': {'object_name': 'Quienes'},
            'actualizado_el': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'contenido': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'creado_el': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'es_activo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'resumen': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '120'})
        }
    }

    complete_apps = ['quienes']
