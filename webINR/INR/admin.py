from django.contrib import admin
from .models import Comentario, PacienteClinica, Diagnostico, Medicacion, Visita

admin.site.register(Comentario)
admin.site.register(PacienteClinica)
admin.site.register(Diagnostico)
admin.site.register(Medicacion)
admin.site.register(Visita)