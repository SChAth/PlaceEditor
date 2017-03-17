# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-16 21:29
from __future__ import unicode_literals

from django.db import migrations, models
import editor.apps.xml_edit_forms.fields


class Migration(migrations.Migration):

    dependencies = [
        ('xml_edit_forms', '0005_auto_20170301_1543'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='xmleditfield',
            name='text_generation',
        ),
        migrations.AddField(
            model_name='xmleditfield',
            name='form_field',
            field=models.CharField(choices=[('StandardCharField', 'StandardCharField')], default='', help_text='The form field used to generate text.', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='xmleditfield',
            name='edit_action',
            field=models.CharField(choices=[(editor.apps.xml_edit_forms.fields.append, 'append'), (editor.apps.xml_edit_forms.fields.replace, 'replace')], help_text='Whether the generated text should be appended to the node or replace it.', max_length=50),
        ),
        migrations.AlterField(
            model_name='xmleditform',
            name='file_type',
            field=models.CharField(choices=[('TEIPlace', 'TEIPlace'), ('TEIPerson', 'TEIPerson'), ('TEIWork', 'TEIWork'), ('TEIManuscript', 'TEIManuscript')], max_length=100),
        ),
    ]
