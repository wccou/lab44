# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bname', '0002_auto_20151027_1744'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BnamePost',
            new_name='Book',
        ),
    ]
