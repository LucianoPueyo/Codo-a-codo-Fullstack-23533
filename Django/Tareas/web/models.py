from django.db import models

class Tarea(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    descripcion = models.CharField(max_length=100, verbose_name='Descripcion')
    categoria = models.CharField(max_length=100, verbose_name='Categoria', null=True)
    fecha_fin = models.DateField(verbose_name='Fecha de fin')
