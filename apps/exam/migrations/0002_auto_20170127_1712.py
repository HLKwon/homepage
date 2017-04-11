# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-27 17:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('LogReg', '0004_auto_20170127_1445'),
        ('exam', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TravelPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('travelers', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='travelers', to='LogReg.User')),
            ],
        ),
        migrations.RemoveField(
            model_name='trip',
            name='travelers',
        ),
        migrations.AddField(
            model_name='travelplan',
            name='trips',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trips', to='exam.Trip'),
        ),
    ]