from django.shortcuts import render, redirect
from .models import Servicios
from django.contrib import messages
from django.shortcuts import render,get_object_or_404,redirect

from .forms import ServiciosForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError


# Create your views here.
def index(request):
    context={}
    return render(request, 'CasoAbogados/index.html', context)






def servicios(request):
    servicios = Servicios.objects.all()
    context={"servicios":servicios}
    return render(request, 'CasoAbogados/servicios.html', context)


def gestionser(request):
    servicios = Servicios.objects.all()
    context={"servicios":servicios}
    return render(request, 'CasoAbogados/Edicion/gestionser.html', context)

def nuevoser(request):
    formulario = ServiciosForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
       formulario.save()
       return redirect('gestionser')
    return render(request, "CasoAbogados/Edicion/nuevoservicio.html", {"formulario": formulario})    

#GESTION USUARIOS
# def login(request):
#     return render(request, "registration/login.html")

# def salir(request):
#     logout(request)
#     return redirect('/')


