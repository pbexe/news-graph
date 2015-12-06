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
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 3, 20, 57, 25, 712493, tzinfo=utc), verbose_name='Date Collected'),
        ),
    ]
