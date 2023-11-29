from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('crear', views.crear_tarea, name='tareas_crear'),
    path('listado', views.tareas_listado, name='tareas_listado'),
    
    # Ejemplo de Url parametrizada
    path('saludar/<str:nombre_usuario>', views.saludar_por_nombre, name='saludar_por_nombre')
]