# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drchrono', '0003_auto_20171004_1246'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='emergency_contact_number',
            new_name='emergency_contact_phone',
        ),
    ]
