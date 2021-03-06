# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-03 18:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Edge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.URLField(max_length=1000)),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date Collected')),
            ],
        ),
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date Collected')),
            ],
        ),
        migrations.CreateModel(
            name='Sentiment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sentiment', models.FloatField()),
                ('node', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sentiment_collected_from', to='relationships.Node')),
            ],
        ),
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.URLField(max_length=1000)),
                ('content', models.TextField()),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date Collected')),
            ],
        ),
        migrations.AddField(
            model_name='node',
            name='collectedFrom',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='story_collected_from', to='relationships.Story'),
        ),
        migrations.AddField(
            model_name='edge',
            name='destination',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='destination_node', to='relationships.Node'),
        ),
        migrations.AddField(
            model_name='edge',
            name='origin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='origin_node', to='relationships.Node'),
        ),
    ]
