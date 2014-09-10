# -*- coding: utf-8 -*-
from django.db import models
from django.utils.encoding import force_unicode
from django.contrib.admin import widgets  
from django.utils.encoding import force_unicode

# Create your models here.
TIPO_E_CIVIL = (
        ("N","No especifica"),
	("S","Soltero/a"),
	("SE","Separado/a"),
	("C","Casado/a"),
	("CO","Concubino/a"), 
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
    cp = models.IntegerField(verbose_name = 'CP', blank=True, null=True)
    
    def __unicode__(self):
        return force_unicode(self.nombre)        
        

class Afiliado(models.Model):
    idafiliado = models.AutoField(primary_key=True)#nroafiliado
    apellido = models.CharField(max_length=200, verbose_name='Apellido')
    nombre = models.CharField(max_length=200, verbose_name='Nombre')
    lugar_empleo = models.CharField(max_length=200, verbose_name='Lugar de Empleo', blank=True)
    documento = models.IntegerField(blank=False, verbose_name = 'Documento')
    direccion = models.CharField(max_length=200, verbose_name='Dirección', blank='True')
    sexo = models.CharField(max_length=1, choices = TIPO_SEXO, verbose_name='Sexo')    
    e_civil = models.CharField(max_length=1, choices=TIPO_E_CIVIL, verbose_name='Estado Civil', default='N')
    telefono = models.CharField(max_length=200, verbose_name='Telefono', blank='True')
    celular = models.CharField(max_length=200, verbose_name='Celular', blank='True')
    e_mail = models.CharField(max_length=200, verbose_name='Email', blank='True')
    fecha_nac = models.DateField(verbose_name= "Fecha de Nacimiento")
    ciudad = models.ForeignKey(Localidad,db_column='idlocalidad',verbose_name= "Ciudad", blank=True)
    cuil = models.CharField(max_length=200, verbose_name='Cuil',blank=True)
    fecha_ingreso = models.DateField(verbose_name= "Fecha de Ingreso",blank=True)
    antiguedad = models.IntegerField(verbose_name = 'Antiguedad',blank=True)
    categoria = models.CharField(max_length=10, verbose_name='Lugar de Empleo', blank=True)
    def __unicode__(self):
        return force_unicode(self.apellido)        

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
