from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
import json
from .models import Sala, Usuario,Monitor,Actividad,Inscripcion,ResponsableSala



#------------- ACTIVIDADES ---------------

def lista_actividades(request):

    actividades = Actividad.objects.all()

    # FILTROS
    tipo = request.GET.get('tipo')
    monitor = request.GET.get('monitor')

    if tipo:
        actividades = actividades.filter(tipo=tipo)

    if monitor:
        actividades = actividades.filter(monitor_id=monitor)

    data = []

    for actividad in actividades:
        data.append({
            'id': actividad.id,
            'nombre': actividad.nombre,
            'tipo': actividad.tipo,
            'horario': actividad.horario,
            'descripcion': actividad.descripcion,
            'duracion': actividad.duracion,
            'plazas_disponibles': actividad.plazas_disponibles,
            'monitor': actividad.monitor.nombre,
            'sala_principal': actividad.sala_principal.nombre
        })

    return JsonResponse(data, safe=False)


@csrf_exempt
def nueva_actividad(request):

    if request.method == 'POST':

        body = json.loads(request.body)

        actividad = Actividad.objects.create(
            nombre=body['nombre'],
            tipo=body['tipo'],
            horario=body['horario'],
            descripcion=body['descripcion'],
            duracion=body['duracion'],
            plazas_disponibles=body['plazas_disponibles'],
            monitor_id=body['monitor_id'],
            sala_principal_id=body['sala_principal_id']
        )

        return JsonResponse({
            'mensaje': 'Actividad creada',
            'id': actividad.id
        })

    return JsonResponse({'error': 'Método no permitido'})


def detalle_actividad(request, id):

    actividad = get_object_or_404(Actividad, id=id)

    data = {
        'id': actividad.id,
        'nombre': actividad.nombre,
        'tipo': actividad.tipo,
        'descripcion': actividad.descripcion,
        'monitor': actividad.monitor.nombre
    }

    return JsonResponse(data)


@csrf_exempt
def editar_actividad(request, id):

    actividad = get_object_or_404(Actividad, id=id)

    if request.method == 'PUT':

        body = json.loads(request.body)

        actividad.nombre = body['nombre']
        actividad.tipo = body['tipo']
        actividad.descripcion = body['descripcion']

        actividad.save()

        return JsonResponse({
            'mensaje': 'Actividad actualizada'
        })

    return JsonResponse({'error': 'Método no permitido'})


@csrf_exempt
def eliminar_actividad(request, id):

    actividad = get_object_or_404(Actividad, id=id)

    if request.method == 'DELETE':

        actividad.delete()

        return JsonResponse({
            'mensaje': 'Actividad eliminada'
        })

    return JsonResponse({'error': 'Método no permitido'})

# -------------- USUARIOS --------------


def lista_usuarios(request):

    usuarios = Usuario.objects.all()

    actividad = request.GET.get('actividad')

    if actividad:
        usuarios = usuarios.filter(
            actividades__id=actividad
        )

    data = list(usuarios.values())

    return JsonResponse(data, safe=False)


@csrf_exempt
def nuevo_usuario(request):

    if request.method == 'POST':

        body = json.loads(request.body)

        usuario = Usuario.objects.create(
            nombre=body['nombre'],
            edad=body['edad'],
            email=body['email'],
            telefono=body['telefono']
        )

        return JsonResponse({
            'mensaje': 'Usuario creado',
            'id': usuario.id
        })

    return JsonResponse({'error': 'Método no permitido'})


def detalle_usuario(request, id):

    usuario = get_object_or_404(Usuario, id=id)

    return JsonResponse({
        'id': usuario.id,
        'nombre': usuario.nombre,
        'edad': usuario.edad,
        'email': usuario.email
    })


@csrf_exempt
def editar_usuario(request, id):

    usuario = get_object_or_404(Usuario, id=id)

    if request.method == 'PUT':

        body = json.loads(request.body)

        usuario.nombre = body['nombre']
        usuario.edad = body['edad']
        usuario.email = body['email']
        usuario.telefono = body['telefono']

        usuario.save()

        return JsonResponse({
            'mensaje': 'Usuario actualizado'
        })

    return JsonResponse({'error': 'Método no permitido'})


@csrf_exempt
def eliminar_usuario(request, id):

    usuario = get_object_or_404(Usuario, id=id)

    if request.method == 'DELETE':

        usuario.delete()

        return JsonResponse({
            'mensaje': 'Usuario eliminado'
        })

    return JsonResponse({'error': 'Método no permitido'})



# -------------- MONITORES --------------


def lista_monitores(request):

    data = []

    for monitor in Monitor.objects.all():
        data.append({
            'id': monitor.id,
            'nombre': monitor.nombre,
            'especializacion': monitor.especializacion,
            'numero_actividades_asignadas':
                monitor.numero_actividades_asignadas
        })

    return JsonResponse(data, safe=False)


@csrf_exempt
def nuevo_monitor(request):

    if request.method == 'POST':

        body = json.loads(request.body)

        monitor = Monitor.objects.create(
            nombre=body['nombre'],
            especializacion=body['especializacion']
        )

        return JsonResponse({
            'mensaje': 'Monitor creado',
            'id': monitor.id
        })

    return JsonResponse({'error': 'Método no permitido'})


def detalle_monitor(request, id):

    monitor = get_object_or_404(Monitor, id=id)

    return JsonResponse({
        'id': monitor.id,
        'nombre': monitor.nombre,
        'especializacion': monitor.especializacion
    })


@csrf_exempt
def editar_monitor(request, id):

    monitor = get_object_or_404(Monitor, id=id)

    if request.method == 'PUT':

        body = json.loads(request.body)

        monitor.nombre = body['nombre']
        monitor.especializacion = body['especializacion']

        monitor.save()

        return JsonResponse({
            'mensaje': 'Monitor actualizado'
        })

    return JsonResponse({'error': 'Método no permitido'})


@csrf_exempt
def eliminar_monitor(request, id):

    monitor = get_object_or_404(Monitor, id=id)

    if request.method == 'DELETE':

        monitor.delete()

        return JsonResponse({
            'mensaje': 'Monitor eliminado'
        })

    return JsonResponse({'error': 'Método no permitido'})



# ------------- SALAS ---------------


def lista_salas(request):

    data = []

    for sala in Sala.objects.all():
        data.append({
            'id': sala.id,
            'nombre': sala.nombre,
            'capacidad': sala.capacidad,
            'ubicacion': sala.ubicacion
        })

    return JsonResponse(data, safe=False)


@csrf_exempt
def nueva_sala(request):

    if request.method == 'POST':

        body = json.loads(request.body)

        sala = Sala.objects.create(
            nombre=body['nombre'],
            capacidad=body['capacidad'],
            ubicacion=body['ubicacion'],
            responsable_id=body['responsable_id']
        )

        return JsonResponse({
            'mensaje': 'Sala creada',
            'id': sala.id
        })

    return JsonResponse({'error': 'Método no permitido'})


def detalle_sala(request, id):

    sala = get_object_or_404(Sala, id=id)

    return JsonResponse({
        'id': sala.id,
        'nombre': sala.nombre,
        'capacidad': sala.capacidad,
        'ubicacion': sala.ubicacion
    })


@csrf_exempt
def editar_sala(request, id):

    sala = get_object_or_404(Sala, id=id)

    if request.method == 'PUT':

        body = json.loads(request.body)

        sala.nombre = body['nombre']
        sala.capacidad = body['capacidad']
        sala.ubicacion = body['ubicacion']

        sala.save()

        return JsonResponse({
            'mensaje': 'Sala actualizada'
        })

    return JsonResponse({'error': 'Método no permitido'})


@csrf_exempt
def eliminar_sala(request, id):

    sala = get_object_or_404(Sala, id=id)

    if request.method == 'DELETE':

        sala.delete()

        return JsonResponse({
            'mensaje': 'Sala eliminada'
        })

    return JsonResponse({'error': 'Método no permitido'})



# ------------- INSCRIPCIONES ---------------


def listar_inscripciones(request, id):

    actividad = get_object_or_404(Actividad, id=id)

    data = []

    for inscripcion in Inscripcion.objects.filter(
        actividad=actividad
    ):

        data.append({
            'usuario_id': inscripcion.usuario.id,
            'usuario': inscripcion.usuario.nombre,
            'fecha_inscripcion':
                inscripcion.fecha_inscripcion,
            'asistencia':
                inscripcion.asistencia
        })

    return JsonResponse(data, safe=False)


@csrf_exempt
def inscribir_usuario(request, id):

    actividad = get_object_or_404(Actividad, id=id)

    if request.method == 'POST':

        body = json.loads(request.body)

        usuario = Usuario.objects.get(
            id=body['usuario_id']
        )

        inscripcion = Inscripcion.objects.create(
            usuario=usuario,
            actividad=actividad
        )

        return JsonResponse({
            'mensaje': 'Usuario inscrito',
            'inscripcion_id': inscripcion.id
        })

    return JsonResponse({'error': 'Método no permitido'})


@csrf_exempt
def cancelar_inscripcion(request, id, usuario_id):

    actividad = get_object_or_404(Actividad, id=id)

    inscripcion = get_object_or_404(
        Inscripcion,
        actividad=actividad,
        usuario_id=usuario_id
    )

    if request.method == 'DELETE':

        inscripcion.delete()

        return JsonResponse({
            'mensaje': 'Inscripción cancelada'
        })

    return JsonResponse({'error': 'Método no permitido'})