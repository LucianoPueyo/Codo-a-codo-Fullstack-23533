from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


def index(request):

    # La data real eventualmente será obtenida de la BBDD

    context = {
        'username': 'Gastón',
        'fecha_hoy': datetime.now(),
        'edad': 25
    }

    return render(request, 'web/index.html', context)
    
def crear_tarea(request):
    return HttpResponse("Trabajo en progreso - En esta vista se van a poder dar de alta nuevas tareas")

def tareas_listado(request):

    # Esta lista esta hardcodeada.
    # Eventualmente, seremos capaces de obtener esta data de una BBDD Real.
    listado_tareas = [
        'Tarea 1',
        'Tarea 2'
    ]

    context = {
        'listado_tareas': listado_tareas,
        'usuario_activo': False
    }

    return render(request, 'web/tareas_listado.html', context)


def saludar_por_nombre(request, nombre_usuario):
    return HttpResponse(f"Bienvenid@ <b>{nombre_usuario}</b>")