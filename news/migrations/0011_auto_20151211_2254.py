# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0010_auto_20151206_1955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='node',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 11, 22, 54, 25, 491211, tzinfo=utc), verbose_name='Date Collected'),
        ),
    ]
