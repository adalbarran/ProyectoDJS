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
        
def delete(self, using=None, keep_parents=False):
    if self.img:
        self.img.storage.delete(self.img.name)
    return super().delete(using=using, keep_parents=keep_parents)        