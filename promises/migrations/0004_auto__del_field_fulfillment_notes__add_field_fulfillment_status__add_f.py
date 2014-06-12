# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Fulfillment.notes'
        db.delete_column(u'promises_fulfillment', 'notes')

        # Adding field 'Fulfillment.status'
        db.add_column(u'promises_fulfillment', 'status',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'Fulfillment.description'
        db.add_column(u'promises_fulfillment', 'description',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)


        # Changing field 'Fulfillment.promise'
        db.alter_column(u'promises_fulfillment', 'promise_id', self.gf('annoying.fields.AutoOneToOneField')(to=orm['promises.Promise'], unique=True))

    def backwards(self, orm):
        # Adding field 'Fulfillment.notes'
        db.add_column(u'promises_fulfillment', 'notes',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Deleting field 'Fulfillment.status'
        db.delete_column(u'promises_fulfillment', 'status')

        # Deleting field 'Fulfillment.description'
        db.delete_column(u'promises_fulfillment', 'description')


        # Changing field 'Fulfillment.promise'
        db.alter_column(u'promises_fulfillment', 'promise_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['promises.Promise'], unique=True))

    models = {
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
        },
        u'promises.category': {
            'Meta': {'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': '()', 'max_length': '50', 'populate_from': "'name'"})
        },
        u'promises.fulfillment': {
            'Meta': {'object_name': 'Fulfillment'},
            'description': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'percentage': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'promise': ('annoying.fields.AutoOneToOneField', [], {'to': u"orm['promises.Promise']", 'unique': 'True'}),
            'status': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'})
        },
        u'promises.informationsource': {
            'Meta': {'object_name': 'InformationSource'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'promise': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'information_sources'", 'to': u"orm['promises.Promise']"}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'promises.milestone': {
            'Meta': {'object_name': 'Milestone'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'promise': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'milestones'", 'to': u"orm['promises.Promise']"})
        },
        u'promises.promise': {
            'Meta': {'object_name': 'Promise'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'promises'", 'null': 'True', 'to': u"orm['promises.Category']"}),
            'date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '2048'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['popolo.Person']"})
        },
        u'promises.verificationdocument': {
            'Meta': {'object_name': 'VerificationDocument'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'promise': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'verification_documents'", 'null': 'True', 'to': u"orm['promises.Promise']"}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['promises']