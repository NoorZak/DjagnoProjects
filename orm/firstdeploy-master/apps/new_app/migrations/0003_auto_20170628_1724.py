# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-28 17:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('new_app', '0002_auto_20170627_2335'),
    ]

    operations = [
        migrations.CreateModel(
            name='Joinedtrips',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Trips',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('travel_start', models.DateField()),
                ('travel_end', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usertrips', to='new_app.User')),
            ],
        ),
        migrations.AddField(
            model_name='joinedtrips',
            name='secret',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tripsjoined', to='new_app.Trips'),
        ),
        migrations.AddField(
            model_name='joinedtrips',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userjoined', to='new_app.User'),
        ),
    ]
