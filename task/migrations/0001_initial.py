# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=50, verbose_name='nome')),
                ('description', models.TextField(verbose_name='descrição')),
                ('finalized', models.BooleanField(verbose_name='finalizado')),
                ('date_execution', models.DateTimeField(null=True, verbose_name='data de execução', blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
                ('modified_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'tarefas',
                'verbose_name': 'tarefa',
                'ordering': ['-created_at'],
            },
            bases=(models.Model,),
        ),
    ]
