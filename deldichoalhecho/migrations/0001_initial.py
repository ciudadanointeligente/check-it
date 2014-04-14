# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Promise'
        db.create_table(u'deldichoalhecho_promise', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['popit.Person'])),
        ))
        db.send_create_signal(u'deldichoalhecho', ['Promise'])

        # Adding model 'InformationSource'
        db.create_table(u'deldichoalhecho_informationsource', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('promise', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['deldichoalhecho.Promise'])),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('display_name', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'deldichoalhecho', ['InformationSource'])

        # Adding model 'Fulfillment'
        db.create_table(u'deldichoalhecho_fulfillment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('promise', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['deldichoalhecho.Promise'])),
            ('percentage', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal(u'deldichoalhecho', ['Fulfillment'])


    def backwards(self, orm):
        # Deleting model 'Promise'
        db.delete_table(u'deldichoalhecho_promise')

        # Deleting model 'InformationSource'
        db.delete_table(u'deldichoalhecho_informationsource')

        # Deleting model 'Fulfillment'
        db.delete_table(u'deldichoalhecho_fulfillment')


    models = {
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
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['popit.Person']"})
        },
        u'popit.apiinstance': {
            'Meta': {'object_name': 'ApiInstance'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'url': ('popit.fields.ApiInstanceURLField', [], {'unique': 'True', 'max_length': '200'})
        },
        u'popit.person': {
            'Meta': {'object_name': 'Person'},
            'api_instance': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['popit.ApiInstance']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'popit_id': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'popit_url': ('popit.fields.PopItURLField', [], {'default': "''", 'max_length': '200', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'summary': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        }
    }

    complete_apps = ['deldichoalhecho']