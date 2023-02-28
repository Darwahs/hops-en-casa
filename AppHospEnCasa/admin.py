from django.contrib import admin
from .models.persona import *
from .models.profesional_salud import *
from .models.paciente import *
from .models.familiar_paciente import *
from .models.historia_clinica import *
from .models.signo_vital import *

# Register your models here.
admin.site.register(TipoDocumento)
admin.site.register(Persona)
admin.site.register(RolPersona)
admin.site.register(Especialidad)
admin.site.register(Profesional_salud)
admin.site.register(Departamento)
admin.site.register(Ciudad)
admin.site.register(Paciente)
admin.site.register(FamiliarPaciente)
admin.site.register(HistoriaClinica)
admin.site.register(Sugerencia)
admin.site.register(Tipo_Signo_Vital)
admin.site.register(Signo_Vital)