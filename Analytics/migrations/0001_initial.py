# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-12-22 15:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='busarrivalv2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_number', models.CharField(blank=True, max_length=6, null=True)),
                ('operator', models.CharField(blank=True, max_length=6, null=True)),
                ('destination_code', models.CharField(blank=True, max_length=50, null=True)),
                ('estimated_arrival', models.CharField(blank=True, max_length=220, null=True)),
                ('feature', models.CharField(blank=True, max_length=10, null=True)),
                ('latitue', models.CharField(blank=True, max_length=100, null=True)),
                ('longitute', models.CharField(blank=True, max_length=100, null=True)),
                ('load', models.CharField(blank=True, max_length=10, null=True)),
                ('logitute', models.CharField(blank=True, max_length=100, null=True)),
                ('origin_code', models.CharField(blank=True, max_length=20, null=True)),
                ('type', models.CharField(blank=True, max_length=5, null=True)),
                ('visit_number', models.CharField(blank=True, max_length=3, null=True)),
            ],
        ),
    ]
