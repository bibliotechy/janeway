# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-07-11 12:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BrokenDOI',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checked', models.DateTimeField()),
                ('resolves_to', models.URLField()),
                ('expected_to_resolve_to', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Identifier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_type', models.CharField(choices=[('doi', 'DOI'), ('uri', 'URI'), ('pubid', 'Publisher ID')], max_length=300)),
                ('identifier', models.CharField(max_length=300)),
                ('enabled', models.BooleanField(default=True)),
            ],
        ),
    ]
