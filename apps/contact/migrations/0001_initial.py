# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'ContactConfig'
        db.create_table('contact_contactconfig', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('contacto_titulo', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('contacto_texto', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('contacto_analytics', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('contacto_imagen', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100)),
            ('exito_titulo', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('exito_texto', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('exito_analytics', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('exito_imagen', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100)),
            ('analytics_contacto', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('analytics_contactame', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('creado_el', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('actualizado_el', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('contact', ['ContactConfig'])

        # Adding model 'NotificationEmail'
        db.create_table('contact_notificationemail', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('configuracion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contact.ContactConfig'])),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
        ))
        db.send_create_signal('contact', ['NotificationEmail'])

        # Adding model 'Message'
        db.create_table('contact_message', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fecha', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('ip', self.gf('django.db.models.fields.IPAddressField')(max_length=15)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=150)),
            ('telefono', self.gf('django.db.models.fields.CharField')(max_length=9, null=True, blank=True)),
            ('mensaje', self.gf('django.db.models.fields.TextField')(max_length=256, null=True, blank=True)),
            ('condiciones', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('contact', ['Message'])

        # Adding model 'Response'
        db.create_table('contact_response', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fecha', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=150)),
            ('asunto', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('mensaje', self.gf('django.db.models.fields.TextField')(max_length=256, null=True, blank=True)),
            ('adjunto', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('contact', ['Response'])


    def backwards(self, orm):
        
        # Deleting model 'ContactConfig'
        db.delete_table('contact_contactconfig')

        # Deleting model 'NotificationEmail'
        db.delete_table('contact_notificationemail')

        # Deleting model 'Message'
        db.delete_table('contact_message')

        # Deleting model 'Response'
        db.delete_table('contact_response')


    models = {
        'contact.contactconfig': {
            'Meta': {'object_name': 'ContactConfig'},
            'actualizado_el': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'analytics_contactame': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'analytics_contacto': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'contacto_analytics': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'contacto_imagen': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'contacto_texto': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'contacto_titulo': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'creado_el': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'exito_analytics': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'exito_imagen': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'exito_texto': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'exito_titulo': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'contact.message': {
            'Meta': {'ordering': "['-fecha']", 'object_name': 'Message'},
            'condiciones': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '150'}),
            'fecha': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.IPAddressField', [], {'max_length': '15'}),
            'mensaje': ('django.db.models.fields.TextField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '9', 'null': 'True', 'blank': 'True'})
        },
        'contact.notificationemail': {
            'Meta': {'object_name': 'NotificationEmail'},
            'configuracion': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contact.ContactConfig']"}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'contact.response': {
            'Meta': {'object_name': 'Response'},
            'adjunto': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'asunto': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '150'}),
            'fecha': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mensaje': ('django.db.models.fields.TextField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        }
    }

    complete_apps = ['contact']
