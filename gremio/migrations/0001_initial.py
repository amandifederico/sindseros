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
                ('apellido', models.CharField(max_length=200, verbose_name=b'Apellido')),
                ('nombre', models.CharField(max_length=200, verbose_name=b'Nombre')),
                ('lugar_empleo', models.CharField(max_length=200, verbose_name=b'Lugar de Empleo', blank=True)),
                ('documento', models.IntegerField(verbose_name=b'Documento')),
                ('direccion', models.CharField(max_length=200, verbose_name=b'Direcci\xc3\xb3n', blank=b'True')),
                ('sexo', models.CharField(max_length=1, verbose_name=b'Sexo', choices=[(b'M', b'Masculino'), (b'F', b'Femenino')])),
                ('e_civil', models.CharField(default=b'N', max_length=1, verbose_name=b'Estado Civil', choices=[(b'N', b'No especifica'), (b'S', b'Soltero/a'), (b'SE', b'Separado/a'), (b'C', b'Casado/a'), (b'CO', b'Concubino/a'), (b'D', b'Divorciado/a'), (b'V', b'Viudo/a')])),
                ('telefono', models.CharField(max_length=200, verbose_name=b'Telefono')),
                ('celular', models.CharField(max_length=200, verbose_name=b'Celular')),
                ('e_mail', models.CharField(max_length=200, verbose_name=b'Email', blank=b'True')),
                ('fecha_nac', models.DateField(verbose_name=b'Fecha de Nacimiento')),
                ('cuil', models.CharField(max_length=200, verbose_name=b'Cuil', blank=True)),
                ('fecha_ingreso', models.DateField(verbose_name=b'Fecha de Ingreso', blank=True)),
                ('antiguedad', models.IntegerField(verbose_name=b'Antiguedad', blank=True)),
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
                ('cp', models.IntegerField(verbose_name=b'CP', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='afiliado',
            name='ciudad',
            field=models.ForeignKey(db_column=b'idlocalidad', verbose_name=b'Ciudad', blank=True, to='gremio.Localidad'),
            preserve_default=True,
        ),
    ]
