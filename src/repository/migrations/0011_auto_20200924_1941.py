# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-09-24 19:41
from __future__ import unicode_literals

import core.file_system
from django.db import migrations, models
import repository.models


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0010_auto_20200901_0737'),
    ]

    operations = [
        migrations.AddField(
            model_name='repository',
            name='footer',
            field=models.TextField(blank=True, default='Powered by Janeway', null=True),
        ),
        migrations.AlterField(
            model_name='preprint',
            name='meta_image',
            field=models.ImageField(blank=True, null=True, storage=core.file_system.JanewayFileSystemStorage(location='/vol/janeway/src/media'), upload_to=repository.models.preprint_file_upload),
        ),
        migrations.AlterField(
            model_name='repository',
            name='logo',
            field=models.ImageField(blank=True, null=True, storage=core.file_system.JanewayFileSystemStorage(location='/vol/janeway/src/media'), upload_to=repository.models.repo_media_upload),
        ),
    ]
