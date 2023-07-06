
from django.forms import ModelForm
from django import forms
from .models import  Servicios

class ServiciosForm(forms.ModelForm):
    class Meta:
        model = Servicios 
        #fields = ['ID', 'Abogado, 'Tipo de Servicio', 'fecha_creacion'] 
   
        fields = '__all__' 
