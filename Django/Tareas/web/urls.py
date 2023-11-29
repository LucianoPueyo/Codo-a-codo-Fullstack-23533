from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('listado', views.TareasListView.as_view(), name='tareas_listado'),
    path('crear', views.TareasCreateView.as_view(), name='tareas_crear'),
    path('detalle/<pk>', views.TareasDetailView.as_view(), name='tareas_detalle'),
    path('modificar/<pk>', views.TareasUpdateView.as_view(), name='tareas_modificar'),
    path('borrar/<pk>', views.TareasDeleteView.as_view(), name='tareas_borrar'),

    # Ejemplo de Url parametrizada
    path('saludar/<str:nombre_usuario>', views.saludar_por_nombre, name='saludar_por_nombre')
]