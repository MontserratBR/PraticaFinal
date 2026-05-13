from django.urls import path
from . import views

urlpatterns = [
    # --------- Actividades ------------- 
    path('actividades/',views.lista_actividades),
    path('actividades/nueva/',views.nueva_actividad),
    path('actividades/<int:id>/',views.detalle_actividad),
    path('actividades/<int:id>/editar/',views.editar_actividad),
    path('actividades/<int:id>/eliminar/',views.eliminar_actividad),
    
    # ----------- Usuarios ------------- 
    path('usuarios/',views.lista_usuarios),
    path('usuarios/nuevo/',views.nuevo_usuario),
    path('usuarios/<int:id>/',views.detalle_usuario),
    path('usuarios/<int:id>/editar/',views.editar_usuario),
    path('usuarios/<int:id>/eliminar/',views.eliminar_usuario),

    # ------------ Monitores -------------
    path('monitores/',views.lista_monitores),
    path('monitores/nuevo/',views.nuevo_monitor),
    path('monitores/<int:id>/',views.detalle_monitor),
    path('monitores/<int:id>/editar/',views.editar_monitor),
    path('monitores/<int:id>/eliminar/',views.eliminar_monitor),

    # -------------- Salas ----------------
    path('salas/',views.lista_salas),
    path('salas/nueva/',views.nueva_sala),
    path('salas/<int:id>/',views.detalle_sala),
    path('salas/<int:id>/editar/',views.editar_sala),
    path('salas/<int:id>/eliminar/',views.eliminar_sala),
   
    #-------------- Inscripciones --------------
    path('actividades/<int:id>/inscripciones/',views.listar_inscripciones),
    path('actividades/<int:id>/inscribir/',views.inscribir_usuario),
    path('actividades/<int:id>/inscripciones/<int:usuario_id>/eliminar/',views.cancelar_inscripcion),
]