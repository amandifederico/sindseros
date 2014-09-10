# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gremio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='localidad',
            name='cp',
            field=models.IntegerField(null=True, verbose_name=b'CP', blank=True),
        ),
    ]
