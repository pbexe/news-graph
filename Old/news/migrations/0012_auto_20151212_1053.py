# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0011_auto_20151211_2254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='node',
            name='date',
            field=models.DateTimeField(verbose_name='Date Collected', default=datetime.datetime(2015, 12, 12, 10, 53, 33, 164972, tzinfo=utc)),
        ),
    ]
