# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-16 14:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xml_edit_forms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='xmleditfield',
            name='field_type',
            field=models.CharField(choices=[('textarea', 'Multiline text'), ('text', 'Single line text')], max_length=100),
        ),
    ]
