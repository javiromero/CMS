# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Slider'
        db.create_table('slider_slider', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('imagen', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100)),
            ('video', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=120, null=True, blank=True)),
            ('contenido', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('enlace', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('enlace_texto', self.gf('django.db.models.fields.CharField')(max_length=60, null=True, blank=True)),
            ('enlace_analytics', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True)),
            ('orden', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('es_activo', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('creado_el', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('actualizado_el', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('real_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'], null=True)),
        ))
        db.send_create_signal('slider', ['Slider'])


    def backwards(self, orm):
        
        # Deleting model 'Slider'
        db.delete_table('slider_slider')


    models = {
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'slider.slider': {
            'Meta': {'ordering': "['orden']", 'object_name': 'Slider'},
            'actualizado_el': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'contenido': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'creado_el': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'enlace': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'enlace_analytics': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'enlace_texto': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True', 'blank': 'True'}),
            'es_activo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'orden': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'real_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']", 'null': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'video': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        }
    }

    complete_apps = ['slider']
