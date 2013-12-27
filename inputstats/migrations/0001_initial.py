# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Game'
        db.create_table(u'inputstats_game', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('winner', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('game_date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'inputstats', ['Game'])

        # Adding model 'Player'
        db.create_table(u'inputstats_player', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('game', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inputstats.Game'])),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('standing', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'inputstats', ['Player'])


    def backwards(self, orm):
        # Deleting model 'Game'
        db.delete_table(u'inputstats_game')

        # Deleting model 'Player'
        db.delete_table(u'inputstats_player')


    models = {
        u'inputstats.game': {
            'Meta': {'object_name': 'Game'},
            'game_date': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'winner': ('django.db.models.fields.CharField', [], {'max_length': '200'})
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