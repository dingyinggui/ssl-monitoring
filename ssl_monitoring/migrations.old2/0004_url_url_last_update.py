# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-10 09:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ssl_monitoring', '0003_auto_20170310_0640'),
    ]

    operations = [
        migrations.AddField(
            model_name='url',
            name='url_last_update',
            field=models.DateTimeField(blank=True, default=1),
            preserve_default=False,
        ),
    ]
