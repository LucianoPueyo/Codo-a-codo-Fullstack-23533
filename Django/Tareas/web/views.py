from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse, reverse_lazy

from .models import Tarea


def index(request):
    # La data real eventualmente será obtenida de la BBDD

    context = {
        'username': 'Raul',
        'fecha_hoy': datetime.now(),
        'edad': 25
    }

    return render(request, 'web/index.html', context)
    
def crear_tarea(request):
    return HttpResponse("Trabajo en progreso - En esta vista se van a poder dar de alta nuevas tareas")

# def tareas_listado(request):
#     # Estoy yendo a la BBDD a buscar todas las tareas
#     listado_tareas = Tarea.objects.all()

#     context = {
#         'listado_tareas': listado_tareas,
#         'usuario_activo': False
#     }

#     return render(request, 'web/tareas_listado.html', context)


def saludar_por_nombre(request, nombre_usuario):
    return HttpResponse(f"Bienvenid@ <b>{nombre_usuario}</b>")

# Vistas basadas en Clases -----------------------------------------------------------

class TareasListView(ListView):
    model = Tarea
    context_object_name = 'tareas_listado'
    template_name = 'web/tareas_listado.html'


class TareasCreateView(CreateView):
    model = Tarea
    template_name = 'web/tareas_crear.html'
    success_url = 'listado'
    fields = '__all__'


class TareasDetailView(DetailView):
    model = Tarea
    template_name = 'web/tareas_detalle.html'


class TareasUpdateView(UpdateView):
    model = Tarea
    template_name = 'web/tareas_modificar.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('tareas_detalle', kwargs={'pk': self.object.pk})
    

class TareasDeleteView(DeleteView):
    model = Tarea
    template_name = 'web/tareas_borrar.html'
    success_url = reverse_lazy('tareas_listado')