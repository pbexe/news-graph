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
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('source', models.URLField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Story',
            fields=[
                ('source', models.URLField(primary_key=True, serialize=False, max_length=1000)),
                ('content', models.TextField(default='')),
            ],
        ),
        migrations.AddField(
            model_name='edge',
            name='destination',
            field=models.ForeignKey(related_name='destination_node', to='news.Node'),
        ),
        migrations.AddField(
            model_name='edge',
            name='origin',
            field=models.ForeignKey(related_name='origin_node', to='news.Node'),
        ),
    ]
