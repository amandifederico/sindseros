# -*- coding: utf-8 -*-
from django.db import models
from django.utils.encoding import force_unicode
from django.contrib.admin import widgets  
from django.utils.encoding import force_unicode

# Create your models here.
TIPO_E_CIVIL = (
	("S","Soltero/a"),
	("C","Casado/a"), 
	("D","Divorciado/a"),
	("V","Viudo/a"),
)

TIPO_SEXO = (
	("M","Masculino"),
	("F","Femenino"), 
)

class Localidad(models.Model):
    idlocalidad = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200, verbose_name='Nombre')
    cp = models.IntegerField(blank=False, verbose_name = 'CP')
    
    def __unicode__(self):
        return force_unicode(self.nombre)        
        

class Afiliado(models.Model):
    idafiliado = models.AutoField(primary_key=True)#nroafiliado
    documento = models.IntegerField(blank=False, verbose_name = 'Documento')
    nombre = models.CharField(max_length=200, verbose_name='Nombre')
    sexo = models.CharField(max_length=1, choices = TIPO_SEXO, verbose_name='Sexo')
    cuil = models.CharField(max_length=200, verbose_name='Cuil')
    localidad = models.ForeignKey(Localidad,db_column='idlocalidad',verbose_name= "Localidad", blank=True)
    calle = models.CharField(max_length=200, verbose_name='Calle')
    nro = models.CharField(max_length=200, verbose_name='Nro')
    piso = models.CharField(max_length=200, verbose_name='Piso', blank=True)
    dpto = models.CharField(max_length=200, verbose_name='Dpto', blank=True)
    e_civil = models.CharField(max_length=1, choices=TIPO_E_CIVIL, verbose_name='Estado Civil')
    fecha_nac = models.DateField(verbose_name= "Fecha de Nacimiento")
    e_mail = models.CharField(max_length=200, verbose_name='Email', blank='True')
    fecha_ingreso = models.DateField(verbose_name= "Fecha de Ingreso")
    lugar_empleo = models.CharField(max_length=200, verbose_name='Lugar de Empleo', blank=True)
    antiguedad = models.IntegerField(blank=False, verbose_name = 'Antiguedad')
    categoria = models.CharField(max_length=10, verbose_name='Lugar de Empleo', blank=True)
    def __unicode__(self):
        return force_unicode(self.nombre)        

class Familia(models.Model):
    idfamilia = models.AutoField(primary_key=True)
    afiliado = models.ForeignKey(Afiliado,db_column='idafiliado',verbose_name= "Afiliado")
    documento = models.IntegerField(blank=False, verbose_name = 'Documento')
    nombre = models.CharField(max_length=200, verbose_name='Nombre')
    parentesco = models.CharField(max_length=200, verbose_name='Parentesco')
    estado = models.CharField(max_length=200, verbose_name='Estado')
    fecha_nac = models.DateField(verbose_name= "Fecha de Nacimiento")
    fecha_vto = models.DateField(verbose_name= "Fecha de Vencimiento")
    def __unicode__(self):
        return force_unicode(self.nombre)        