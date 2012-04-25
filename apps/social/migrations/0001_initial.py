# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'RedSocial'
        db.create_table('social_redsocial', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('enlace', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('enlace_analytics', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True)),
            ('orden', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('imagen', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100)),
            ('es_activo', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('creado_el', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('actualizado_el', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('social', ['RedSocial'])


    def backwards(self, orm):
        
        # Deleting model 'RedSocial'
        db.delete_table('social_redsocial')


    models = {
        'social.redsocial': {
            'Meta': {'ordering': "['orden']", 'object_name': 'RedSocial'},
            'actualizado_el': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'creado_el': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'enlace': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'enlace_analytics': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'es_activo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'orden': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['social']
