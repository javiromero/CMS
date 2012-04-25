# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'Metatag.palabras_clave'
        db.alter_column('metatags_metatag', 'palabras_clave', self.gf('django.db.models.fields.CharField')(max_length=150, null=True))

        # Changing field 'Metatag.descripcion'
        db.alter_column('metatags_metatag', 'descripcion', self.gf('django.db.models.fields.CharField')(max_length=150, null=True))

        # Changing field 'Metatag.titulo'
        db.alter_column('metatags_metatag', 'titulo', self.gf('django.db.models.fields.CharField')(max_length=70, null=True))


    def backwards(self, orm):
        
        # Changing field 'Metatag.palabras_clave'
        db.alter_column('metatags_metatag', 'palabras_clave', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'Metatag.descripcion'
        db.alter_column('metatags_metatag', 'descripcion', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'Metatag.titulo'
        db.alter_column('metatags_metatag', 'titulo', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))


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
        }
    }

    complete_apps = ['metatags']
