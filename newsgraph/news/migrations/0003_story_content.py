# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20151202_1909'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='content',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]
