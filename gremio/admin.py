from django.contrib import admin
from models import *
# Register your models here.

class LocalidadAdmin(admin.ModelAdmin):
    pass

class FamiliaAdmin(admin.ModelAdmin):
    raw_id_fields = ('afiliado',)
    pass

class AfiliadoAdmin(admin.ModelAdmin):
    raw_id_fields = ('ciudad',)
    list_display = ['apellido','nombre','lugar_empleo','documento','direccion','sexo','e_civil','telefono','celular','e_mail','fecha_nac','ciudad']
    pass

admin.site.register(Localidad, LocalidadAdmin)
admin.site.register(Familia, FamiliaAdmin)
admin.site.register(Afiliado, AfiliadoAdmin)
