from django.shortcuts import render, redirect



# Create your views here.
def index(request):
    context={}
    return render(request, 'CasoAbogados/index.html', context)









#GESTION USUARIOS
# def login(request):
#     return render(request, "registration/login.html")

# def salir(request):
#     logout(request)
#     return redirect('/')


