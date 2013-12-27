# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Game.winner'
        db.delete_column(u'inputstats_game', 'winner')

        # Adding field 'Game.variation'
        db.add_column(u'inputstats_game', 'variation',
                      self.gf('django.db.models.fields.CharField')(default='hello', max_length=200),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Game.winner'
        db.add_column(u'inputstats_game', 'winner',
                      self.gf('django.db.models.fields.CharField')(default=datetime.datetime(2013, 12, 1, 0, 0), max_length=200),
                      keep_default=False)

        # Deleting field 'Game.variation'
        db.delete_column(u'inputstats_game', 'variation')


    models = {
        u'inputstats.game': {
            'Meta': {'object_name': 'Game'},
            'game_date': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'variation': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'inputstats.player': {
            'Meta': {'object_name': 'Player'},
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'game': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inputstats.Game']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'standing': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['inputstats']