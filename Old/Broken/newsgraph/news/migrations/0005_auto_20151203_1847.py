# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20151203_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='node',
            name='date',
            field=models.DateTimeField(verbose_name='Date Collected', default=datetime.datetime(2015, 12, 3, 18, 47, 55, 308529, tzinfo=utc)),
        ),
    ]
