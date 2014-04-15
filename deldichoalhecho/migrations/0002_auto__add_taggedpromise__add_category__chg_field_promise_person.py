# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TaggedPromise'
        db.create_table(u'deldichoalhecho_taggedpromise', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tag', self.gf('django.db.models.fields.related.ForeignKey')(related_name='tagged_promises', to=orm['deldichoalhecho.Category'])),
            ('content_object', self.gf('django.db.models.fields.related.ForeignKey')(related_name='tagged_promises', to=orm['deldichoalhecho.Promise'])),
        ))
        db.send_create_signal(u'deldichoalhecho', ['TaggedPromise'])

        # Adding model 'Category'
        db.create_table(u'deldichoalhecho_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=100)),
        ))
        db.send_create_signal(u'deldichoalhecho', ['Category'])


        # Changing field 'Promise.person'
        db.alter_column(u'deldichoalhecho_promise', 'person_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['popolo.Person']))

    def backwards(self, orm):
        # Deleting model 'TaggedPromise'
        db.delete_table(u'deldichoalhecho_taggedpromise')

        # Deleting model 'Category'
        db.delete_table(u'deldichoalhecho_category')


        # Changing field 'Promise.person'
        db.alter_column(u'deldichoalhecho_promise', 'person_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['popit.Person']))

    models = {
        u'deldichoalhecho.category': {
            'Meta': {'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'})
        },
        u'deldichoalhecho.fulfillment': {
            'Meta': {'object_name': 'Fulfillment'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'percentage': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'promise': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['deldichoalhecho.Promise']"})
        },
        u'deldichoalhecho.informationsource': {
            'Meta': {'object_name': 'InformationSource'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'promise': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['deldichoalhecho.Promise']"}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'deldichoalhecho.promise': {
            'Meta': {'object_name': 'Promise'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['popolo.Person']"})
        },
        u'deldichoalhecho.taggedpromise': {
            'Meta': {'object_name': 'TaggedPromise'},
            'content_object': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'tagged_promises'", 'to': u"orm['deldichoalhecho.Promise']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'tagged_promises'", 'to': u"orm['deldichoalhecho.Category']"})
        },
        u'popolo.person': {
            'Meta': {'object_name': 'Person'},
            'additional_name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'biography': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'birth_date': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'created_at': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'death_date': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'end_date': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'family_name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'gender': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'given_name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'honorific_prefix': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'honorific_suffix': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'patronymic_name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique': 'True', 'max_length': '50', 'populate_from': 'None', 'unique_with': '()'}),
            'sort_name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'start_date': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'summary': ('django.db.models.fields.CharField', [], {'max_length': '512', 'blank': 'True'}),
            'updated_at': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'})
        }
    }

    complete_apps = ['deldichoalhecho']