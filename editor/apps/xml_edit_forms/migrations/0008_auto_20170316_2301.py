# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-16 23:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xml_edit_forms', '0007_xmleditfield_field_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='xmleditform',
            name='form_name',
            field=models.CharField(default='', help_text='A descriptive name for this form.', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='xmleditfield',
            name='edit_action',
            field=models.CharField(choices=[('append', 'append'), ('replace', 'replace')], help_text='Whether the generated text should be appended to the node or replace it.', max_length=50),
        ),
        migrations.AlterField(
            model_name='xmleditfield',
            name='field_name',
            field=models.CharField(help_text='A descriptive name for this field.', max_length=100),
        ),
    ]
