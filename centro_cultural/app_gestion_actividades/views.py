from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404, redirect, render
import json
from .models import Sala, Usuario,Monitor,Actividad,Inscripcion,ResponsableSala

from .forms import ActividadForm, UsuarioForm, MonitorForm, SalaForm, InscripcionForm



#------------- Actividades ---------------
def lista_actividades(request):

    actividades = Actividad.objects.all()

    # filtros
    tipo = request.GET.get('tipo')
    monitor = request.GET.get('monitor')

    if tipo:
        actividades = actividades.filter(tipo=tipo)

    if monitor:
        actividades = actividades.filter(monitor_id=monitor)

    return render(request, 'lista.html', {
        'titulo': 'Actividades',
        'items': actividades,
        'crear_url': '/actividades/nueva/',
        'detalle_url': '/actividades/',
        'editar_url': '/actividades/',
        'eliminar_url': '/actividades/'
    })

def detalle_actividad(request, id):

    actividad = get_object_or_404(Actividad, id=id)

    return render(request, 'detalle.html', {
        'titulo': actividad.nombre,
        'datos': {
            'Nombre': actividad.nombre,
            'Tipo': actividad.tipo,
            'Descripción': actividad.descripcion,
            'Duración': actividad.duracion,
            'Monitor': actividad.monitor.nombre,
            'Sala': actividad.sala_principal.nombre
        }
    })

def nueva_actividad(request):

    if request.method == 'POST':
        form = ActividadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/actividades/')

    else:
        form = ActividadForm()

    return render(request, 'form.html', {
        'titulo': 'Nueva Actividad',
        'form': form
    })

def editar_actividad(request, id):

    actividad = get_object_or_404(Actividad, id=id)

    if request.method == 'POST':
        form = ActividadForm(request.POST, instance=actividad)
        if form.is_valid():
            form.save()
            return redirect('/actividades/')

    else:
        form = ActividadForm(instance=actividad)

    return render(request, 'form.html', {
        'titulo': 'Editar Actividad',
        'form': form
    })

def eliminar_actividad(request, id):

    actividad = get_object_or_404(Actividad, id=id)

    if request.method == 'POST':
        actividad.delete()
        return redirect('/actividades/')

    return render(request, 'eliminar.html', {
        'titulo': 'Eliminar Actividad',
        'item': actividad
    })



# -------------- Usuarios --------------
def lista_usuarios(request):

    actividad = request.GET.get('actividad')

    usuarios = Usuario.objects.all()

    if actividad:
        usuarios = usuarios.filter(actividades__id=actividad)

    return render(request, 'lista.html', {
        'titulo': 'Usuarios',
        'items': usuarios,
        'crear_url': '/usuarios/nuevo/',
        'detalle_url': '/usuarios/',
        'editar_url': '/usuarios/',
        'eliminar_url': '/usuarios/'
    })

def detalle_usuario(request, id):

    usuario = get_object_or_404(Usuario, id=id)

    return render(request, 'detalle.html', {
        'titulo': usuario.nombre,
        'datos': {
            'Nombre': usuario.nombre,
            'Edad': usuario.edad,
            'Email': usuario.email,
            'Teléfono': usuario.telefono
        }
    })

def nuevo_usuario(request):

    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/usuarios/')
    else:
        form = UsuarioForm()

    return render(request, 'form.html', {
        'titulo': 'Nuevo Usuario',
        'form': form
    })

def editar_usuario(request, id):

    usuario = get_object_or_404(Usuario, id=id)

    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('/usuarios/')
    else:
        form = UsuarioForm(instance=usuario)

    return render(request, 'form.html', {
        'titulo': 'Editar Usuario',
        'form': form
    })

def eliminar_usuario(request, id):

    usuario = get_object_or_404(Usuario, id=id)

    if request.method == 'POST':
        usuario.delete()
        return redirect('/usuarios/')

    return render(request, 'delete.html', {
        'titulo': 'Eliminar Usuario',
        'item': usuario
    })

# -------------- Monitores --------------

def lista_monitores(request):

    return render(request, 'lista.html', {
        'titulo': 'Monitores',
        'items': Monitor.objects.all(),
        'crear_url': '/monitores/nuevo/',
        'detalle_url': '/monitores/',
        'editar_url': '/monitores/',
        'eliminar_url': '/monitores/'
    })
def detalle_monitor(request, id):

    monitor = get_object_or_404(Monitor, id=id)

    return render(request, 'detalle.html', {
        'titulo': monitor.nombre,
        'datos': {
            'Nombre': monitor.nombre,
            'Especialización': monitor.especializacion,
            'Actividades asignadas': monitor.numero_actividades_asignadas
        }
    })
def nuevo_monitor(request):

    if request.method == 'POST':
        form = MonitorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/monitores/')
    else:
        form = MonitorForm()

    return render(request, 'form.html', {
        'titulo': 'Nuevo Monitor',
        'form': form
    })

def editar_monitor(request, id):

    monitor = get_object_or_404(Monitor, id=id)

    if request.method == 'POST':
        form = MonitorForm(request.POST, instance=monitor)
        if form.is_valid():
            form.save()
            return redirect('/monitores/')
    else:
        form = MonitorForm(instance=monitor)

    return render(request, 'form.html', {
        'titulo': 'Editar Monitor',
        'form': form
    })

def eliminar_monitor(request, id):

    monitor = get_object_or_404(Monitor, id=id)

    if request.method == 'POST':
        monitor.delete()
        return redirect('/monitores/')

    return render(request, 'eliminar.html', {
        'titulo': 'Eliminar Monitor',
        'item': monitor
    })

# ------------- Salas ---------------

def lista_salas(request):

    return render(request, 'lista.html', {
        'titulo': 'Salas',
        'items': Sala.objects.all(),
        'crear_url': '/salas/nueva/',
        'detalle_url': '/salas/',
        'editar_url': '/salas/',
        'eliminar_url': '/salas/'
    })
def detalle_sala(request, id):

    sala = get_object_or_404(Sala, id=id)

    return render(request, 'detalle.html', {
        'titulo': sala.nombre,
        'datos': {
            'Nombre': sala.nombre,
            'Capacidad': sala.capacidad,
            'Ubicación': sala.ubicacion,
            'Responsable': sala.responsable.nombre
        }
    })

def nueva_sala(request):

    if request.method == 'POST':
        form = SalaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/salas/')
    else:
        form = SalaForm()

    return render(request, 'form.html', {
        'titulo': 'Nueva Sala',
        'form': form
    })

def editar_sala(request, id):

    sala = get_object_or_404(Sala, id=id)

    if request.method == 'POST':
        form = SalaForm(request.POST, instance=sala)
        if form.is_valid():
            form.save()
            return redirect('/salas/')
    else:
        form = SalaForm(instance=sala)

    return render(request, 'form.html', {
        'titulo': 'Editar Sala',
        'form': form
    })

def eliminar_sala(request, id):

    sala = get_object_or_404(Sala, id=id)

    if request.method == 'POST':
        sala.delete()
        return redirect('/salas/')

    return render(request, 'eliminar.html', {
        'titulo': 'Eliminar Sala',
        'item': sala
    })

# ------------- Inscripciones ---------------

def listar_inscripciones(request, id):

    actividad = get_object_or_404(Actividad, id=id)

    inscripciones = Inscripcion.objects.filter(actividad=actividad)

    return render(request, 'inscripciones/lista.html', {
        'actividad': actividad,
        'inscripciones': inscripciones
    })
def inscribir_usuario(request, id):

    actividad = get_object_or_404(Actividad, id=id)

    if request.method == 'POST':
        form = InscripcionForm(request.POST)
        if form.is_valid():
            inscripcion = form.save(commit=False)
            inscripcion.actividad = actividad
            inscripcion.save()
            return redirect(f'/actividades/{id}/inscripciones/')
    else:
        form = InscripcionForm()

    return render(request, 'inscripciones/form.html', {
        'titulo': 'Inscribir Usuario',
        'form': form,
        'actividad': actividad
    })

def cancelar_inscripcion(request, id, usuario_id):

    actividad = get_object_or_404(Actividad, id=id)

    inscripcion = get_object_or_404(
        Inscripcion,
        actividad=actividad,
        usuario_id=usuario_id
    )

    if request.method == 'POST':
        inscripcion.delete()
        return redirect(f'/actividades/{id}/inscripciones/')

    return render(request, 'eliminar.html', {
        'titulo': 'Cancelar Inscripción',
        'item': inscripcion
    })