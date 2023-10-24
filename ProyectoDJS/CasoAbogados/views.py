from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import render,get_object_or_404,redirect
from .models import Abogado, Caso
from .forms import CasoForm
from .forms import AbogadoForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from .forms import ContactForm

# Create your views here.
def index(request):
    context={}
    return render(request, 'CasoAbogados/index.html', context)

#GESTION USUARIOS
def register_view(request):
    if request.method == 'GET':
        return render(request, 'registration/register.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
                try:
                    user = User.objects.create_user(
                    username=request.POST['username'],
                    password =request.POST['password1'])
                    user.save()
                    login(request, user)
                    return redirect('index')
                except IntegrityError:
                    return render(request, 'registration/register.html', {
                    'form': UserCreationForm,
                    "error" : 'Usuario ya existe'
                })
            
        return render(request, 'registration/register.html', {
                    'form': UserCreationForm,
                    "error" : 'La contraseña no coincide'
                })

def login_user(request):
    if request.method == 'GET':
        return render(request, 'registration/login.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user is None:
            return render(request, 'registration/login.html', {
                'form': AuthenticationForm(),
                'error': 'Username o contraseña incorrecta'
            })
        else:
            login(request, user)
            return redirect('index')

def logout_view(request):
    logout(request)
    return redirect('index')

def abogados(request):
    abogados = Abogado.objects.all()
    context={"abogados":abogados}
    return render(request, 'CasoAbogados/abogados.html', context)


def casos(request):
    casos = Caso.objects.all()
    context = {"casos": casos}
    return render(request, 'CasoAbogados/casos.html', context)

# PESTAÑAS AGREGADAS POR XINO
def sucursales(request):
    return render(request, 'CasoAbogados/sucursales.html')

def servicios(request):
    return render(request, 'CasoAbogados/servicios.html')

#CRUDSERVICIOS
def gestioncasos(request):
    casos = Caso.objects.all()
    context = {"casos": casos}
    return render(request, 'CasoAbogados/Edicion/gestioncasos.html', context)


def nuevocaso(request):
    formulario = CasoForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('gestioncasos')
    return render(request, "CasoAbogados/Edicion/nuevocaso.html", {"formulario": formulario})


def editarcaso(request, ID_caso):
    caso = Caso.objects.get(ID_caso=ID_caso)
    formulario = CasoForm(request.POST or None, request.FILES or None, instance=caso)
    if formulario.is_valid() and request.method == 'POST':
        formulario.save()
        return redirect('gestioncasos')
    return render(request, "CasoAbogados/Edicion/editarcaso.html", {"formulario": formulario})


def borrarcaso(request, ID_caso):
    caso = Caso.objects.get(ID_caso=ID_caso)
    caso.delete()
    messages.success(request, '¡Caso Eliminado!')
    return redirect('gestioncasos')

#CRUDABOGADOS
@login_required
def gestionabo(request):
    abogados = Abogado.objects.all()
    context={"abogados":abogados}
    return render(request, 'CasoAbogados/Edit/gestionabo.html', context)

def nuevoabogado(request):
    formulario = AbogadoForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
       formulario.save()
       return redirect('gestionabo')
    return render(request, "CasoAbogados/Edit/nuevoabogado.html", {"formulario": formulario})    

def editarabogado(request, rut):
    abogado = Abogado.objects.get(rut=rut)
    formulario = AbogadoForm(request.POST or None, request.FILES or None, instance=abogado)
    if formulario.is_valid() and request.method == 'POST':
        formulario.save()
        return redirect('gestionabo')
    return render(request, "CasoAbogados/Edit/editarabogado.html", {"formulario": formulario})

def borrarabogado(request, rut):
    abogados = Abogado.objects.get(rut = rut)
    abogados.delete()
    messages.success(request, '¡Abogado Eliminado!')
    return redirect('gestionabo')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Procesar los datos del formulario
            nombre = form.cleaned_data['nombre']
            correo = form.cleaned_data['correo']
            numero = form.cleaned_data['numero']
            abogado = form.cleaned_data['abogado']
            contexto = form.cleaned_data['contexto']
            # Realizar las operaciones necesarias con los datos recibidos

            caso = Caso.objects.create(Abogado=abogado, titulo="Solicitud de Cliente", descripcion=contexto)


            # Redirigir o mostrar un mensaje de éxito al usuario
            return render(request, 'CasoAbogados/contact_success.html')
    else:
        form = ContactForm()
    
    return render(request,  'CasoAbogados/contact.html', {'form': form})
#GESTION USUARIOS
# def login(request):
#     return render(request, "registration/login.html")

# def salir(request):
#     logout(request)
#     return redirect('/')


