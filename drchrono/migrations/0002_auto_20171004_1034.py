# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drchrono', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='id',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='id',
        ),
        migrations.AddField(
            model_name='appointment',
            name='appointment_id',
            field=models.IntegerField(default=0, serialize=False, primary_key=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='patient_id',
            field=models.IntegerField(default=None, serialize=False, primary_key=True),
            preserve_default=False,
        ),
    ]
