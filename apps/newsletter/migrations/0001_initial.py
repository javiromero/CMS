# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Subscription'
        db.create_table('newsletter_subscription', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('subscribed', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(unique=True, max_length=75)),
            ('created_on', self.gf('django.db.models.fields.DateField')(blank=True)),
            ('updated_on', self.gf('django.db.models.fields.DateField')(blank=True)),
        ))
        db.send_create_signal('newsletter', ['Subscription'])


    def backwards(self, orm):
        
        # Deleting model 'Subscription'
        db.delete_table('newsletter_subscription')


    models = {
        'newsletter.subscription': {
            'Meta': {'object_name': 'Subscription'},
            'created_on': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'subscribed': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'updated_on': ('django.db.models.fields.DateField', [], {'blank': 'True'})
        }
    }

    complete_apps = ['newsletter']
