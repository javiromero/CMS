# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Configuracion'
        db.create_table('configuracion_configuracion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(unique=True, max_length=120)),
            ('eslogan', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('logo', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100)),
            ('favicon', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100)),
            ('telefono', self.gf('django.db.models.fields.CharField')(max_length=12, null=True, blank=True)),
            ('movil', self.gf('django.db.models.fields.CharField')(max_length=12, null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
            ('direccion', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('codigo_postal', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('ciudad', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('blog', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('blog_rss', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('blog_entradas', self.gf('django.db.models.fields.IntegerField')(default=5, null=True, blank=True)),
            ('tiempo_diapositivas', self.gf('django.db.models.fields.IntegerField')(default=5000)),
            ('google_analytics', self.gf('django.db.models.fields.TextField')(max_length=100, null=True, blank=True)),
            ('verificacion_webmaster', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('creado_el', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('actualizado_el', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('configuracion', ['Configuracion'])

        # Adding model 'NotificationEmail'
        db.create_table('configuracion_notificationemail', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('configuracion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['configuracion.Configuracion'])),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
        ))
        db.send_create_signal('configuracion', ['NotificationEmail'])


    def backwards(self, orm):
        
        # Deleting model 'Configuracion'
        db.delete_table('configuracion_configuracion')

        # Deleting model 'NotificationEmail'
        db.delete_table('configuracion_notificationemail')


    models = {
        'configuracion.configuracion': {
            'Meta': {'object_name': 'Configuracion'},
            'actualizado_el': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'blog': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'blog_entradas': ('django.db.models.fields.IntegerField', [], {'default': '5', 'null': 'True', 'blank': 'True'}),
            'blog_rss': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'ciudad': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'codigo_postal': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'creado_el': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'eslogan': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'favicon': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'google_analytics': ('django.db.models.fields.TextField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'movil': ('django.db.models.fields.CharField', [], {'max_length': '12', 'null': 'True', 'blank': 'True'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '12', 'null': 'True', 'blank': 'True'}),
            'tiempo_diapositivas': ('django.db.models.fields.IntegerField', [], {'default': '5000'}),
            'titulo': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '120'}),
            'verificacion_webmaster': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        'configuracion.notificationemail': {
            'Meta': {'object_name': 'NotificationEmail'},
            'configuracion': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['configuracion.Configuracion']"}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
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

    complete_apps = ['configuracion']
