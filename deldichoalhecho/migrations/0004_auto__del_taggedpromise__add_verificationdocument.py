# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'TaggedPromise'
        db.delete_table(u'deldichoalhecho_taggedpromise')

        # Adding model 'VerificationDocument'
        db.create_table(u'deldichoalhecho_verificationdocument', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('display_name', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('fulfillment', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['deldichoalhecho.Fulfillment'])),
        ))
        db.send_create_signal(u'deldichoalhecho', ['VerificationDocument'])


    def backwards(self, orm):
        # Adding model 'TaggedPromise'
        db.create_table(u'deldichoalhecho_taggedpromise', (
            ('content_object', self.gf('django.db.models.fields.related.ForeignKey')(related_name='tagged_promises', to=orm['deldichoalhecho.Promise'])),
            ('tag', self.gf('django.db.models.fields.related.ForeignKey')(related_name='tagged_promises', to=orm['deldichoalhecho.Category'])),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'deldichoalhecho', ['TaggedPromise'])

        # Deleting model 'VerificationDocument'
        db.delete_table(u'deldichoalhecho_verificationdocument')


    models = {
        u'deldichoalhecho.category': {
            'Meta': {'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': '()', 'max_length': '50', 'populate_from': "'name'"})
        },
        u'deldichoalhecho.fulfillment': {
            'Meta': {'object_name': 'Fulfillment'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'percentage': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'promise': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['deldichoalhecho.Promise']", 'unique': 'True'})
        },
        u'deldichoalhecho.informationsource': {
            'Meta': {'object_name': 'InformationSource'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'promise': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'information_sources'", 'to': u"orm['deldichoalhecho.Promise']"}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'deldichoalhecho.promise': {
            'Meta': {'object_name': 'Promise'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'promises'", 'null': 'True', 'to': u"orm['deldichoalhecho.Category']"}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['popolo.Person']"})
        },
        u'deldichoalhecho.verificationdocument': {
            'Meta': {'object_name': 'VerificationDocument'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'fulfillment': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['deldichoalhecho.Fulfillment']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
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