from django.contrib import admin
from .models import Usuario, Monitor, ResponsableSala, Sala, Actividad, Inscripcion

admin.site.register(Usuario)
admin.site.register(Monitor)
admin.site.register(ResponsableSala)
admin.site.register(Sala)
admin.site.register(Actividad)
admin.site.register(Inscripcion)

