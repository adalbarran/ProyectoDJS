from django.shortcuts import render, redirect
from .models import Servicios
from django.contrib import messages
from django.shortcuts import render,get_object_or_404,redirect
from .models import Abogado
from .forms import ServiciosForm
from .forms import AbogadoForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError


# Create your views here.
def index(request):
    context={}
    return render(request, 'CasoAbogados/index.html', context)

#GESTION USUARIOS
def signin(request):
    if request.method == 'GET':
        return render(request, 'registration/login.html',{
        'form': AuthenticationForm
    })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST
            ['password'])
        if user is None:
            return render(request, 'registration/login.html',{
                'form': AuthenticationForm,
                'error': 'Username o contraseÃ±a incorrecta'
            })
        else:
            login(request, user)
            return redirect('index')

def signout(request):
    logout(request)
    return redirect('index')

def abogados(request):
    abogados = Abogado.objects.all()
    context={"abogados":abogados}
    return render(request, 'CasoAbogados/abogados.html', context)


def servicios(request):
    servicios = Servicios.objects.all()
    context={"servicios":servicios}
    return render(request, 'CasoAbogados/servicios.html', context)

#CRUDSERVICIOS
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

def editarservicio(request, ID_servicio):
    servicio = Servicios.objects.get(ID_servicio=ID_servicio)
    formulario = ServiciosForm(request.POST or None, request.FILES or None, instance=servicio)
    if formulario.is_valid() and request.method == 'POST':
        formulario.save()
        return redirect('gestionser')
    return render(request, "CasoAbogados/Edicion/editarservicio.html", {"formulario": formulario})

def borrarservicio(request, ID_servicio):
    servicios = Servicios.objects.get(ID_servicio = ID_servicio)
    servicios.delete()
    messages.success(request, '¡Servicio Eliminado!')
    return redirect('gestionser')

#CRUDABOGADOS
def gestionabo(request):
    abogados = Abogado.objects.all()
    context={"abogados":abogados}
    return render(request, 'CasoAbogados/Edicion/gestionabo.html', context)

def nuevoabogado(request):
    formulario = AbogadoForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
       formulario.save()
       return redirect('gestionabo')
    return render(request, "CasoAbogados/Edicion/nuevoabogado.html", {"formulario": formulario})    

def editarabogado(request, rut):
    abogados = Abogado.objects.get(rut=rut)
    formulario = AbogadoForm(request.POST or None, request.FILES or None, instance=abogado)
    if formulario.is_valid() and request.method == 'POST':
        formulario.save()
        return redirect('gestionabo')
    return render(request, "CasoAbogados/Edicion/editarabogado.html", {"formulario": formulario})

def borrarabogado(request, rut):
    abogados = Abogado.objects.get(rut = rut)
    abogados.delete()
    messages.success(request, '¡Abogado Eliminado!')
    return redirect('gestionabo')

#GESTION USUARIOS
# def login(request):
#     return render(request, "registration/login.html")

# def salir(request):
#     logout(request)
#     return redirect('/')


