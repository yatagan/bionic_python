# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coursera', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='group',
            field=models.CharField(default='group#1', max_length=100),
            preserve_default=False,
        ),
    ]
