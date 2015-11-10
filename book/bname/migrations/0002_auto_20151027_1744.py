# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bname', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BnamePost',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ISBN', models.CharField(max_length=150)),
                ('Title', models.CharField(max_length=150)),
                ('AuthorID', models.CharField(max_length=150)),
                ('Publisher', models.CharField(max_length=150)),
                ('PublishDate', models.CharField(max_length=150)),
                ('Price', models.CharField(max_length=150)),
            ],
        ),
        migrations.DeleteModel(
            name='BlogsPost',
        ),
    ]
