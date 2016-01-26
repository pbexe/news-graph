# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_story_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='node',
            name='collectedFrom',
            field=models.ForeignKey(to='news.Story', related_name='story_collected_from', default=''),
        ),
        migrations.AddField(
            model_name='node',
            name='date',
            field=models.DateTimeField(verbose_name='Date Collected', default=datetime.datetime(2015, 12, 3, 18, 44, 49, 674370, tzinfo=utc)),
        ),
    ]
