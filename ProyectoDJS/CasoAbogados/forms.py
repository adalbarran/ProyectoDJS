
from django.forms import ModelForm
from django import forms
from .models import  Servicios
from .models import  Abogado

class ServiciosForm(forms.ModelForm):
    class Meta:
        model = Servicios 
        #fields = ['ID', 'Abogado, 'Tipo de Servicio', 'fecha_creacion'] 
   
        fields = '__all__' 

class AbogadoForm(forms.ModelForm):
    class Meta:
        model = Abogado
        #fields = ['rut', 'nombre', 'apellido_paterno', 'apellido_materno', 
         #         'fec_nac', 'telefono', 'area', 'email' 'img' ] 
   
        fields = '__all__' 

