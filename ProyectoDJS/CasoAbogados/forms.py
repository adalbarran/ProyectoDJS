from django.forms import ModelForm
from django import forms
from .models import Caso
from .models import Abogado

class CasoForm(forms.ModelForm):
    class Meta:
        model = Caso
        fields = '__all__' 

class AbogadoForm(forms.ModelForm):
    class Meta:
        model = Abogado
        fields = '__all__' 

class ContactForm(forms.Form):
    nombre = forms.CharField(label='Nombre')
    correo = forms.EmailField(label='Correo')
    numero = forms.CharField(label='Número de Teléfono')
    abogado = forms.ModelChoiceField(queryset=Abogado.objects.all(), label='Abogado')
    contexto = forms.CharField(label='Contexto del Caso', widget=forms.Textarea)