# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-07-15 18:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0005_auto_20160715_1225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='events',
            field=models.ManyToManyField(null=True, to='events.Event'),
        ),
    ]