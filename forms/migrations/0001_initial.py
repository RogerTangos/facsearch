# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Host'
        db.create_table(u'forms_host', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('lastLogin', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('officePhone', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('officeNumber', self.gf('django.db.models.fields.CharField')(max_length=7, null=True, blank=True)),
            ('mitId', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'forms', ['Host'])

        # Adding model 'Visitor'
        db.create_table(u'forms_visitor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('lastLogin', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('address1', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('address2', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('zipcode', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('officePhone', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('cellPhone', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('dietary', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
            ('videoRecording', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'forms', ['Visitor'])

        # Adding M2M table for field hosts on 'Visitor'
        m2m_table_name = db.shorten_name(u'forms_visitor_hosts')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('visitor', models.ForeignKey(orm[u'forms.visitor'], null=False)),
            ('host', models.ForeignKey(orm[u'forms.host'], null=False))
        ))
        db.create_unique(m2m_table_name, ['visitor_id', 'host_id'])

        # Adding model 'Assistant'
        db.create_table(u'forms_assistant', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('lastLogin', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('officePhone', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('officeNumber', self.gf('django.db.models.fields.CharField')(max_length=7, null=True, blank=True)),
            ('mitId', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'forms', ['Assistant'])

        # Adding M2M table for field facMembers on 'Assistant'
        m2m_table_name = db.shorten_name(u'forms_assistant_facMembers')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('assistant', models.ForeignKey(orm[u'forms.assistant'], null=False)),
            ('host', models.ForeignKey(orm[u'forms.host'], null=False))
        ))
        db.create_unique(m2m_table_name, ['assistant_id', 'host_id'])

        # Adding model 'Event'
        db.create_table(u'forms_event', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('start', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('end', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('creator', self.gf('django.db.models.fields.related.ForeignKey')(related_name='event_user_creator', blank=True, to=orm['auth.User'])),
            ('editor', self.gf('django.db.models.fields.related.ForeignKey')(default=<django.db.models.fields.related.ForeignKey: creator>, related_name='event_user_editor', blank=True, to=orm['auth.User'])),
            ('visitor', self.gf('django.db.models.fields.related.ForeignKey')(related_name='event_user_visitor', to=orm['forms.Visitor'])),
            ('lastEdit', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('detail', self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True)),
        ))
        db.send_create_signal(u'forms', ['Event'])


    def backwards(self, orm):
        # Deleting model 'Host'
        db.delete_table(u'forms_host')

        # Deleting model 'Visitor'
        db.delete_table(u'forms_visitor')

        # Removing M2M table for field hosts on 'Visitor'
        db.delete_table(db.shorten_name(u'forms_visitor_hosts'))

        # Deleting model 'Assistant'
        db.delete_table(u'forms_assistant')

        # Removing M2M table for field facMembers on 'Assistant'
        db.delete_table(db.shorten_name(u'forms_assistant_facMembers'))

        # Deleting model 'Event'
        db.delete_table(u'forms_event')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'forms.assistant': {
            'Meta': {'object_name': 'Assistant'},
            'facMembers': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['forms.Host']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastLogin': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'mitId': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'officeNumber': ('django.db.models.fields.CharField', [], {'max_length': '7', 'null': 'True', 'blank': 'True'}),
            'officePhone': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        },
        u'forms.event': {
            'Meta': {'object_name': 'Event'},
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'event_user_creator'", 'blank': 'True', 'to': u"orm['auth.User']"}),
            'detail': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'editor': ('django.db.models.fields.related.ForeignKey', [], {'default': '<django.db.models.fields.related.ForeignKey: creator>', 'related_name': "'event_user_editor'", 'blank': 'True', 'to': u"orm['auth.User']"}),
            'end': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastEdit': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'start': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'visitor': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'event_user_visitor'", 'to': u"orm['forms.Visitor']"})
        },
        u'forms.host': {
            'Meta': {'object_name': 'Host'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastLogin': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'mitId': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'officeNumber': ('django.db.models.fields.CharField', [], {'max_length': '7', 'null': 'True', 'blank': 'True'}),
            'officePhone': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        },
        u'forms.visitor': {
            'Meta': {'object_name': 'Visitor'},
            'address1': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'address2': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'cellPhone': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'dietary': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'hosts': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['forms.Host']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastLogin': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'officePhone': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'}),
            'videoRecording': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'zipcode': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['forms']