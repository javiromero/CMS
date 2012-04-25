# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'ContactData'
        db.create_table('configuracion_contactdata', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('telefono', self.gf('django.db.models.fields.CharField')(max_length=12, null=True, blank=True)),
            ('movil', self.gf('django.db.models.fields.CharField')(max_length=12, null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
            ('direccion', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('codigo_postal', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('ciudad', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('configuracion', ['ContactData'])

        # Deleting field 'Configuracion.movil'
        db.delete_column('configuracion_configuracion', 'movil')

        # Deleting field 'Configuracion.codigo_postal'
        db.delete_column('configuracion_configuracion', 'codigo_postal')

        # Deleting field 'Configuracion.direccion'
        db.delete_column('configuracion_configuracion', 'direccion')

        # Deleting field 'Configuracion.email'
        db.delete_column('configuracion_configuracion', 'email')

        # Deleting field 'Configuracion.ciudad'
        db.delete_column('configuracion_configuracion', 'ciudad')

        # Deleting field 'Configuracion.telefono'
        db.delete_column('configuracion_configuracion', 'telefono')


    def backwards(self, orm):
        
        # Deleting model 'ContactData'
        db.delete_table('configuracion_contactdata')

        # Adding field 'Configuracion.movil'
        db.add_column('configuracion_configuracion', 'movil', self.gf('django.db.models.fields.CharField')(max_length=12, null=True, blank=True), keep_default=False)

        # Adding field 'Configuracion.codigo_postal'
        db.add_column('configuracion_configuracion', 'codigo_postal', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True), keep_default=False)

        # Adding field 'Configuracion.direccion'
        db.add_column('configuracion_configuracion', 'direccion', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True), keep_default=False)

        # Adding field 'Configuracion.email'
        db.add_column('configuracion_configuracion', 'email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True), keep_default=False)

        # Adding field 'Configuracion.ciudad'
        db.add_column('configuracion_configuracion', 'ciudad', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True), keep_default=False)

        # Adding field 'Configuracion.telefono'
        db.add_column('configuracion_configuracion', 'telefono', self.gf('django.db.models.fields.CharField')(max_length=12, null=True, blank=True), keep_default=False)


    models = {
        'configuracion.configuracion': {
            'Meta': {'object_name': 'Configuracion'},
            'actualizado_el': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'blog': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'blog_entradas': ('django.db.models.fields.IntegerField', [], {'default': '5', 'null': 'True', 'blank': 'True'}),
            'blog_rss': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
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
