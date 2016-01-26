# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0009_auto_20151206_1937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='node',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 6, 19, 55, 6, 993251, tzinfo=utc), verbose_name='Date Collected'),
        ),
    ]
