# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('scheduled_time', models.DateTimeField()),
                ('duration', models.IntegerField()),
                ('status', models.CharField(max_length=100)),
                ('time_arrived', models.DateTimeField(null=True, verbose_name=b'time when patient checked in')),
                ('time_seen', models.DateTimeField(null=True, verbose_name=b'time when doctor saw patient')),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateTimeField()),
            ],
        ),
        migrations.AddField(
            model_name='appointment',
            name='patient',
            field=models.ForeignKey(to='drchrono.Patient'),
        ),
    ]
