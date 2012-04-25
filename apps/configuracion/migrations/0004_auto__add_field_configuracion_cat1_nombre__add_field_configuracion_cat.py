# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Configuracion.cat1_nombre'
        db.add_column('configuracion_configuracion', 'cat1_nombre', self.gf('django.db.models.fields.CharField')(default=u'Para los que saben lo que quieren...', max_length=255), keep_default=False)

        # Adding field 'Configuracion.cat2_nombre'
        db.add_column('configuracion_configuracion', 'cat2_nombre', self.gf('django.db.models.fields.CharField')(default=u'Para los que buscan quien los ayude...', max_length=255), keep_default=False)

        # Adding field 'Configuracion.cat3_nombre'
        db.add_column('configuracion_configuracion', 'cat3_nombre', self.gf('django.db.models.fields.CharField')(default=u'Para los que se bastan solos...', max_length=255), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Configuracion.cat1_nombre'
        db.delete_column('configuracion_configuracion', 'cat1_nombre')

        # Deleting field 'Configuracion.cat2_nombre'
        db.delete_column('configuracion_configuracion', 'cat2_nombre')

        # Deleting field 'Configuracion.cat3_nombre'
        db.delete_column('configuracion_configuracion', 'cat3_nombre')


    models = {
        'configuracion.configuracion': {
            'Meta': {'object_name': 'Configuracion'},
            'actualizado_el': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'blog': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'blog_entradas': ('django.db.models.fields.IntegerField', [], {'default': '5', 'null': 'True', 'blank': 'True'}),
            'blog_rss': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'cat1_nombre': ('django.db.models.fields.CharField', [], {'default': "u'Para los que saben lo que quieren...'", 'max_length': '255'}),
            'cat2_nombre': ('django.db.models.fields.CharField', [], {'default': "u'Para los que buscan quien los ayude...'", 'max_length': '255'}),
            'cat3_nombre': ('django.db.models.fields.CharField', [], {'default': "u'Para los que se bastan solos...'", 'max_length': '255'}),
            'creado_el': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'eslogan': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'favicon': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'google_analytics': ('django.db.models.fields.TextField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'tiempo_diapositivas': ('django.db.models.fields.IntegerField', [], {'default': '5000'}),
            'titulo': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '120'}),
            'verificacion_webmaster': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        'configuracion.contactdata': {
            'Meta': {'object_name': 'ContactData'},
            'ciudad': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'codigo_postal': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'configuracion': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['configuracion.Configuracion']"}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'movil': ('django.db.models.fields.CharField', [], {'max_length': '12', 'null': 'True', 'blank': 'True'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '12', 'null': 'True', 'blank': 'True'})
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
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'palabras_clave': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'robots': ('django.db.models.fields.CharField', [], {'default': '0', 'max_length': '2'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '70', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['configuracion']
