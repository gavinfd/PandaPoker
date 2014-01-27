# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Variation'
        db.create_table(u'variations_variation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('rating', self.gf('django.db.models.fields.IntegerField')()),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=5000)),
        ))
        db.send_create_signal(u'variations', ['Variation'])


    def backwards(self, orm):
        # Deleting model 'Variation'
        db.delete_table(u'variations_variation')


    models = {
        u'variations.variation': {
            'Meta': {'object_name': 'Variation'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '5000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'rating': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['variations']