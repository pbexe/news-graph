# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0014_auto_20151212_2155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='node',
            name='date',
            field=models.DateTimeField(verbose_name='Date Collected', default=datetime.datetime(2015, 12, 13, 12, 37, 51, 693971, tzinfo=utc)),
        ),
    ]
