# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Afiliado',
            fields=[
                ('idafiliado', models.AutoField(serialize=False, primary_key=True)),
                ('documento', models.IntegerField(verbose_name=b'Documento')),
                ('nombre', models.CharField(max_length=200, verbose_name=b'Nombre')),
                ('sexo', models.CharField(max_length=1, verbose_name=b'Sexo', choices=[(b'M', b'Masculino'), (b'F', b'Femenino')])),
                ('cuil', models.CharField(max_length=200, verbose_name=b'Cuil')),
                ('calle', models.CharField(max_length=200, verbose_name=b'Calle')),
                ('nro', models.CharField(max_length=200, verbose_name=b'Nro')),
                ('piso', models.CharField(max_length=200, verbose_name=b'Piso', blank=True)),
                ('dpto', models.CharField(max_length=200, verbose_name=b'Dpto', blank=True)),
                ('e_civil', models.CharField(max_length=1, verbose_name=b'Estado Civil', choices=[(b'S', b'Soltero/a'), (b'C', b'Casado/a'), (b'D', b'Divorciado/a'), (b'V', b'Viudo/a')])),
                ('fecha_nac', models.DateField(verbose_name=b'Fecha de Nacimiento')),
                ('e_mail', models.CharField(max_length=200, verbose_name=b'Email', blank=b'True')),
                ('fecha_ingreso', models.DateField(verbose_name=b'Fecha de Ingreso')),
                ('lugar_empleo', models.CharField(max_length=200, verbose_name=b'Lugar de Empleo', blank=True)),
                ('antiguedad', models.IntegerField(verbose_name=b'Antiguedad')),
                ('categoria', models.CharField(max_length=10, verbose_name=b'Lugar de Empleo', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Familia',
            fields=[
                ('idfamilia', models.AutoField(serialize=False, primary_key=True)),
                ('documento', models.IntegerField(verbose_name=b'Documento')),
                ('nombre', models.CharField(max_length=200, verbose_name=b'Nombre')),
                ('parentesco', models.CharField(max_length=200, verbose_name=b'Parentesco')),
                ('estado', models.CharField(max_length=200, verbose_name=b'Estado')),
                ('fecha_nac', models.DateField(verbose_name=b'Fecha de Nacimiento')),
                ('fecha_vto', models.DateField(verbose_name=b'Fecha de Vencimiento')),
                ('afiliado', models.ForeignKey(db_column=b'idafiliado', verbose_name=b'Afiliado', to='gremio.Afiliado')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Localidad',
            fields=[
                ('idlocalidad', models.AutoField(serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=200, verbose_name=b'Nombre')),
                ('cp', models.IntegerField(verbose_name=b'CP')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='afiliado',
            name='localidad',
            field=models.ForeignKey(db_column=b'idlocalidad', verbose_name=b'Localidad', blank=True, to='gremio.Localidad'),
            preserve_default=True,
        ),
    ]
