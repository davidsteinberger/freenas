# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-10 15:42
from __future__ import unicode_literals

from django.db import migrations, models
import freenasUI.freeadmin.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0011_auto_20170729_1515'),
    ]

    operations = [
        migrations.AddField(
            model_name='afp',
            name='afp_srv_hometimemachine',
            field=models.BooleanField(default=False, help_text='Enable Time Machine for home share.', verbose_name='Home Share Time Machine'),
        ),
    ]