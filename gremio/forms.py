# -*- coding: utf-8 -*-
from django import forms
from gremio.models import *
from django.contrib.admin import widgets
from django.forms.widgets import *
#from django.contrib.admin.widgets import widgets
from django.forms.fields import DateField



class formAfiliado(forms.ModelForm):
    fecha_nac = forms.DateField(label="Fecha Nacimiento",widget=forms.DateInput(format='%d/%m/%Y',attrs={'id':'dp1','class':'datepicker','data-date-format':'dd/mm/yyyy'}))
    fecha_ingreso = forms.DateField(label="Fecha Ingreso",widget=forms.DateInput(format='%d/%m/%Y',attrs={'id':'dp2','class':'datepicker','data-date-format':'dd/mm/yyyy'}))
    
    class Meta:
        model = Afiliado
        fields =('idafiliado','apellido','nombre','lugar_empleo','documento','direccion','sexo','e_civil','telefono','celular','e_mail','fecha_nac','ciudad','cuil','fecha_ingreso','antiguedad','categoria')
    def __init__(self, *args, **kwargs):
        super(formAfiliado, self).__init__(*args, **kwargs)
        self.fields['sexo'].widget = forms.Select(choices=TIPO_SEXO)
        self.fields['e_civil'].widget = forms.Select(choices=TIPO_E_CIVIL)

