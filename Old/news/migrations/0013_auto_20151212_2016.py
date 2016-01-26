# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0012_auto_20151212_1053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='node',
            name='date',
            field=models.DateTimeField(verbose_name='Date Collected', default=datetime.datetime(2015, 12, 12, 20, 16, 45, 911203, tzinfo=utc)),
        ),
    ]
