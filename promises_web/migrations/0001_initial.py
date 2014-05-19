# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TagExtraCss'
        db.create_table(u'promises_web_tagextracss', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('classes', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('tag', self.gf('django.db.models.fields.related.ForeignKey')(related_name='extracss', to=orm['taggit.Tag'])),
        ))
        db.send_create_signal(u'promises_web', ['TagExtraCss'])


    def backwards(self, orm):
        # Deleting model 'TagExtraCss'
        db.delete_table(u'promises_web_tagextracss')


    models = {
        u'promises_web.tagextracss': {
            'Meta': {'object_name': 'TagExtraCss'},
            'classes': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'extracss'", 'to': u"orm['taggit.Tag']"})
        },
        u'taggit.tag': {
            'Meta': {'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'})
        }
    }

    complete_apps = ['promises_web']