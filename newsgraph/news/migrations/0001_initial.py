# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Edge',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('source', models.URLField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='edge',
            name='destination',
            field=models.ForeignKey(to='news.Node', related_name='destination_node'),
        ),
        migrations.AddField(
            model_name='edge',
            name='origin',
            field=models.ForeignKey(to='news.Node', related_name='origin_node'),
        ),
    ]
