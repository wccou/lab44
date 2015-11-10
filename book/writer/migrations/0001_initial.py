# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('AuthorID', models.CharField(max_length=150)),
                ('Name', models.CharField(max_length=150)),
                ('Age', models.CharField(max_length=150)),
                ('Country', models.CharField(max_length=150)),
            ],
        ),
    ]
