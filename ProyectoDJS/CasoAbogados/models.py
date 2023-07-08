from typing import Any, Dict, Tuple

from django.db import models

# Create your models here.
class Servicios(models.Model):

    ID_servicio = models.AutoField(primary_key=True, db_column='id')

    Abogado = models.CharField(max_length=50, verbose_name='Abogado')
    Tipo_de_Servicio = models.CharField(max_length=90, blank=True, null=True, verbose_name='Tipo_de_Servicio')
    fecha_creacion = models.DateField(auto_now=False, verbose_name='fecha_creacion')

    def __str__(self):
        return str(self.Abogado)

    class Meta:
        ordering = ['Abogado']
       

class Abogado(models.Model):
    rut = models.AutoField(primary_key=True, db_column='rut')
    nombre = models.CharField(max_length=200, blank=True, null=True, verbose_name='nombre ')
    apellido_paterno = models.CharField(max_length=20)
    apellido_materno = models.CharField(max_length=20)
    fec_nac = models.DateField(blank=False, null=False) 
    telefono = models.CharField(max_length=9)
    area = models.CharField(max_length=20)
    email = models.EmailField(unique=True, max_length=100, blank=True, null=True)
    img = models.ImageField(upload_to='img/', null=True, blank=True, verbose_name='img')

    def __str__(self):
        return str(self.rut)
    class Meta:      
        ordering = ['rut']

    def delete(self, using=None, keep_parents=False):
        self.img.storage.delete(self.img.name)
        return super().delete()    

        
