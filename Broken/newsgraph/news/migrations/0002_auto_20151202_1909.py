# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='story',
            name='content',
        ),
        migrations.AddField(
            model_name='story',
            name='id',
            field=models.AutoField(default=0, verbose_name='ID', serialize=False, primary_key=True, auto_created=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='story',
            name='source',
            field=models.URLField(max_length=1000),
        ),
    ]
