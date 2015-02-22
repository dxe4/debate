# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_debate_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(related_name='user_comments', blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
    ]
