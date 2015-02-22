# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20150222_0259'),
    ]

    operations = [
        migrations.AddField(
            model_name='debate',
            name='url',
            field=models.CharField(default='o', max_length=200),
            preserve_default=False,
        ),
    ]
