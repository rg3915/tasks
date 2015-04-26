# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0004_task_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='user',
            field=models.ForeignKey(blank=True, verbose_name='usuário', related_name='tasks', to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
    ]
