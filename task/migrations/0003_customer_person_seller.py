# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_auto_20150425_1128'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('cpf', models.CharField(verbose_name='CPF', max_length=11)),
                ('first_name', models.CharField(verbose_name='Nome', max_length=20)),
                ('last_name', models.CharField(verbose_name='Sobrenome', max_length=20)),
                ('email', models.EmailField(unique=True, verbose_name='e-mail', max_length=75)),
            ],
            options={
                'ordering': ['first_name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, parent_link=True, primary_key=True, to='task.Person', serialize=False)),
            ],
            options={
                'verbose_name': 'cliente',
                'verbose_name_plural': 'clientes',
            },
            bases=('task.person',),
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, parent_link=True, primary_key=True, to='task.Person', serialize=False)),
                ('active', models.BooleanField(default=True, verbose_name='ativo')),
                ('internal', models.BooleanField(default=True, verbose_name='interno')),
                ('commissioned', models.BooleanField(default=True, verbose_name='comissionado')),
            ],
            options={
                'verbose_name': 'vendedor',
                'verbose_name_plural': 'vendedores',
            },
            bases=('task.person',),
        ),
    ]
