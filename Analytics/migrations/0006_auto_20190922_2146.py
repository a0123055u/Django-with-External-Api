# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-09-22 13:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Analytics', '0005_bustiming'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='busarrivalv2',
            name='destination_code',
        ),
        migrations.RemoveField(
            model_name='busarrivalv2',
            name='estimated_arrival',
        ),
        migrations.RemoveField(
            model_name='busarrivalv2',
            name='feature',
        ),
        migrations.RemoveField(
            model_name='busarrivalv2',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='busarrivalv2',
            name='load',
        ),
        migrations.RemoveField(
            model_name='busarrivalv2',
            name='longitute',
        ),
        migrations.RemoveField(
            model_name='busarrivalv2',
            name='origin_code',
        ),
        migrations.RemoveField(
            model_name='busarrivalv2',
            name='type',
        ),
        migrations.RemoveField(
            model_name='busarrivalv2',
            name='visit_number',
        ),
    ]