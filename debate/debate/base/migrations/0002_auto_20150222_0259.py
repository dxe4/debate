# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='debate',
        ),
        migrations.AddField(
            model_name='comment',
            name='comment',
            field=models.ForeignKey(related_name='comment_comments', blank=True, to='base.Comment', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='solution',
            field=models.ForeignKey(related_name='solution_comments', blank=True, to='base.Solution', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(related_name='user_comments', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='follow',
            name='user',
            field=models.ForeignKey(related_name='followers', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='solution',
            name='debate',
            field=models.ForeignKey(related_name='solutions', to='base.Debate'),
            preserve_default=True,
        ),
    ]
