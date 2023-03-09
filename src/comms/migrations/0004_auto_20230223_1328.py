# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2023-02-23 13:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comms', '0003_newsitem_custom_byline'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='newsitem',
            options={'ordering': ('-posted', 'title')},
        ),
        migrations.AddField(
            model_name='newsitem',
            name='pinned',
            field=models.BooleanField(default=False, help_text='Pinned news items will appear at the top of the news list'),
        ),
        migrations.AlterField(
            model_name='newsitem',
            name='large_image_file',
            field=models.ForeignKey(blank=True, help_text='An image for the top of the news item page and thenews list page. Note that it will be automaticallycropped to 750px x 324px, so wide images work best.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='large_news_file', to='core.File'),
        ),
    ]
