# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting model 'NamedURLSitemap'
        db.delete_table('web_namedurlsitemap')

        # Deleting model 'Sitemap'
        db.delete_table('web_sitemap')

        # Changing field 'ImagenPagina.descripcion'
        db.alter_column('web_imagenpagina', 'descripcion', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'VideoPagina.descripcion'
        db.alter_column('web_videopagina', 'descripcion', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'ArchivoPagina.descripcion'
        db.alter_column('web_archivopagina', 'descripcion', self.gf('django.db.models.fields.TextField')(null=True))


    def backwards(self, orm):
        
        # Adding model 'NamedURLSitemap'
        db.create_table('web_namedurlsitemap', (
            ('sitemap_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['web.Sitemap'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('web', ['NamedURLSitemap'])

        # Adding model 'Sitemap'
        db.create_table('web_sitemap', (
            ('es_activo', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('actualizado_el', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('imagen', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=60, unique=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('contenido', self.gf('django.db.models.fields.TextField')()),
            ('resumen', self.gf('django.db.models.fields.TextField')()),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=255, db_index=True)),
            ('creado_el', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=120, unique=True)),
        ))
        db.send_create_signal('web', ['Sitemap'])

        # User chose to not deal with backwards NULL issues for 'ImagenPagina.descripcion'
        raise RuntimeError("Cannot reverse this migration. 'ImagenPagina.descripcion' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'VideoPagina.descripcion'
        raise RuntimeError("Cannot reverse this migration. 'VideoPagina.descripcion' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'ArchivoPagina.descripcion'
        raise RuntimeError("Cannot reverse this migration. 'ArchivoPagina.descripcion' and its values cannot be restored.")


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
