# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0013_auto_20151212_2016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='node',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 12, 21, 55, 43, 593872, tzinfo=utc), verbose_name='Date Collected'),
        ),
    ]
