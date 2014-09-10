# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gremio', '0002_auto_20140910_1221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='afiliado',
            name='celular',
            field=models.CharField(max_length=200, verbose_name=b'Celular', blank=b'True'),
        ),
        migrations.AlterField(
            model_name='afiliado',
            name='telefono',
            field=models.CharField(max_length=200, verbose_name=b'Telefono', blank=b'True'),
        ),
    ]
