# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='finalized',
            field=models.BooleanField(default=False, verbose_name='finalizado'),
            preserve_default=True,
        ),
    ]
