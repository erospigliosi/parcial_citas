from django.contrib import admin
from .models import citas_medicas,paciente,doctores,usuarios
from .models import especialidades,tipo_documento_identidad,tipos_seguro


admin.site.register(citas_medicas)
admin.site.register(paciente)
admin.site.register(doctores)
admin.site.register(especialidades)
admin.site.register(tipo_documento_identidad)
admin.site.register(tipos_seguro)
admin.site.register(usuarios)

# Register your models here.
