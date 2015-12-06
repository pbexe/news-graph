# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_auto_20151203_1850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='node',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 6, 19, 21, 48, 765627, tzinfo=utc), verbose_name='Date Collected'),
        ),
    ]
